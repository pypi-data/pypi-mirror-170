import builtins
import contextlib
import functools
import logging
import os
import shutil
import tempfile
import time
from decimal import Decimal
from pathlib import Path
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Iterator,
    List,
    Literal,
    Optional,
    Tuple,
    Type,
    Union,
)

import psycopg.rows
import psycopg.sql
from pgtoolkit import conf as pgconf
from pgtoolkit import ctl, pgpass
from pgtoolkit.ctl import Status as Status
from pydantic import SecretStr

from . import cmd, conf, databases, db, exceptions, hookimpl, roles, util
from .models import interface, system
from .postgresql import Standby
from .settings import EXTENSIONS_CONFIG, PostgreSQLVersion
from .task import task
from .types import ConfigChanges, PostgreSQLStopMode

if TYPE_CHECKING:
    from .ctx import BaseContext

logger = logging.getLogger(__name__)


@functools.lru_cache(maxsize=len(PostgreSQLVersion) + 1)
def pg_ctl(bindir: Path, *, ctx: "BaseContext") -> ctl.PGCtl:
    return ctl.PGCtl(bindir, run_command=ctx.run)


@hookimpl(trylast=True)  # type: ignore[misc]
def instance_init_replication(
    ctx: "BaseContext", instance: system.BaseInstance, standby: "Standby"
) -> Optional[bool]:
    with tempfile.TemporaryDirectory() as _tmpdir:
        tmpdir = Path(_tmpdir)
        # pg_basebackup will also copy config files from primary datadir.
        # So to have expected configuration at this stage we have to backup
        # postgresql.conf & pg_hba.conf (created by prior pg_ctl init) and
        # restore after pg_basebackup finishes.
        keep = {"postgresql.conf", "pg_hba.conf"}
        for name in keep:
            shutil.copyfile(instance.datadir / name, tmpdir / name)
        ctx.rmtree(instance.datadir)
        ctx.rmtree(instance.waldir)
        cmd = [
            str(instance.bindir / "pg_basebackup"),
            "--pgdata",
            str(instance.datadir),
            "--write-recovery-conf",
            "--checkpoint=fast",
            "--no-password",
            "--progress",
            "--verbose",
            "--dbname",
            standby.primary_conninfo,
            "--waldir",
            str(instance.waldir),
        ]

        if standby.slot:
            cmd += ["--slot", standby.slot]

        ctx.run(cmd, check=True)
        for name in keep:
            shutil.copyfile(tmpdir / name, instance.datadir / name)
    return True


@hookimpl(trylast=True)  # type: ignore[misc]
def initdb(
    ctx: "BaseContext", manifest: "interface.Instance", instance: system.BaseInstance
) -> Literal[True]:
    """Initialize the PostgreSQL database cluster with plain initdb."""
    # Would raise SystemError if requested postgresql binaries are not
    # available or if versions mismatch.
    pgctl = pg_ctl(instance.bindir, ctx=ctx)

    settings = ctx.settings
    surole = manifest.surole(settings)
    opts: Dict[str, Union[str, Literal[True]]] = {
        "waldir": str(instance.waldir),
        "username": surole.name,
    }
    opts.update(
        {
            f"auth_{m}": v.value
            for m, v in manifest.auth_options(settings.postgresql.auth).dict().items()
        }
    )
    opts.update(
        manifest.initdb_options(settings.postgresql.initdb).dict(exclude_none=True)
    )

    if surole.password:
        with tempfile.NamedTemporaryFile("w") as pwfile:
            pwfile.write(surole.password.get_secret_value())
            pwfile.flush()
            pgctl.init(instance.datadir, pwfile=pwfile.name, **opts)
    else:
        pgctl.init(instance.datadir, **opts)

    return True


@task("initializing PostgreSQL instance")
def init(ctx: "BaseContext", manifest: interface.Instance) -> system.PostgreSQLInstance:
    """Initialize a PostgreSQL instance."""
    try:
        return system.PostgreSQLInstance.system_lookup(
            ctx, (manifest.name, manifest.version)
        )
    except exceptions.InstanceNotFound:
        pass

    postgresql_settings = ctx.settings.postgresql
    postgresql_settings.socket_directory.mkdir(parents=True, exist_ok=True)

    sys_instance = system.BaseInstance.get(manifest.name, manifest.version, ctx)

    ctx.hook.initdb(ctx=ctx, manifest=manifest, instance=sys_instance)

    # Possibly comment out everything in postgresql.conf, as in upstream
    # sample file, but in contrast with some distribution packages.
    postgresql_conf = ctx.hook.postgresql_conf(instance=sys_instance)
    pgconfig = pgconf.Configuration(str(postgresql_conf))
    with postgresql_conf.open() as f:
        includes = builtins.list(pgconfig.parse(f))
    assert (
        not includes
    ), f"default {postgresql_conf} contains unexpected include directives"
    with pgconfig.edit() as entries:
        commented = set()
        for name, entry in entries.items():
            if not entry.commented:
                entry.commented = True
                commented.add(name)
    logger.debug(
        "commenting PostgreSQL configuration entries in %s: %s",
        postgresql_conf,
        ", ".join(sorted(commented)),
    )
    pgconfig.save()

    standby = manifest._standby()
    if standby:
        ctx.hook.instance_init_replication(
            ctx=ctx, instance=sys_instance, manifest=manifest, standby=standby
        )

    ctx.hook.configure_auth(
        settings=ctx.settings, instance=sys_instance, manifest=manifest
    )

    sys_instance.psqlrc.write_text(
        "\n".join(
            [
                f"\\set PROMPT1 '[{sys_instance}] %n@%~%R%x%# '",
                "\\set PROMPT2 ' %R%x%# '",
            ]
        )
        + "\n"
    )

    ctx.hook.enable_service(
        ctx=ctx, service=ctx.hook.postgresql_service_name(), name=sys_instance.qualname
    )

    return system.PostgreSQLInstance.system_lookup(ctx, sys_instance)


