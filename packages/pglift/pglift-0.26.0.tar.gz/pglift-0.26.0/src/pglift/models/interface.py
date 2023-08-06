import enum
import hashlib
from datetime import datetime
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    Dict,
    Final,
    Iterator,
    List,
    Literal,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
)

from pgtoolkit import conf as pgconf
from pgtoolkit.ctl import Status
from pydantic import (
    BaseModel,
    ByteSize,
    DirectoryPath,
    Field,
    SecretStr,
    ValidationError,
    create_model,
    root_validator,
    validator,
)
from pydantic.error_wrappers import ErrorWrapper
from pydantic.utils import lenient_issubclass

from .. import settings, util
from ..types import AnsibleConfig, AutoStrEnum, CLIConfig
from ..types import Extension as Extension
from ..types import Manifest, Port, ServiceManifest

if TYPE_CHECKING:
    from ..pm import PluginManager
    from ..postgresql import Standby

default_port: Final = 5432


def validate_ports(model: BaseModel) -> None:
    """Walk fields of 'model', checking those with type Port if their value is
    available.
    """

    def _validate(
        model: BaseModel, *, loc: Tuple[str, ...] = ()
    ) -> Iterator[ErrorWrapper]:
        cls = model.__class__
        for name, field in cls.__fields__.items():
            value = getattr(model, name)
            if value is None:
                continue
            ftype = field.outer_type_
            if lenient_issubclass(ftype, BaseModel):
                yield from _validate(value, loc=loc + (name,))
            elif lenient_issubclass(ftype, Port):
                assert isinstance(value, Port)
                if not value.available():
                    yield ErrorWrapper(
                        ValueError(f"port {value} already in use"), loc + (name,)
                    )

    errors = list(_validate(model))
    if errors:
        raise ValidationError(errors, model.__class__)


class InstanceState(AutoStrEnum):
    """Instance state."""

    stopped = enum.auto()
    """stopped"""

    started = enum.auto()
    """started"""

    absent = enum.auto()
    """absent"""

    restarted = enum.auto()
    """restarted"""

    @classmethod
    def from_pg_status(cls, status: Status) -> "InstanceState":
        """Instance state from PostgreSQL status.

        >>> InstanceState.from_pg_status(Status.running)
        <InstanceState.started: 'started'>
        >>> InstanceState.from_pg_status(Status.not_running)
        <InstanceState.stopped: 'stopped'>
        >>> InstanceState.from_pg_status(Status.unspecified_datadir)
        <InstanceState.absent: 'absent'>
        """
        return cls(
            {
                status.running: cls.started,
                status.not_running: cls.stopped,
                status.unspecified_datadir: cls.absent,
            }[status]
        )


class PresenceState(AutoStrEnum):
    """Should the object be present or absent?"""

    present = enum.auto()
    absent = enum.auto()


class InstanceListItem(Manifest):

    name: str
    version: str
    port: int
    datadir: DirectoryPath
    status: str


class BaseInstance(Manifest):
    """PostgreSQL instance suitable for lookup"""

    name: str = Field(readOnly=True, description=("Instance name."))
    version: Optional[settings.PostgreSQLVersion] = Field(
        default=None, description="PostgreSQL version.", readOnly=True
    )

    @validator("name")
    def __validate_name_(cls, v: str) -> str:
        """Validate 'name' field.

        >>> Instance(name='without_dash')  # doctest: +ELLIPSIS
        Instance(name='without_dash', ...)
        >>> Instance(name='with-dash')
        Traceback (most recent call last):
            ...
        pydantic.error_wrappers.ValidationError: 1 validation error for Instance
        name
          instance name must not contain dashes (type=value_error)
        >>> Instance(name='with/slash')
        Traceback (most recent call last):
            ...
        pydantic.error_wrappers.ValidationError: 1 validation error for Instance
        name
          instance name must not contain slashes (type=value_error)
        """
        # Avoid dash as this will break systemd instance unit.
        if "-" in v:
            raise ValueError("instance name must not contain dashes")
        # Likewise, slash messes up with file paths.
        if "/" in v:
            raise ValueError("instance name must not contain slashes")
        return v


