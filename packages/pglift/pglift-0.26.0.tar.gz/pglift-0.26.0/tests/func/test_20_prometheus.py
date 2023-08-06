import logging
from pathlib import Path
from typing import Dict, Iterator, Optional, Tuple

import pytest
import requests
from tenacity import retry
from tenacity.stop import stop_after_attempt
from tenacity.wait import wait_fixed

from pglift import exceptions, instances, systemd
from pglift.ctx import Context
from pglift.models import interface, system
from pglift.prometheus import impl as prometheus
from pglift.prometheus import models
from pglift.prometheus.models import Service
from pglift.settings import PrometheusSettings
from pglift.systemd import service_manager

from . import reconfigure_instance
from .conftest import DatabaseFactory, Factory, RoleFactory


@pytest.fixture(scope="session", autouse=True)
def _prometheus_available(prometheus_execpath: Optional[Path]) -> None:
    if not prometheus_execpath:
        pytest.skip("prometheus is not available")


def config_dict(configpath: Path) -> Dict[str, str]:
    config = {}
    for line in configpath.read_text().splitlines():
        key, value = line.split("=", 1)
        config[key] = value.strip()
    return config


def test_configure(
    ctx: Context,
    prometheus_settings: PrometheusSettings,
    prometheus_password: str,
    instance: system.Instance,
    instance_manifest: interface.Instance,
    tmp_port_factory: Iterator[int],
) -> None:
    service = instance.service(models.Service)
    assert (
        service.password and service.password.get_secret_value() == prometheus_password
    )
    name = instance.qualname
    configpath = Path(str(prometheus_settings.configpath).format(name=name))
    assert configpath.exists()

    prometheus_config = config_dict(configpath)
    dsn = prometheus_config["DATA_SOURCE_NAME"]
    assert "postgresql://prometheus" in dsn
    assert f":{instance.port}" in dsn
    port = service.port
    assert prometheus_config["PG_EXPORTER_WEB_LISTEN_ADDRESS"] == f":{port}"

    queriespath = Path(str(prometheus_settings.queriespath).format(name=name))
    assert queriespath.exists()

    new_port = next(tmp_port_factory)
    with reconfigure_instance(ctx, instance_manifest, port=new_port):
        new_prometheus_config = config_dict(configpath)
        dsn = new_prometheus_config["DATA_SOURCE_NAME"]
        assert f":{new_port}" in dsn


@pytest.fixture
def postgres_exporter(
    ctx: Context,
    prometheus_settings: PrometheusSettings,
    prometheus_password: str,
    instance_manifest: interface.Instance,
    instance: system.Instance,
    tmp_port_factory: Iterator[int],
    role_factory: RoleFactory,
) -> Iterator[Service]:
    """Setup a postgres_exporter service for 'instance' using another port."""
    port = next(tmp_port_factory)
    name = "123-fo-o"
    role = interface.Role(name="prometheus_tests", password=prometheus_password)
    unix_socket_directories = instance.config()["unix_socket_directories"]
    assert isinstance(unix_socket_directories, str), unix_socket_directories
    host = unix_socket_directories.split(",", 1)[0]
    dsn = f"host={host} dbname=postgres port={instance.port} user={role.name} sslmode=disable"
    service = prometheus.setup(
        ctx, name, prometheus_settings, dsn=dsn, password=prometheus_password, port=port
    )
    configpath = Path(str(prometheus_settings.configpath).format(name=name))
    assert configpath.exists()
    queriespath = Path(str(prometheus_settings.queriespath).format(name=name))
    assert queriespath.exists()

    role_factory(
        role.name, f"LOGIN PASSWORD '{prometheus_password}' IN ROLE pg_monitor"
    )

    yield service

    prometheus.revert_setup(ctx, name, prometheus_settings)
    assert not configpath.exists()
    assert not queriespath.exists()


def test_setup(
    prometheus_settings: PrometheusSettings,
    instance: system.Instance,
    postgres_exporter: Service,
) -> None:
    configpath = Path(
        str(prometheus_settings.configpath).format(name=postgres_exporter.name)
    )
    prometheus_config = config_dict(configpath)
    assert f":{instance.port}" in prometheus_config["DATA_SOURCE_NAME"]
    assert (
        prometheus_config["PG_EXPORTER_WEB_LISTEN_ADDRESS"]
        == f":{postgres_exporter.port}"
    )


@retry(reraise=True, wait=wait_fixed(2), stop=stop_after_attempt(5))
def request_metrics(port: int) -> requests.Response:
    return requests.get(f"http://0.0.0.0:{port}/metrics")


@pytest.mark.usefixtures("prometheus_settings")
def test_start_stop(
    ctx: Context, instance: system.Instance, database_factory: DatabaseFactory
) -> None:
    service = instance.service(models.Service)
    port = service.port

    if ctx.settings.service_manager == "systemd":
        assert systemd.is_enabled(
            ctx, service_manager.unit("postgres_exporter", instance.qualname)
        )

    database_factory("newdb")

    with instances.running(ctx, instance):
        if ctx.settings.service_manager == "systemd":
            assert systemd.is_active(
                ctx, service_manager.unit("postgres_exporter", instance.qualname)
            )
        try:
            r = request_metrics(port)
        except requests.ConnectionError as e:
            raise AssertionError(f"HTTP connection failed: {e}") from None
        r.raise_for_status()
        assert r.ok
        output = r.text
        assert "pg_up 1" in output.splitlines()

    with instances.stopped(ctx, instance):
        if ctx.settings.service_manager == "systemd":
            assert not systemd.is_active(
                ctx, service_manager.unit("postgres_exporter", instance.qualname)
            )
        with pytest.raises(requests.ConnectionError):
            request_metrics(port)