@init.revert("deleting PostgreSQL instance")
def revert_init(ctx: "BaseContext", manifest: interface.Instance) -> None:
    """Un-initialize a PostgreSQL instance."""
    sys_instance = system.BaseInstance.get(manifest.name, manifest.version, ctx)
    ctx.hook.disable_service(
        ctx=ctx,
        service=ctx.hook.postgresql_service_name(),
        name=sys_instance.qualname,
        now=True,
    )

    for path in (sys_instance.datadir, sys_instance.waldir):
        if path.exists():
            ctx.rmtree(path)


def configure(
    ctx: "BaseContext",
    manifest: interface.Instance,
    *,
    run_hooks: bool = True,
    _creating: bool = False,
) -> ConfigChanges:
    """Write instance's configuration in postgresql.conf."""
    with configure_context(
        ctx, manifest, run_hooks=run_hooks, _creating=_creating
    ) as changes:
        return changes


@contextlib.contextmanager
def configure_context(
    ctx: "BaseContext",
    manifest: interface.Instance,
    *,
    run_hooks: bool = True,
    _creating: bool = False,
) -> Iterator[ConfigChanges]:
    """Context manager to write instance's configuration in postgresql.conf
    while pausing for further actions before calling 'instance_configure'
    hooks.


    Also compute changes to the overall PostgreSQL configuration and return it
    as a 'ConfigChanges' dictionary.
    """
    logger.info("configuring PostgreSQL instance")
    instance = system.BaseInstance.get(manifest.name, manifest.version, ctx)

    config = configuration(ctx, manifest, instance)
    changes = ctx.hook.configure_postgresql(
        ctx=ctx, manifest=manifest, configuration=config, instance=instance
    )

    yield changes

    if run_hooks:
        ctx.hook.instance_configure(
            ctx=ctx,
            manifest=manifest,
            config=config,
            changes=changes,
            creating=_creating,
        )

    if not _creating:
        sys_instance = system.Instance.system_lookup(
            ctx, (manifest.name, manifest.version)
        )
        check_pending_actions(ctx, sys_instance, changes, manifest.restart_on_changes)


@hookimpl(trylast=True)  # type: ignore[misc]
def configure_postgresql(
    ctx: "BaseContext",
    manifest: "interface.Instance",
    configuration: pgconf.Configuration,
    instance: "system.BaseInstance",
) -> ConfigChanges:
    postgresql_conf = pgconf.parse(instance.datadir / "postgresql.conf")
    config_before = postgresql_conf.as_dict()
    conf.update(postgresql_conf, **configuration.as_dict())
    config_after = postgresql_conf.as_dict()
    changes = conf.changes(config_before, config_after)

    if changes:
        postgresql_conf.save()

    return changes


def configure_ssl(
    ctx: "BaseContext",
    configuration: Dict[str, Any],
    name: str,
    directory: Path,
) -> Dict[str, str]:
    """Possibly generate SSL certificate files in 'directory' based on specified 'configuration'."""
    if not configuration.get("ssl"):
        return {}
    try:
        cert, key = Path(configuration["ssl_cert_file"]), Path(
            configuration["ssl_key_file"]
        )
    except KeyError:
        cert, key = Path(f"{name}.crt"), Path(f"{name}.key")
        directory.mkdir(exist_ok=True, parents=True)
    if not cert.is_absolute():
        cert = directory / cert
    if not key.is_absolute():
        key = directory / key
    if not cert.exists() and not key.exists():
        certcontent, keycontent = util.generate_certificate(run_command=ctx.run)
        cert.write_text(certcontent)
        key.touch(mode=0o600)
        key.write_text(keycontent)
    else:
        assert (
            cert.exists() and key.exists()
        ), f"One of SSL certificate files {cert} or {key} exists but the other does not"
    return {"ssl_cert_file": str(cert), "ssl_key_file": str(key)}


def configuration(
    ctx: "BaseContext", manifest: interface.Instance, instance: system.BaseInstance
) -> pgconf.Configuration:
    """Return instance configuration from manifest.

    `manifest.configuration.ssl`, `manifest.configuration.ssl_cert_file` and
    `manifest.configuration.ssl_key_file` control the SSL configuration.
    If the `ssl` field is:
       - False, SSL is not enabled
       - True (without specifying cert and key), a self-signed certificate is generated
       - True and the ssl_cert_file and ssl_key_file are present, the instance will be
         configured with those files (if they exist)

    'shared_buffers' and 'effective_cache_size' setting, if defined and set to
    a percent-value, will be converted to proper memory value relative to the
    total memory available on the system.
    """
    confitems: Dict[str, pgconf.Value] = {
        "cluster_name": manifest.name,
        "port": manifest.port,
    }

    # Load base configuration from site settings.
    postgresql_conf_template = util.site_config("postgresql", "postgresql.conf")
    if postgresql_conf_template is not None:
        confitems.update(pgconf.parse(postgresql_conf_template).as_dict())

    # Transform initdb options as configuration parameters.
    locale = manifest.initdb_options(ctx.settings.postgresql.initdb).locale
    if locale:
        for key in ("lc_messages", "lc_monetary", "lc_numeric", "lc_time"):
            confitems.setdefault(key, locale)

    confitems.update(manifest.configuration)

    ssl_cert_directory = ctx.settings.postgresql.ssl_cert_directory
    ssl_config = configure_ssl(
        ctx, manifest.configuration, instance.qualname, ssl_cert_directory
    )
    confitems.update(ssl_config)

    try:
        logdir = confitems["log_directory"]
    except KeyError:
        pass
    else:
        assert isinstance(logdir, str)  # per model validation
        conf.log_directory(instance.datadir, Path(logdir)).mkdir(
            exist_ok=True, parents=True
        )

    spl = ""
    spl_list = []
    for extension in manifest.extensions:
        if EXTENSIONS_CONFIG[extension][0]:
            spl_list.append(extension)
    spl = ", ".join(spl_list)

    for r in ctx.hook.instance_configuration(ctx=ctx, manifest=manifest):
        for k, v in r.entries.items():
            if k == "shared_preload_libraries":
                spl = conf.merge_lists(spl, v.value)
            else:
                confitems[k] = v.value

    if spl:
        confitems["shared_preload_libraries"] = spl

    conf.format_values(confitems, ctx.settings.postgresql)

    return conf.make(manifest.name, **confitems)