class Role(Manifest):
    """PostgreSQL role"""

    _cli_config: ClassVar[Dict[str, CLIConfig]] = {
        "in_roles": {"name": "in_role"},
        "state": {"hide": True},
        "has_password": {"hide": True},
    }
    _ansible_config: ClassVar[Dict[str, AnsibleConfig]] = {
        "has_password": {"hide": True},
    }
    name: str = Field(readOnly=True, description=("Role name."))
    password: Optional[SecretStr] = Field(
        default=None, description="Role password.", exclude=True
    )
    has_password: bool = Field(
        default=False,
        description="True if the role has a password.",
        readOnly=True,
    )
    inherit: bool = Field(
        default=True,
        description="Let the role inherit the privileges of the roles it is a member of.",
    )
    login: bool = Field(default=False, description="Allow the role to log in.")
    superuser: bool = Field(default=False, description="Superuser role.")
    replication: bool = Field(default=False, description="Replication role.")
    connection_limit: Optional[int] = Field(
        description="How many concurrent connections the role can make.",
    )
    validity: Optional[datetime] = Field(
        description="Sets a date and time after which the role's password is no longer valid."
    )
    in_roles: List[str] = Field(
        default_factory=list,
        description="List of roles to which the new role will be added as a new member.",
    )
    pgpass: bool = Field(
        default=False, description="Add an entry in password file for this role."
    )
    state: PresenceState = Field(
        default=PresenceState.present, description=("Role state.")
    )

    @validator("has_password", always=True)
    def __set_has_password(cls, value: bool, values: Dict[str, Any]) -> bool:
        """Set 'has_password' field according to 'password'.

        >>> r = Role(name="postgres")
        >>> r.has_password
        False
        >>> r = Role(name="postgres", password="P4zzw0rd")
        >>> r.has_password
        True
        >>> r = Role(name="postgres", has_password=True)
        >>> r.has_password
        True
        """
        return value or values["password"] is not None


class Database(Manifest):
    """PostgreSQL database"""

    _cli_config: ClassVar[Dict[str, CLIConfig]] = {
        "settings": {"hide": True},
        "state": {"hide": True},
        "extensions": {"name": "extension"},
    }
    _ansible_config: ClassVar[Dict[str, AnsibleConfig]] = {
        "settings": {"spec": {"type": "dict", "required": False}},
    }
    name: str = Field(readOnly=True, description=("Database name."))
    owner: Optional[str] = Field(
        description="The role name of the user who will own the database."
    )
    settings: Optional[Dict[str, Optional[pgconf.Value]]] = Field(
        default=None,
        description=(
            "Session defaults for run-time configuration variables for the database. "
            "Upon update, an empty (dict) value would reset all settings."
        ),
    )
    extensions: List[Extension] = Field(
        default_factory=list,
        description="List of extensions to create in the database.",
    )
    state: PresenceState = Field(
        default=PresenceState.present, description=("Database state.")
    )


