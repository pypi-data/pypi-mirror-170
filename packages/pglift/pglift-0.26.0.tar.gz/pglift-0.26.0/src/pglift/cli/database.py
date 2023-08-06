import functools
from typing import IO, Any, Optional, Sequence

import click
import psycopg
from pydantic.utils import deep_update
from rich.console import Console

from .. import databases, instances, privileges
from ..ctx import Context
from ..models import helpers, interface, system
from .util import (
    Group,
    as_json_option,
    instance_identifier_option,
    pass_console,
    pass_ctx,
    pass_instance,
    print_json_for,
    print_schema,
    print_table_for,
)


@click.group("database", cls=Group)
@instance_identifier_option
@click.option(
    "--schema",
    is_flag=True,
    callback=functools.partial(print_schema, model=interface.Database),
    expose_value=False,
    is_eager=True,
    help="Print the JSON schema of database model and exit.",
)
def cli(instance: system.Instance) -> None:
    """Manage databases."""


@cli.command("create")
@helpers.parameters_from_model(interface.Database, "create")
@pass_instance
@pass_ctx
def database_create(
    ctx: Context, instance: system.Instance, database: interface.Database
) -> None:
    """Create a database in a PostgreSQL instance"""
    with instances.postgresql_running(ctx, instance):
        if databases.exists(ctx, instance, database.name):
            raise click.ClickException("database already exists")
        databases.apply(ctx, instance, database)


@cli.command("alter")
@helpers.parameters_from_model(interface.Database, "update", parse_model=False)
@click.argument("dbname")
@pass_instance
@pass_ctx
def database_alter(
    ctx: Context, instance: system.Instance, dbname: str, **changes: Any
) -> None:
    """Alter a database in a PostgreSQL instance"""
    changes = helpers.unnest(interface.Database, changes)
    with instances.postgresql_running(ctx, instance):
        values = databases.get(ctx, instance, dbname).dict()
        values = deep_update(values, changes)
        altered = interface.Database.parse_obj(values)
        databases.apply(ctx, instance, altered)


@cli.command("apply", hidden=True)
@click.option("-f", "--file", type=click.File("r"), metavar="MANIFEST", required=True)
@pass_instance
@pass_ctx
def database_apply(ctx: Context, instance: system.Instance, file: IO[str]) -> None:
    """Apply manifest as a database"""
    database = interface.Database.parse_yaml(file)
    with instances.postgresql_running(ctx, instance):
        databases.apply(ctx, instance, database)


@cli.command("get")
@as_json_option
@click.argument("name")
@pass_instance
@pass_console
@pass_ctx
def database_get(
    ctx: Context, console: Console, instance: system.Instance, name: str, as_json: bool
) -> None:
    """Get the description of a database"""
    with instances.postgresql_running(ctx, instance):
        m = databases.get(ctx, instance, name).dict(by_alias=True)
        del m["state"]
    if as_json:
        print_json_for(m, display=console.print_json)
    else:
        print_table_for([m], display=console.print, box=None)


@cli.command("list")
@as_json_option
@click.argument("dbname", nargs=-1)
@pass_instance
@pass_console
@pass_ctx
def database_list(
    ctx: Context,
    console: Console,
    instance: system.Instance,
    dbname: Sequence[str],
    as_json: bool,
) -> None:
    """List databases (all or specified ones)

    Only queried databases are shown when DBNAME is specified.
    """

    with instances.postgresql_running(ctx, instance):
        dbs = databases.list(ctx, instance, dbnames=dbname)
    if as_json:
        print_json_for((i.dict(by_alias=True) for i in dbs), display=console.print_json)
    else:
        print_table_for((i.dict(by_alias=True) for i in dbs), display=console.print)


@cli.command("drop")
@click.argument("name")
@pass_instance
@pass_ctx
def database_drop(ctx: Context, instance: system.Instance, name: str) -> None:
    """Drop a database"""
    with instances.postgresql_running(ctx, instance):
        databases.drop(ctx, instance, name)


@cli.command("privileges")
@click.argument("name")
@click.option("-r", "--role", "roles", multiple=True, help="Role to inspect")
@click.option("--default", "defaults", is_flag=True, help="Display default privileges")
@as_json_option
@pass_instance
@pass_ctx
def database_privileges(
    ctx: Context,
    instance: system.Instance,
    name: str,
    roles: Sequence[str],
    defaults: bool,
    as_json: bool,
) -> None:
    """List privileges on a database."""
    with instances.postgresql_running(ctx, instance):
        databases.get(ctx, instance, name)  # check existence
        try:
            prvlgs = privileges.get(
                ctx, instance, databases=(name,), roles=roles, defaults=defaults
            )
        except ValueError as e:
            raise click.ClickException(str(e))
    if as_json:
        print_json_for((i.dict(by_alias=True) for i in prvlgs))
    else:
        print_table_for((i.dict(by_alias=True) for i in prvlgs))


@cli.command("run")
@click.argument("sql_command")
@click.option(
    "-d", "--database", "dbnames", multiple=True, help="Database to run command on"
)
@click.option(
    "-x",
    "--exclude-database",
    "exclude_dbnames",
    multiple=True,
    help="Database to not run command on",
)
@as_json_option
@pass_instance
@pass_ctx
def database_run(
    ctx: Context,
    instance: system.Instance,
    sql_command: str,
    dbnames: Sequence[str],
    exclude_dbnames: Sequence[str],
    as_json: bool,
) -> None:
    """Run given command on databases of a PostgreSQL instance"""
    with instances.postgresql_running(ctx, instance):
        try:
            result = databases.run(
                ctx,
                instance,
                sql_command,
                dbnames=dbnames,
                exclude_dbnames=exclude_dbnames,
            )
        except psycopg.ProgrammingError as e:
            raise click.ClickException(str(e))
    if as_json:
        print_json_for(result)
    else:
        for dbname, rows in result.items():
            print_table_for(rows, title=f"Database {dbname}")


@cli.command("dump")
@click.argument("dbname")
@pass_instance
@pass_ctx
def database_dump(ctx: Context, instance: system.Instance, dbname: str) -> None:
    """Dump a database"""
    with instances.postgresql_running(ctx, instance):
        databases.dump(ctx, instance, dbname)


@cli.command("dumps")
@click.argument("dbname", nargs=-1)
@as_json_option
@pass_instance
@pass_ctx
def database_dumps(
    ctx: Context, instance: system.Instance, dbname: Sequence[str], as_json: bool
) -> None:
    """List the database dumps"""
    dumps = databases.list_dumps(ctx, instance, dbnames=dbname)
    if as_json:
        print_json_for((i.dict(by_alias=True) for i in dumps))
    else:
        print_table_for((i.dict(by_alias=True) for i in dumps))


@cli.command("restore")
@click.argument("dump_id")
@click.argument("targetdbname", required=False)
@pass_instance
@pass_ctx
def database_restore(
    ctx: Context,
    instance: system.Instance,
    dump_id: str,
    targetdbname: Optional[str],
) -> None:
    """Restore a database dump

    DUMP_ID identifies the dump id.

    TARGETDBNAME identifies the (optional) name of the database in which the
    dump is reloaded. If provided, the database needs to be created beforehand.

    If TARGETDBNAME is not provided, the dump is reloaded using the database
    name that appears in the dump. In this case, the restore command will
    create the database so it needs to be dropped before running the command.
    """
    with instances.postgresql_running(ctx, instance):
        databases.restore(ctx, instance, dump_id, targetdbname)