@contextlib.contextmanager
def running(ctx: "BaseContext", instance: system.Instance) -> Iterator[None]:
    """Context manager to temporarily start an instance and run hooks."""
    if status(ctx, instance) == Status.running:
        yield
        return

    start(ctx, instance)
    try:
        yield
    finally:
        stop(ctx, instance)


@contextlib.contextmanager
def postgresql_running(
    ctx: "BaseContext", instance: system.PostgreSQLInstance
) -> Iterator[None]:
    """Context manager to temporarily start a postgreSQL instance."""
    if status(ctx, instance) == Status.running:
        yield
        return

    start_postgresql(
        ctx,
        instance,
        foreground=False,
        wait=True,
        # Keep logs to stderr, uncollected, to get meaningful errors on our side.
        logging_collector="off",
        log_destination="stderr",
    )
    try:
        yield
    finally:
        stop_postgresql(ctx, instance, mode="fast", wait=True)


@contextlib.contextmanager
def stopped(
    ctx: "BaseContext",
    instance: system.Instance,
    *,
    timeout: int = 10,
) -> Iterator[None]:
    """Context manager to temporarily stop an instance.

    :param timeout: delay to wait for instance stop.

    :raises ~exceptions.InstanceStateError: when the instance did stop after
        specified `timeout` (in seconds).
    """
    if status(ctx, instance) == Status.not_running:
        yield
        return

    stop(ctx, instance)
    for __ in range(timeout):
        time.sleep(1)
        if status(ctx, instance) == Status.not_running:
            break
    else:
        raise exceptions.InstanceStateError(f"{instance} not stopped after {timeout}s")
    try:
        yield
    finally:
        start(ctx, instance)


def start(
    ctx: "BaseContext",
    instance: system.Instance,
    *,
    foreground: bool = False,
    wait: bool = True,
) -> None:
    """Start an instance.

    :param wait: possibly wait for PostgreSQL to get ready.
    :param foreground: start postgres in the foreground, replacing the current
        process.

    .. note:: When starting in "foreground", hooks will not be triggered and
        `wait` parameter have no effect.
    """
    logger.info("starting instance %s", instance)

    if status(ctx, instance) == Status.running:
        logger.warning("instance %s is already started", instance)
        return

    ctx.settings.postgresql.socket_directory.mkdir(parents=True, exist_ok=True)

    started = False
    if not foreground:
        started = ctx.hook.start_service(
            ctx=ctx, service=ctx.hook.postgresql_service_name(), name=instance.qualname
        )
        if started and wait:
            wait_ready(ctx, instance)
    if not started:
        ctx.hook.start_postgresql(
            ctx=ctx, instance=instance, foreground=foreground, wait=wait
        )

    if wait:
        if foreground:
            logger.debug("not running hooks for a foreground start")
        else:
            ctx.hook.instance_start(ctx=ctx, instance=instance)


@hookimpl(trylast=True)  # type: ignore[misc]
def start_postgresql(
    ctx: "BaseContext",
    instance: system.PostgreSQLInstance,
    foreground: bool,
    wait: bool,
    **runtime_parameters: str,
) -> Literal[True]:
    logger.info("starting PostgreSQL")
    postgres = instance.bindir / "postgres"
    command = [str(postgres), "-D", str(instance.datadir)]
    for name, value in runtime_parameters.items():
        command.extend(["-c", f"{name}={value}"])
    if foreground:
        cmd.execute_program(command, logger=logger)
    else:
        with cmd.Program(command, pidfile=None, logger=logger):
            if wait:
                wait_ready(ctx, instance)
    return True


def status(ctx: "BaseContext", instance: system.BaseInstance) -> Status:
    """Return the status of an instance."""
    logger.debug("get status of PostgreSQL instance %s", instance)
    return pg_ctl(instance.bindir, ctx=ctx).status(instance.datadir)


def is_running(ctx: "BaseContext", instance: system.BaseInstance) -> bool:
    """Return True if the instance is running based on its status."""
    return status(ctx, instance) == Status.running