class DatabaseDump(Manifest):
    id: str
    dbname: str
    date: datetime

    @root_validator(pre=True)
    def __generate_id_(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """Identifier for the dump."""
        id = "_".join(
            [
                values["dbname"],
                hashlib.blake2b(
                    (values["dbname"] + str(values["date"])).encode("utf-8"),
                    digest_size=5,
                ).hexdigest(),
            ]
        )
        values["id"] = id
        return values


class Instance(BaseInstance):
    """PostgreSQL instance"""

    class Config(Manifest.Config):
        # Allow extra fields to permit plugins to populate an object with
        # their specific data, following (hopefully) what's defined by
        # the "composite" model (see composite()).
        extra = "allow"

    _cli_config: ClassVar[Dict[str, CLIConfig]] = {
        "status": {"hide": True},
        "state": {
            "choices": [InstanceState.started.value, InstanceState.stopped.value]
        },
        "pending_restart": {"hide": True},
        "restart_on_changes": {"hide": True},
        "configuration": {"hide": True},
        "extensions": {"name": "extension"},
        "roles": {"hide": True},
        "databases": {"hide": True},
    }
    _ansible_config: ClassVar[Dict[str, AnsibleConfig]] = {
        "pending_restart": {"hide": True},
    }

    _T = TypeVar("_T", bound="Instance")

    @classmethod
    def composite(cls: Type[_T], pm: "PluginManager") -> Type[_T]:
        """Create a model class, based on this one, with extra fields based on
        interface models for satellite components defined in plugins.
        """
        fields = {}
        for m in pm.hook.interface_model():
            sname = m.__service__
            if sname in fields:
                raise ValueError(f"duplicated '{sname}' service")
            fields[sname] = Optional[m], Field(default_factory=m)
        try:
            m = pm.hook.standby_model()
        except ValueError:
            pass
        else:
            fields["standby"] = Optional[m], Field(default=None)
        # XXX Spurious 'type: ignore' below.
        m = create_model(cls.__name__, __base__=cls, __module__=__name__, **fields)  # type: ignore[call-overload]
        # pydantic.create_model() uses type(), so this will confuse mypy which
        # cannot handle dynamic base class; hence the 'type: ignore'.
        return m  # type: ignore[no-any-return]

    port: Port = Field(
        default=Port(default_port),
        description=(
            "TCP port the postgresql instance will be listening to. "
            f"If unspecified, default to {default_port} unless a 'port' setting is found in 'configuration'."
        ),
    )
    configuration: Dict[str, Any] = Field(
        default={}, description=("Settings for the PostgreSQL instance.")
    )
    surole_password: Optional[SecretStr] = Field(
        default=None,
        description="Super-user role password.",
        readOnly=True,
        exclude=True,
    )
    replrole_password: Optional[SecretStr] = Field(
        default=None,
        description="Replication role password.",
        readOnly=True,
        exclude=True,
    )
    data_checksums: Optional[bool] = Field(
        default=None,
        description=(
            "Enable or disable data checksums. "
            "If unspecified, fall back to site settings choice."
        ),
    )
    locale: Optional[str] = Field(
        default=None, description="Default locale.", readOnly=True
    )
    encoding: Optional[str] = Field(
        default=None,
        description="Character encoding of the PostgreSQL instance.",
        readOnly=True,
    )

    class Auth(BaseModel):
        local: Optional[settings.AuthLocalMethod] = Field(
            default=None,
            description="Authentication method for local-socket connections",
            readOnly=True,
        )
        host: Optional[settings.AuthHostMethod] = Field(
            default=None,
            description="Authentication method for local TCP/IP connections",
            readOnly=True,
        )

    auth: Optional[Auth] = Field(default=None, exclude=True, writeOnly=True)

    extensions: List[Extension] = Field(
        default_factory=list,
        description="List of extensions to install in the instance.",
    )

    state: InstanceState = Field(
        default=InstanceState.started,
        description="Runtime state.",
    )
    databases: List["Database"] = Field(
        default_factory=list,
        description="Databases",
        exclude=True,
        writeOnly=True,
    )
    roles: List["Role"] = Field(
        default_factory=list,
        description="Roles",
        exclude=True,
        writeOnly=True,
    )

    pending_restart: bool = Field(
        default=False,
        description="Whether the instance needs a restart to account for configuration changes.",
        readOnly=True,
    )
    restart_on_changes: bool = Field(
        default=False,
        description="Whether or not to automatically restart the instance to account for configuration changes.",
        exclude=True,
        writeOnly=True,
    )

    @root_validator(pre=True)
    def __validate_port_(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """Validate that 'port' field and configuration['port'] are consistent.

        If unspecified, 'port' is either set from configuration value or from
        the default port value.

        >>> i = Instance(name="i")
        >>> i.port, "port" in i.configuration
        (5432, False)
        >>> i = Instance(name="i", configuration={"port": 5423})
        >>> i.port, i.configuration["port"]
        (5423, 5423)
        >>> i = Instance(name="i", port=5454)
        >>> i.port, "port" in i.configuration
        (5454, False)

        Otherwise, and if configuration['port'] exists, make sure values are
        consistent and possibly cast the latter as an integer.

        >>> i = Instance(name="i", configuration={"port": 5455})
        >>> i.port, i.configuration["port"]
        (5455, 5455)
        >>> i = Instance(name="i", port=123, configuration={"port": "123"})
        >>> i.port, i.configuration["port"]
        (123, 123)
        >>> Instance(name="i", port=321, configuration={"port": 123})
        Traceback (most recent call last):
            ...
        pydantic.error_wrappers.ValidationError: 1 validation error for Instance
        __root__
          'port' field and configuration['port'] mismatch (type=value_error)
        >>> Instance(name="i", configuration={"port": "abc"})
        Traceback (most recent call last):
            ...
        pydantic.error_wrappers.ValidationError: 1 validation error for Instance
        __root__
          invalid literal for int() with base 10: 'abc' (type=value_error)
        """
        config_port = None
        try:
            port = values["port"]
        except KeyError:
            try:
                config_port = int(values["configuration"]["port"])
            except KeyError:
                pass
            else:
                values["port"] = Port(config_port)
        else:
            try:
                config_port = int(values["configuration"]["port"])
            except KeyError:
                pass
            else:
                if config_port != port:
                    raise ValueError("'port' field and configuration['port'] mismatch")
        if config_port is not None:
            values["configuration"]["port"] = config_port
        return values

    @validator("configuration")
    def __validate_configuration_(cls, value: Dict[str, Any]) -> Dict[str, Any]:
        """Validate 'configuration' field.

        >>> Instance(name="main", configuration={"log_directory": 1})
        Traceback (most recent call last):
          ...
        pydantic.error_wrappers.ValidationError: 1 validation error for Instance
        configuration
          expecting a string for 'log_directory' setting (type=value_error)
        """
        try:
            if not isinstance(value["log_directory"], str):
                raise ValueError("expecting a string for 'log_directory' setting")
        except KeyError:
            pass
        return value

    _S = TypeVar("_S", bound=ServiceManifest)

    def service_manifest(self, stype: Type[_S]) -> Optional[_S]:
        """Return satellite service manifest attached to this instance.

        :raises ValueError: if not found.
        """
        fname = stype.__service__
        try:
            s = getattr(self, fname)
        except AttributeError:
            raise ValueError(fname)
        if s is None:
            return None
        assert isinstance(
            s, stype
        ), f"expecting field {fname} to have type {stype} (got {type(s)})"
        return s

    def _standby(self) -> Optional["Standby"]:
        return getattr(self, "standby", None)

    def surole(self, settings: settings.Settings) -> "Role":
        s = settings.postgresql.surole
        return Role(
            name=s.name,
            password=self.surole_password,
            pgpass=s.pgpass,
        )

    def replrole(self, settings: settings.Settings) -> "Role":
        name = settings.postgresql.replrole
        return Role(
            name=name,
            password=self.replrole_password,
            login=True,
            replication=True,
        )

    def auth_options(self, settings: settings.AuthSettings) -> Auth:
        auth = self.auth
        local, host = settings.local, settings.host
        if auth:
            local = auth.local or local
            host = auth.host or host
        return Instance.Auth(local=local, host=host)

    def pg_hba(self, settings: settings.Settings) -> str:
        surole = self.surole(settings)
        replrole = self.replrole(settings)
        auth = self.auth_options(settings.postgresql.auth)
        return util.template("postgresql", "pg_hba.conf").format(
            auth=auth,
            surole=surole.name,
            backuprole=settings.postgresql.backuprole.name,
            replrole=replrole.name,
        )

    def pg_ident(self, settings: settings.Settings) -> str:
        surole = self.surole(settings)
        replrole = self.replrole(settings)
        return util.template("postgresql", "pg_ident.conf").format(
            surole=surole.name,
            backuprole=settings.postgresql.backuprole.name,
            replrole=replrole.name,
            sysuser=settings.sysuser[0],
        )

    def initdb_options(self, base: settings.InitdbSettings) -> settings.InitdbSettings:
        data_checksums: Union[None, Literal[True]] = {
            True: True,
            False: None,
            None: base.data_checksums or None,
        }[self.data_checksums]
        return settings.InitdbSettings(
            locale=self.locale or base.locale,
            encoding=self.encoding or base.encoding,
            data_checksums=data_checksums,
        )


class InstanceBackup(Manifest):
    label: str
    size: ByteSize
    repo_size: ByteSize
    date_start: datetime
    date_stop: datetime
    type: Literal["incr", "diff", "full"]
    databases: List[str]


class Tablespace(BaseModel):
    name: str
    location: str
    size: ByteSize


class DetailedDatabase(Manifest):
    """PostgreSQL database (with details)"""

    name: str
    owner: str
    encoding: str
    collation: str
    ctype: str
    acls: List[str]
    size: ByteSize
    description: Optional[str]
    tablespace: Tablespace

    def __init__(
        self,
        **kwargs: Any,
    ) -> None:
        tablespace = kwargs["tablespace"]
        if not isinstance(tablespace, Tablespace):
            assert isinstance(tablespace, str)
            try:
                kwargs["tablespace"] = Tablespace(
                    name=tablespace,
                    location=kwargs.pop("tablespace_location"),
                    size=kwargs.pop("tablespace_size"),
                )
            except KeyError as exc:
                raise TypeError(f"missing {exc} argument when 'tablespace' is a string")
        super().__init__(**kwargs)


class DefaultPrivilege(Manifest):
    """Default access privilege"""

    database: str
    schema_: str = Field(alias="schema")
    object_type: str
    role: str
    privileges: List[str]

    @validator("privileges")
    def __sort_privileges_(cls, value: List[str]) -> List[str]:
        return sorted(value)


class Privilege(DefaultPrivilege):
    """Access privilege"""

    object_name: str
    column_privileges: Dict[str, List[str]]

    @validator("column_privileges")
    def __sort_column_privileges_(
        cls, value: Dict[str, List[str]]
    ) -> Dict[str, List[str]]:
        for v in value.values():
            v.sort()
        return value


class PGSetting(Manifest):
    """A column from pg_settings view."""

    _query: ClassVar[
        str
    ] = "SELECT name, setting, context, pending_restart FROM pg_settings"

    name: str
    setting: str
    context: str
    pending_restart: bool


class ApplyChangeState(AutoStrEnum):
    """A apply change state for object handled by pglift"""

    created = enum.auto()  #:
    changed = enum.auto()  #:
    dropped = enum.auto()  #:


class ApplyResult(Manifest):
    """
    ApplyResult allows to describe the result of a call to apply function
    (Eg: pglift.database.apply) to an object (Eg: database, instance,...).

    The `change_state` attribute of this class can be set to one of to those values:
      - :attr:`~ApplyChangeState.created` if the object has been created,
      - :attr:`~ApplyChangeState.changed` if the object has been changed,
      - :attr:`~ApplyChangeState.dropped` if the object has been dropped,
      - :obj:`None` if nothing happened to the object we manipulate (neither created,
        changed or dropped)
    """

    change_state: Optional[ApplyChangeState] = Field(
        description="Define the change applied (created, changed or dropped) to a manipulated object",
    )  #:


class InstanceApplyResult(ApplyResult):
    pending_restart: bool = Field(
        default=False,
        description="Whether the instance needs a restart to account for configuration changes.",
    )