def test_standby(
    standby_ctx: Context,
    prometheus_password: str,
    standby_prometheus_settings: PrometheusSettings,
    standby_instance: system.Instance,
) -> None:
    name = standby_instance.qualname
    service = standby_instance.service(models.Service)
    port = service.port
    assert (
        service.password and service.password.get_secret_value() == prometheus_password
    )
    configpath = Path(str(standby_prometheus_settings.configpath).format(name=name))
    assert configpath.exists()
    with instances.running(standby_ctx, standby_instance):
        if standby_ctx.settings.service_manager == "systemd":
            assert systemd.is_active(
                standby_ctx, service_manager.unit("postgres_exporter", name)
            )
        assert (
            instances.status(standby_ctx, standby_instance) == instances.Status.running
        )
        try:
            r = request_metrics(port)
        except requests.ConnectionError as e:
            raise AssertionError(f"HTTP connection failed: {e}") from None
        r.raise_for_status()
        assert r.ok
        output = r.text
        assert "pg_up 1" in output.splitlines()


@pytest.mark.xfail
def test_upgrade(
    prometheus_settings: PrometheusSettings, upgraded_instance: system.Instance
) -> None:
    service = upgraded_instance.service(models.Service)
    assert service.password
    name = upgraded_instance.qualname
    configpath = Path(str(prometheus_settings.configpath).format(name=name))
    assert configpath.exists()
    # TODO: complement similarly to test_configure()


def test_start_stop_nonlocal(
    ctx: Context,
    instance: system.Instance,
    prometheus_settings: PrometheusSettings,
    postgres_exporter: Service,
) -> None:
    if ctx.settings.service_manager == "systemd":
        assert systemd.is_enabled(
            ctx, service_manager.unit("postgres_exporter", postgres_exporter.name)
        )

    with instances.postgresql_running(ctx, instance):
        prometheus.start(ctx, postgres_exporter)
        try:
            if ctx.settings.service_manager == "systemd":
                assert systemd.is_active(
                    ctx,
                    service_manager.unit("postgres_exporter", postgres_exporter.name),
                )
            try:
                r = request_metrics(postgres_exporter.port)
            except requests.ConnectionError as e:
                raise AssertionError(f"HTTP connection failed: {e}") from None
            r.raise_for_status()
            assert r.ok
            output = r.text
            assert "pg_up 1" in output.splitlines()
        finally:
            prometheus.stop(ctx, postgres_exporter)

        if ctx.settings.service_manager == "systemd":
            assert not systemd.is_active(
                ctx, service_manager.unit("postgres_exporter", postgres_exporter.name)
            )
        with pytest.raises(requests.ConnectionError):
            request_metrics(postgres_exporter.port)


def test_apply(
    ctx: Context,
    prometheus_settings: PrometheusSettings,
    tmp_port_factory: Iterator[int],
) -> None:
    port = next(tmp_port_factory)
    m = models.PostgresExporter(name="test", dsn="dbname=test", port=port)
    prometheus.apply(ctx, m, prometheus_settings)

    configpath = Path(str(prometheus_settings.configpath).format(name="test"))
    assert configpath.exists()
    queriespath = Path(str(prometheus_settings.queriespath).format(name="test"))
    assert queriespath.exists()

    prometheus_config = config_dict(configpath)
    assert prometheus_config["PG_EXPORTER_WEB_LISTEN_ADDRESS"] == f":{port}"

    port1 = next(tmp_port_factory)
    prometheus.apply(ctx, m.copy(update={"port": port1}), prometheus_settings)
    prometheus_config = config_dict(configpath)
    assert prometheus_config["PG_EXPORTER_WEB_LISTEN_ADDRESS"] == f":{port1}"

    prometheus.apply(
        ctx,
        models.PostgresExporter(name="test", dsn="", port=port, state="absent"),
        prometheus_settings,
    )
    assert not configpath.exists()
    assert not queriespath.exists()


def test_drop_exists(
    ctx: Context,
    prometheus_settings: PrometheusSettings,
    tmp_port_factory: Iterator[int],
    caplog: pytest.LogCaptureFixture,
) -> None:
    port = next(tmp_port_factory)
    prometheus.setup(ctx, "dropme", prometheus_settings, port=port)
    assert prometheus.port("dropme", prometheus_settings) == port
    assert prometheus.exists(ctx, "dropme")
    prometheus.drop(ctx, "dropme")
    assert not prometheus.exists(ctx, "dropme")
    with pytest.raises(exceptions.FileNotFoundError, match="postgres_exporter config"):
        prometheus.port("dropme", prometheus_settings)
    caplog.clear()
    with caplog.at_level(logging.WARNING, logger="pglift"):
        prometheus.drop(ctx, "dropme")
    assert caplog.records[0].message == "no postgres_exporter service 'dropme' found"


def test_instance_no_prometheus(
    ctx: Context,
    prometheus_settings: PrometheusSettings,
    instance_factory: Factory[Tuple[interface.Instance, system.Instance]],
) -> None:
    """Make sure we can create an instance without postgres_exporter and have
    it running and restarted.
    """
    _, instance_no_prometheus = instance_factory(
        "noprom", state="started", prometheus=None
    )
    assert not prometheus.enabled(instance_no_prometheus.name, prometheus_settings)
    assert instances.status(ctx, instance_no_prometheus) == instances.Status.running
    instances.restart(ctx, instance_no_prometheus)
    assert instances.status(ctx, instance_no_prometheus) == instances.Status.running