def is_ready(ctx: "BaseContext", instance: system.PostgreSQLInstance) -> bool:
    """Return True if the instance is ready per pg_isready."""
    logger.debug("checking if PostgreSQL instance %s is ready", instance)
    pg_isready = str(instance.bindir / "pg_isready")
    postgresql_settings = ctx.settings.postgresql
    dsn = db.dsn(instance, postgresql_settings, user=postgresql_settings.surole.name)
    env = postgresql_settings.libpq_environ(
        ctx, instance, postgresql_settings.surole.name
    )
    r = ctx.run([pg_isready, "-d", dsn], env=env)
    if r.returncode == 0:
        return True
    assert r.returncode in (
        1,
        2,
    ), f"Unexpected exit status from pg_isready {r.returncode}: {r.stdout}, {r.stderr}"
    return False


def wait_ready(
    ctx: "BaseContext", instance: system.PostgreSQLInstance, *, timeout: int = 10
) -> None:
    for __ in range(timeout):
        if is_ready(ctx, instance):
            return
        time.sleep(1)
    raise exceptions.InstanceStateError(f"{instance} not ready after {timeout}s")


def check_status(
    ctx: "BaseContext", instance: system.BaseInstance, expected: Status
) -> None:
    """Check actual instance status with respected to `expected` one.

    :raises ~exceptions.InstanceStateError: in case the actual status is not expected.
    """
    st = status(ctx, instance)
    if st != expected:
        raise exceptions.InstanceStateError(f"instance is {st.name}")


def stop(
    ctx: "BaseContext",
    instance: system.Instance,
    *,
    mode: PostgreSQLStopMode = "fast",
    wait: bool = True,
    deleting: bool = False,
) -> None:
    """Stop an instance."""
    logger.info("stopping instance %s", instance)
    if status(ctx, instance) == Status.not_running:
        logger.warning("instance %s is already stopped", instance)
    else:
        stopped = ctx.hook.stop_service(
            ctx=ctx, service=ctx.hook.postgresql_service_name(), name=instance.qualname
        )
        if not stopped:
            ctx.hook.stop_postgresql(
                ctx=ctx, instance=instance, mode=mode, wait=wait, deleting=deleting
            )

    if wait:
        ctx.hook.instance_stop(ctx=ctx, instance=instance)


@hookimpl(trylast=True)  # type: ignore[misc]
def stop_postgresql(
    ctx: "BaseContext",
    instance: system.PostgreSQLInstance,
    mode: PostgreSQLStopMode,
    wait: bool,
) -> Literal[True]:
    logger.info("stopping PostgreSQL")
    if status(ctx, instance) == Status.not_running:
        logger.warning("instance %s is already stopped", instance)
    else:
        pg_ctl(instance.bindir, ctx=ctx).stop(instance.datadir, mode=mode, wait=wait)
    return True


def restart(
    ctx: "BaseContext",
    instance: system.Instance,
    *,
    mode: PostgreSQLStopMode = "fast",
    wait: bool = True,
) -> None:
    """Restart an instance."""
    logger.info("restarting instance %s", instance)
    ctx.hook.instance_stop(ctx=ctx, instance=instance)
    restarted = ctx.hook.restart_service(
        ctx=ctx, service=ctx.hook.postgresql_service_name(), name=instance.qualname
    )
    if restarted:
        wait_ready(ctx, instance)
    else:
        ctx.hook.restart_postgresql(ctx=ctx, instance=instance, mode=mode, wait=wait)

    ctx.hook.instance_start(ctx=ctx, instance=instance)


@hookimpl(trylast=True)  # type: ignore[misc]
def restart_postgresql(
    ctx: "BaseContext",
    instance: system.PostgreSQLInstance,
    mode: PostgreSQLStopMode,
    wait: bool,
) -> Literal[True]:
    logger.info("restarting PostgreSQL")
    stop_postgresql(ctx, instance, mode=mode, wait=wait)
    start_postgresql(ctx, instance, foreground=False, wait=wait)
    return True


def reload(ctx: "BaseContext", instance: system.PostgreSQLInstance) -> None:
    """Reload an instance."""
    ctx.hook.reload_postgresql(ctx=ctx, instance=instance)


@hookimpl(trylast=True)  # type: ignore[misc]
def reload_postgresql(ctx: "BaseContext", instance: system.Instance) -> Literal[True]:
    logger.info(f"reloading PostgreSQL configuration for {instance.qualname}")
    with db.connect(ctx, instance) as cnx:
        cnx.execute("SELECT pg_reload_conf()")
    return True


def promote(ctx: "BaseContext", instance: system.PostgreSQLInstance) -> None:
    """Promote a standby instance"""
    if not instance.standby:
        raise exceptions.InstanceStateError(f"{instance} is not a standby")
    ctx.hook.promote_postgresql(ctx=ctx, instance=instance)


@hookimpl(trylast=True)  # type: ignore[misc]
def promote_postgresql(ctx: "BaseContext", instance: system.Instance) -> Literal[True]:
    logger.info("promoting PostgreSQL instance")
    pgctl = pg_ctl(instance.bindir, ctx=ctx)
    ctx.run(
        [str(pgctl.pg_ctl), "promote", "-D", str(instance.datadir)],
        check=True,
    )
    return True


