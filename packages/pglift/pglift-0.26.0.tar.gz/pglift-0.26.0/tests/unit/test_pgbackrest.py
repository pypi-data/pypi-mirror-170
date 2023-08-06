from datetime import datetime, timezone
from unittest.mock import patch

import pytest
from pgtoolkit.conf import Configuration

from pglift import exceptions, types
from pglift.ctx import Context
from pglift.models import interface
from pglift.models.system import Instance
from pglift.pgbackrest import impl as pgbackrest
from pglift.pgbackrest import instance_configure
from pglift.settings import PgBackRestSettings, Settings


@pytest.fixture
def pgbackrest_settings(settings: Settings) -> PgBackRestSettings:
    assert settings.pgbackrest is not None
    return settings.pgbackrest


def test_make_cmd(settings: Settings, pgbackrest_settings: PgBackRestSettings) -> None:
    assert pgbackrest.make_cmd("42-test", pgbackrest_settings, "stanza-upgrade") == [
        "/usr/bin/pgbackrest",
        "--config-path=/etc/pgbckrst",
        "--stanza=42-test",
        "stanza-upgrade",
    ]


def test_backup_info(
    ctx: Context,
    settings: Settings,
    pgbackrest_settings: PgBackRestSettings,
) -> None:
    with patch.object(ctx, "run") as run:
        run.return_value.stdout = "[]"
        assert (
            pgbackrest.backup_info(
                ctx, "testback", pgbackrest_settings, backup_set="foo"
            )
            == []
        )
    run.assert_called_once_with(
        [
            "/usr/bin/pgbackrest",
            "--config-path=/etc/pgbckrst",
            "--stanza=testback",
            "--set=foo",
            "--output=json",
            "info",
        ],
        check=True,
    )


def test_backup_command(
    settings: Settings, pgbackrest_settings: PgBackRestSettings
) -> None:
    assert pgbackrest.backup_command(
        "backtesr", pgbackrest_settings, type=types.BackupType.full
    ) == [
        "/usr/bin/pgbackrest",
        "--config-path=/etc/pgbckrst",
        "--stanza=backtesr",
        "--type=full",
        "--log-level-console=info",
        "--start-fast",
        "backup",
    ]


def test_expire_command(
    settings: Settings, pgbackrest_settings: PgBackRestSettings
) -> None:
    assert pgbackrest.expire_command("expire", pgbackrest_settings) == [
        "/usr/bin/pgbackrest",
        "--config-path=/etc/pgbckrst",
        "--stanza=expire",
        "--log-level-console=info",
        "expire",
    ]


def test_restore_command(
    settings: Settings, pgbackrest_settings: PgBackRestSettings
) -> None:
    with pytest.raises(exceptions.UnsupportedError):
        pgbackrest.restore_command(
            "rest", pgbackrest_settings, date=datetime.now(), backup_set="sunset"
        )

    assert pgbackrest.restore_command("rest", pgbackrest_settings) == [
        "/usr/bin/pgbackrest",
        "--config-path=/etc/pgbckrst",
        "--stanza=rest",
        "--log-level-console=info",
        "--delta",
        "--link-all",
        "restore",
    ]

    assert pgbackrest.restore_command(
        "backtest",
        pgbackrest_settings,
        date=datetime(2003, 1, 1).replace(tzinfo=timezone.utc),
    ) == [
        "/usr/bin/pgbackrest",
        "--config-path=/etc/pgbckrst",
        "--stanza=backtest",
        "--log-level-console=info",
        "--delta",
        "--link-all",
        "--target-action=promote",
        "--type=time",
        "--target=2003-01-01 00:00:00.000000+0000",
        "restore",
    ]

    assert pgbackrest.restore_command(
        "backtest",
        pgbackrest_settings,
        backup_set="x",
    ) == [
        "/usr/bin/pgbackrest",
        "--config-path=/etc/pgbckrst",
        "--stanza=backtest",
        "--log-level-console=info",
        "--delta",
        "--link-all",
        "--target-action=promote",
        "--type=immediate",
        "--set=x",
        "restore",
    ]


def test_standby_backup(
    ctx: Context, pgbackrest_settings: PgBackRestSettings, standby_instance: Instance
) -> None:
    with pytest.raises(
        exceptions.InstanceStateError,
        match="^backup should be done on primary instance",
    ):
        pgbackrest.backup(ctx, standby_instance, pgbackrest_settings)


def test_standby_restore(
    ctx: Context, pgbackrest_settings: PgBackRestSettings, standby_instance: Instance
) -> None:
    with pytest.raises(
        exceptions.InstanceReadOnlyError,
        match=f"^{standby_instance.version}/standby is a read-only standby",
    ):
        pgbackrest.restore(ctx, standby_instance, pgbackrest_settings)


def test_instance_configure_cancelled_if_repo_exists(
    ctx: Context, instance: Instance, instance_manifest: interface.Instance
) -> None:
    settings = ctx.settings.pgbackrest
    assert settings is not None
    with patch.object(pgbackrest, "enabled", return_value=True) as enabled:
        with pytest.raises(exceptions.Cancelled):
            instance_configure(
                ctx=ctx,
                manifest=instance_manifest,
                config=Configuration(),
                creating=True,
            )
    enabled.assert_called_once_with(instance.qualname, settings)


def test_env_for(
    instance: Instance,
    settings: Settings,
    pgbackrest_settings: PgBackRestSettings,
) -> None:
    assert pgbackrest.env_for(instance, pgbackrest_settings) == {
        "PGBACKREST_CONFIG_PATH": "/etc/pgbckrst",
        "PGBACKREST_STANZA": f"{instance.version}-{instance.name}",
    }