@task("upgrading PostgreSQL instance")
def upgrade(
    ctx: "BaseContext",
    instance: system.Instance,
    *,
    version: Optional[str] = None,
    name: Optional[str] = None,
    port: Optional[int] = None,
    jobs: Optional[int] = None,
    _instance_model: Optional[Type[interface.Instance]] = None,
) -> system.Instance:
    """Upgrade a primary instance using pg_upgrade"""
    if instance.standby:
        raise exceptions.InstanceReadOnlyError(instance)
    if version is None:
        version = system.default_postgresql_version(ctx)
    if (name is None or name == instance.name) and version == instance.version:
        raise exceptions.InvalidVersion(
            f"Could not upgrade {instance} using same name and same version"
        )
    # check if target name/version already exists
    if exists(ctx, name=(instance.name if name is None else name), version=version):
        raise exceptions.InstanceAlreadyExists(
            f"Could not upgrade {instance}: target name/version instance already exists"
        )

    if not ctx.confirm(
        f"Confirm upgrade of instance {instance} to version {version}?", True
    ):
        raise exceptions.Cancelled(f"upgrade of instance {instance} cancelled")

    postgresql_settings = ctx.settings.postgresql
    surole = postgresql_settings.surole
    surole_password = postgresql_settings.libpq_environ(ctx, instance, surole.name).get(
        "PGPASSWORD"
    )
    if not surole_password and surole.pgpass:
        passfile = pgpass.parse(ctx.settings.postgresql.auth.passfile)
        for entry in passfile:
            if entry.matches(port=instance.port, username=surole.name):
                surole_password = entry.password
    if _instance_model is None:
        _instance_model = interface.Instance.composite(ctx.pm)
    new_manifest = _instance_model.parse_obj(
        dict(
            _get(ctx, instance),
            name=name or instance.name,
            version=version,
            port=port or instance.port,
            state=interface.InstanceState.stopped,
            surole_password=SecretStr(surole_password) if surole_password else None,
        )
    )
    newinstance = init(ctx, new_manifest)
    configure(ctx, new_manifest, _creating=True, run_hooks=False)
    pg_upgrade = str(newinstance.bindir / "pg_upgrade")
    cmd = [
        pg_upgrade,
        f"--old-bindir={instance.bindir}",
        f"--new-bindir={newinstance.bindir}",
        f"--old-datadir={instance.datadir}",
        f"--new-datadir={newinstance.datadir}",
        f"--username={ctx.settings.postgresql.surole.name}",
    ]
    if jobs is not None:
        cmd.extend(["--jobs", str(jobs)])
    env = postgresql_settings.libpq_environ(
        ctx, instance, ctx.settings.postgresql.surole.name
    )
    if surole_password:
        env.setdefault("PGPASSWORD", surole_password)
    with tempfile.TemporaryDirectory() as tmpdir:
        ctx.run(cmd, check=True, cwd=tmpdir, env=env)
    ctx.hook.instance_upgrade(ctx=ctx, old=instance, new=newinstance)
    apply(ctx, new_manifest, _creating=True)
    return system.Instance.system_lookup(ctx, newinstance)


@upgrade.revert("dropping upgraded instance")
def revert_upgrade(
    ctx: "BaseContext",
    instance: system.Instance,
    *,
    version: Optional[str] = None,
    name: Optional[str] = None,
    port: Optional[int] = None,
    jobs: Optional[int] = None,
    _instance_model: Optional[Type[interface.Instance]] = None,
) -> None:
    newinstance = system.Instance.system_lookup(ctx, (name or instance.name, version))
    drop(ctx, newinstance)


def get_locale(
    ctx: "BaseContext", instance: system.PostgreSQLInstance
) -> Optional[str]:
    """Return the value of instance locale.

    If locale subcategories are set to distinct values, return None.

    The instance must be running.
    """
    locales = {
        s.name: s.setting for s in settings(ctx, instance) if s.name.startswith("lc_")
    }
    values = set(locales.values())
    if len(values) == 1:
        return values.pop()
    else:
        logger.debug(
            "cannot determine instance locale, settings are heterogeneous: %s",
            ", ".join(f"{n}: {s}" for n, s in sorted(locales.items())),
        )
        return None


def get_encoding(ctx: "BaseContext", instance: system.PostgreSQLInstance) -> str:
    """Return the value of instance encoding."""
    with db.connect(ctx, instance) as cnx:
        row = cnx.execute(db.query("instance_encoding")).fetchone()
        assert row is not None
        value = row["pg_encoding_to_char"]
        return str(value)


def get_data_checksums(ctx: "BaseContext", instance: system.PostgreSQLInstance) -> bool:
    """Return True/False if data_checksums is enabled/disabled on instance."""
    if status(ctx, instance) == Status.running:
        # Use SQL SHOW data_checksums since pg_checksums doesn't work if
        # instance is running.
        with db.connect(ctx, instance) as cnx:
            row = cnx.execute("SHOW data_checksums").fetchone()
            assert row is not None
            value = row["data_checksums"]
            assert value in ("on", "off"), value
            return True if value == "on" else False
    if instance.version == PostgreSQLVersion.v11:
        command = str(instance.bindir / "pg_verify_checksums")
        proc = ctx.run([command, "--pgdata", str(instance.datadir)])
    else:
        command = str(instance.bindir / "pg_checksums")
        proc = ctx.run([command, "--check", "--pgdata", str(instance.datadir)])
    if proc.returncode == 0:
        return True
    elif proc.returncode == 1:
        return False
    raise exceptions.CommandError(proc.returncode, proc.args, proc.stdout, proc.stderr)


def set_data_checksums(
    ctx: "BaseContext", instance: system.PostgreSQLInstance, enabled: bool
) -> None:
    """Enable/disable data checksums on instance."""
    if status(ctx, instance) == Status.running:
        raise exceptions.InstanceStateError(
            "could not alter data_checksums on a running instance"
        )
    action = "enable" if enabled else "disable"
    if instance.version < PostgreSQLVersion.v12:
        raise exceptions.UnsupportedError(
            "PostgreSQL <= 11 doesn't have pg_checksums to enable data checksums"
        )
    ctx.run(
        [
            str(instance.bindir / "pg_checksums"),
            f"--{action}",
            "--pgdata",
            str(instance.datadir),
        ],
        check=True,
    )


def apply(
    ctx: "BaseContext", instance: interface.Instance, *, _creating: bool = False
) -> interface.InstanceApplyResult:
    """Apply state described by interface model as a PostgreSQL instance.

    Depending on the previous state and existence of the target instance, the
    instance may be created or updated or dropped.

    If configuration changes are detected and the instance was previously
    running, the server will be reloaded automatically; if a restart is
    needed, the user will be prompted in case of interactive usage or this
    will be performed automatically if 'restart_on_changes' is set to True.
    """
    States = interface.InstanceState
    state = instance.state
    if state == States.absent:
        dropped = False
        if exists(ctx, instance.name, instance.version):
            drop(
                ctx,
                system.Instance.system_lookup(ctx, (instance.name, instance.version)),
            )
            dropped = True
        return interface.InstanceApplyResult(
            change_state=interface.ApplyChangeState.dropped if dropped else None,
        )

    changed = False
    try:
        sys_instance = system.PostgreSQLInstance.system_lookup(
            ctx, (instance.name, instance.version)
        )
    except exceptions.InstanceNotFound:
        _creating = True
        interface.validate_ports(instance)
        sys_instance = init(ctx, instance)
        changed = True

    with configure_context(ctx, instance, _creating=_creating) as changes:
        if _creating:
            # Now that PostgreSQL configuration is done, call hooks for
            # super-user role creation (handled by initdb), e.g. to create the
            # .pgpass entry.
            surole = instance.surole(ctx.settings)
            ctx.hook.role_change(ctx=ctx, role=surole, instance=instance)
            if not sys_instance.standby:  # standby instances are read-only
                with postgresql_running(ctx, sys_instance):
                    replrole = instance.replrole(ctx.settings)
                    roles.apply(ctx, sys_instance, replrole)
                    for role in ctx.hook.role(settings=ctx.settings, manifest=instance):
                        roles.apply(ctx, sys_instance, role)
                    for database in ctx.hook.database(
                        settings=ctx.settings, manifest=instance
                    ):
                        databases.apply(ctx, sys_instance, database)
    changed = changed or bool(changes)

    instance_is_running = is_running(ctx, sys_instance)
    sys_instance = system.Instance.system_lookup(ctx, sys_instance)

    if instance.data_checksums is not None:
        actual_data_checksums = get_data_checksums(ctx, sys_instance)
        if actual_data_checksums != instance.data_checksums:
            if instance.data_checksums:
                logger.info("enabling data checksums")
            else:
                logger.info("disabling data checksums")
            set_data_checksums(ctx, sys_instance, instance.data_checksums)
            changed = True

    if state == States.stopped:
        if instance_is_running:
            stop(ctx, sys_instance)
            changed = True
    elif state in (States.started, States.restarted):
        if not instance_is_running:
            start(ctx, sys_instance)
            changed = True
        elif state == States.restarted:
            restart(ctx, sys_instance)
            changed = True
    else:
        assert False, f"unexpected state: {state}"  # pragma: nocover

    StandbyState = Standby.State
    standby = instance._standby()

    if (
        standby
        and standby.status == StandbyState.promoted
        and sys_instance.standby is not None
    ):
        promote(ctx, sys_instance)

    if not sys_instance.standby:
        logger.info("updating PostgreSQL extensions installation if needed")
        with postgresql_running(ctx, sys_instance):
            db.create_or_drop_extensions(ctx, sys_instance, instance.extensions)
            for a_role in instance.roles:
                changed = (
                    roles.apply(ctx, sys_instance, a_role).change_state
                    in (
                        interface.ApplyChangeState.created,
                        interface.ApplyChangeState.changed,
                    )
                    or changed
                )
            for a_database in instance.databases:
                changed = (
                    databases.apply(ctx, sys_instance, a_database).change_state
                    in (
                        interface.ApplyChangeState.changed,
                        interface.ApplyChangeState.created,
                    )
                    or changed
                )
    change_state, p_restart = None, False
    if _creating:
        change_state = interface.ApplyChangeState.created
    elif changed:
        change_state = interface.ApplyChangeState.changed
        p_restart = pending_restart(ctx, sys_instance)
    return interface.InstanceApplyResult(
        change_state=change_state, pending_restart=p_restart
    )


def pending_restart(ctx: "BaseContext", instance: system.PostgreSQLInstance) -> bool:
    """Return True if the instance is pending a restart to account for configuration changes."""
    if not is_running(ctx, instance):
        return False
    with db.connect(ctx, instance) as cnx, cnx.cursor(
        row_factory=psycopg.rows.args_row(bool)
    ) as cur:
        cur.execute("SELECT bool_or(pending_restart) FROM pg_settings")
        row = cur.fetchone()
        assert row is not None
        return row


def check_pending_actions(
    ctx: "BaseContext",
    instance: system.Instance,
    changes: ConfigChanges,
    restart_on_changes: bool,
) -> None:
    """Check if any of the changes require a reload or a restart.

    The instance is automatically reloaded if needed.
    The user is prompted for confirmation if a restart is needed.
    """
    if not is_running(ctx, instance):
        return

    if "port" in changes:
        needs_restart = True
    else:
        needs_restart = False
        pending_restart = set()
        pending_reload = set()
        for p in settings(ctx, instance):
            pname = p.name
            if pname not in changes:
                continue
            if p.context == "postmaster":
                pending_restart.add(pname)
            else:
                pending_reload.add(pname)

        if pending_reload:
            logger.info(
                "instance %s needs reload due to parameter changes: %s",
                instance,
                ", ".join(sorted(pending_reload)),
            )
            reload(ctx, instance)

        if pending_restart:
            logger.warning(
                "instance %s needs restart due to parameter changes: %s",
                instance,
                ", ".join(sorted(pending_restart)),
            )
            needs_restart = True

    if needs_restart and ctx.confirm(
        "Instance needs to be restarted; restart now?", restart_on_changes
    ):
        restart(ctx, instance)


def get(ctx: "BaseContext", name: str, version: Optional[str]) -> interface.Instance:
    """Return the instance object with specified name and version."""
    instance = system.Instance.system_lookup(ctx, (name, version))
    if not is_running(ctx, instance):
        missing_bits = [
            "locale",
            "encoding",
            "passwords",
            "extensions",
            "pending_restart",
        ]
        if instance.standby is not None:
            missing_bits.append("replication lag")
        logger.warning(
            "instance %s is not running, information about %s may not be accurate",
            instance,
            f"{', '.join(missing_bits[:-1])} and {missing_bits[-1]}",
        )
    return _get(ctx, instance)


def _get(ctx: "BaseContext", instance: system.Instance) -> interface.Instance:
    config = instance.config()
    managed_config = config.as_dict()
    managed_config.pop("port", None)
    st = status(ctx, instance)
    state = interface.InstanceState.from_pg_status(st)
    instance_is_running = st == Status.running
    services = {
        s.__class__.__service__: s
        for s in ctx.hook.get(ctx=ctx, instance=instance)
        if s is not None
    }
    if instance.standby:
        kw: Dict[str, Any] = {
            "for": instance.standby.for_,
            "slot": instance.standby.slot,
            "password": instance.standby.password,
        }
        if instance_is_running:
            kw["replication_lag"] = replication_lag(ctx, instance)
        try:
            standby_model = ctx.hook.standby_model()
        except ValueError:
            pass
        else:
            services["standby"] = standby_model(**kw)

    extensions: List[interface.Extension] = []
    if "shared_preload_libraries" in config:
        extensions += [
            interface.Extension(spl.strip())
            for spl in str(config["shared_preload_libraries"]).split(",")
            if spl.strip()
        ]

    locale = None
    encoding = None
    pending_rst = False
    if instance_is_running:
        locale = get_locale(ctx, instance)
        encoding = get_encoding(ctx, instance)
        extensions += [
            e for e in db.installed_extensions(ctx, instance) if e not in extensions
        ]
        pending_rst = pending_restart(ctx, instance)

    try:
        data_checksums = get_data_checksums(ctx, instance)
    except exceptions.UnsupportedError as e:
        logger.warning(str(e))
        data_checksums = None

    return interface.Instance(
        name=instance.name,
        version=instance.version,
        port=instance.port,
        state=state,
        pending_restart=pending_rst,
        configuration=managed_config,
        locale=locale,
        encoding=encoding,
        data_checksums=data_checksums,
        extensions=extensions,
        **services,
    )


@task("dropping PostgreSQL instance")
def drop(ctx: "BaseContext", instance: system.Instance) -> None:
    """Drop an instance."""
    if not ctx.confirm(f"Confirm complete deletion of instance {instance}?", True):
        raise exceptions.Cancelled(f"deletion of instance {instance} cancelled")

    stop(ctx, instance, mode="immediate", deleting=True)

    ctx.hook.instance_drop(ctx=ctx, instance=instance)
    for rolename in ctx.hook.rolename(settings=ctx.settings):
        ctx.hook.role_change(
            ctx=ctx,
            role=interface.Role(name=rolename, state=interface.PresenceState.absent),
            instance=instance,
        )
    manifest = interface.Instance(name=instance.name, version=instance.version)
    revert_init(ctx, manifest)


def list(
    ctx: "BaseContext", *, version: Optional[PostgreSQLVersion] = None
) -> Iterator[interface.InstanceListItem]:
    """Yield instances found by system lookup.

    :param version: filter instances matching a given version.

    :raises ~exceptions.InvalidVersion: if specified version is unknown.
    """
    for instance in system_list(ctx, version=version):
        yield interface.InstanceListItem(
            name=instance.name,
            datadir=instance.datadir,
            port=instance.port,
            status=status(ctx, instance).name,
            version=instance.version,
        )


def system_list(
    ctx: "BaseContext", *, version: Optional[PostgreSQLVersion] = None
) -> Iterator[system.PostgreSQLInstance]:
    if version is not None:
        assert isinstance(version, PostgreSQLVersion)
        versions = [version.value]
    else:
        versions = sorted(ctx.settings.postgresql.versions)

    # Search for directories matching datadir template globing on the {name}
    # part. Since the {version} part may come after or before {name}, we first
    # build a datadir for each known version and split it on {name} for
    # further globbing.
    name_idx = ctx.settings.postgresql.datadir.parts.index("{name}")
    for ver in versions:
        version_path = Path(
            str(ctx.settings.postgresql.datadir).format(name="*", version=ver)
        )
        prefix = Path(*version_path.parts[:name_idx])
        suffix = Path(*version_path.parts[name_idx + 1 :])
        pattern = f"*/{suffix}"
        for d in sorted(prefix.glob(pattern)):
            if not d.is_dir():
                continue
            name = d.relative_to(prefix).parts[0]
            try:
                yield system.PostgreSQLInstance.system_lookup(ctx, (name, ver))
            except exceptions.InstanceNotFound:
                pass


def env_for(
    ctx: "BaseContext", instance: system.PostgreSQLInstance, *, path: bool = False
) -> Dict[str, str]:
    """Return libpq environment variables suitable to connect to `instance`.

    If 'path' is True, also inject PostgreSQL binaries directory in PATH.
    """
    postgresql_settings = ctx.settings.postgresql
    env = postgresql_settings.libpq_environ(
        ctx, instance, postgresql_settings.surole.name, base={}
    )
    config = instance.config()
    try:
        host = config.unix_socket_directories.split(",")[0]  # type: ignore[union-attr]
    except (AttributeError, IndexError):
        host = "localhost"
    env.update(
        {
            "PGUSER": ctx.settings.postgresql.surole.name,
            "PGPORT": str(instance.port),
            "PGHOST": host,
            "PGDATA": str(instance.datadir),
            "PSQLRC": str(instance.psqlrc),
            "PSQL_HISTORY": str(instance.psql_history),
        }
    )
    if path:
        env["PATH"] = ":".join(
            [str(instance.bindir)]
            + ([os.environ["PATH"]] if "PATH" in os.environ else [])
        )
    for env_vars in ctx.hook.instance_env(ctx=ctx, instance=instance):
        env.update(env_vars)
    return env


def exec(
    ctx: "BaseContext", instance: system.PostgreSQLInstance, command: Tuple[str, ...]
) -> None:
    """Execute given PostgreSQL command in the libpq environment for `instance`.

    The command to be executed is looked up for in PostgreSQL binaries directory.
    """
    env = os.environ.copy()
    env.update(env_for(ctx, instance))
    progname, *args = command
    program = instance.bindir / progname
    try:
        cmd.execute_program([str(program)] + args, env=env, logger=logger)
    except FileNotFoundError as e:
        raise exceptions.FileNotFoundError(str(e))


def env(ctx: "BaseContext", instance: system.PostgreSQLInstance) -> str:
    return "\n".join(
        [
            f"export {key}={value}"
            for key, value in sorted(env_for(ctx, instance, path=True).items())
        ]
    )


def exists(ctx: "BaseContext", name: str, version: Optional[str]) -> bool:
    """Return true when instance exists"""
    try:
        system.PostgreSQLInstance.system_lookup(ctx, (name, version))
    except exceptions.InstanceNotFound:
        return False
    return True


def settings(
    ctx: "BaseContext", instance: system.PostgreSQLInstance
) -> List[interface.PGSetting]:
    """Return the list of run-time parameters of the server, as available in
    pg_settings view.

    The instance must be running.
    """
    with db.connect(ctx, instance, dbname="template1") as cnx, cnx.cursor(
        row_factory=psycopg.rows.class_row(interface.PGSetting)
    ) as cur:
        cur.execute(interface.PGSetting._query)
        return cur.fetchall()


def logs(ctx: "BaseContext", instance: system.PostgreSQLInstance) -> Iterator[str]:
    """Return the content of current log file as an iterator.

    :raises ~exceptions.FileNotFoundError: if the current log file, matching
        configured log_destination, is not found.
    :raises ~exceptions.SystemError: if the current log file cannot be opened
        for reading.
    :raises ValueError: if no record matching configured log_destination is
        found in current_logfiles (this indicates a misconfigured instance).
    """
    config = instance.config()
    log_destination = config.get("log_destination", "stderr")
    current_logfiles = instance.datadir / "current_logfiles"
    if not current_logfiles.exists():
        raise exceptions.FileNotFoundError(
            f"file 'current_logfiles' for instance {instance} not found"
        )
    with current_logfiles.open() as f:
        for line in f:
            destination, logfilelocation = line.strip().split(None, maxsplit=1)
            if destination == log_destination:
                break
        else:
            raise ValueError(
                f"no record matching '{log_destination}' log destination found for instance {instance}"
            )

    logfile = Path(logfilelocation)
    if not logfile.is_absolute():
        logfile = instance.datadir / logfile

    logger.info("reading logs of instance '%s' from %s", instance, logfile)
    try:
        with logfile.open() as f:
            yield from f
    except OSError:
        raise exceptions.SystemError(f"failed to read {logfile} on instance {instance}")


def replication_lag(
    ctx: "BaseContext", instance: system.PostgreSQLInstance
) -> Optional[Decimal]:
    """Return the replication lag of a standby instance.

    The instance must be running; if the primary is not running, None is
    returned.

    :raises TypeError: if the instance is not a standby.
    """
    standby = instance.standby
    if standby is None:
        raise TypeError(f"{instance} is not a standby")

    try:
        with db.primary_connect(standby) as cnx:
            row = cnx.execute("SELECT pg_current_wal_lsn() AS lsn").fetchone()
    except psycopg.OperationalError as e:
        logger.warning("failed to connect to primary (is it running?): %s", e)
        return None
    assert row is not None
    primary_lsn = row["lsn"]

    password = standby.password.get_secret_value() if standby.password else None
    dsn = db.dsn(
        instance,
        ctx.settings.postgresql,
        dbname="template1",
        user=ctx.settings.postgresql.replrole,
        password=password,
    )
    with db.connect_dsn(dsn) as cnx:
        row = cnx.execute(
            "SELECT %s::pg_lsn - pg_last_wal_replay_lsn() AS lag", (primary_lsn,)
        ).fetchone()
    assert row is not None
    lag = row["lag"]
    assert isinstance(lag, Decimal)
    return lag
