from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Argument(_message.Message):
    __slots__ = ["position", "value"]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    position: int
    value: bytes
    def __init__(self, position: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...

class Class(_message.Message):
    __slots__ = ["documentation", "name"]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    documentation: str
    name: str
    def __init__(self, name: _Optional[str] = ..., documentation: _Optional[str] = ...) -> None: ...

class ConnectionRequest(_message.Message):
    __slots__ = ["client_identifier", "client_name", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CLIENT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    RPC: ConnectionRequest.Type
    STREAM: ConnectionRequest.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    client_identifier: bytes
    client_name: str
    type: ConnectionRequest.Type
    def __init__(self, type: _Optional[_Union[ConnectionRequest.Type, str]] = ..., client_name: _Optional[str] = ..., client_identifier: _Optional[bytes] = ...) -> None: ...

class ConnectionResponse(_message.Message):
    __slots__ = ["client_identifier", "message", "status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CLIENT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    MALFORMED_MESSAGE: ConnectionResponse.Status
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OK: ConnectionResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT: ConnectionResponse.Status
    WRONG_TYPE: ConnectionResponse.Status
    client_identifier: bytes
    message: str
    status: ConnectionResponse.Status
    def __init__(self, status: _Optional[_Union[ConnectionResponse.Status, str]] = ..., message: _Optional[str] = ..., client_identifier: _Optional[bytes] = ...) -> None: ...

class Dictionary(_message.Message):
    __slots__ = ["entries"]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[DictionaryEntry]
    def __init__(self, entries: _Optional[_Iterable[_Union[DictionaryEntry, _Mapping]]] = ...) -> None: ...

class DictionaryEntry(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    value: bytes
    def __init__(self, key: _Optional[bytes] = ..., value: _Optional[bytes] = ...) -> None: ...

class Enumeration(_message.Message):
    __slots__ = ["documentation", "name", "values"]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    documentation: str
    name: str
    values: _containers.RepeatedCompositeFieldContainer[EnumerationValue]
    def __init__(self, name: _Optional[str] = ..., values: _Optional[_Iterable[_Union[EnumerationValue, _Mapping]]] = ..., documentation: _Optional[str] = ...) -> None: ...

class EnumerationValue(_message.Message):
    __slots__ = ["documentation", "name", "value"]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    documentation: str
    name: str
    value: int
    def __init__(self, name: _Optional[str] = ..., value: _Optional[int] = ..., documentation: _Optional[str] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ["description", "name", "service", "stack_trace"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
    description: str
    name: str
    service: str
    stack_trace: str
    def __init__(self, service: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., stack_trace: _Optional[str] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ["stream"]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    stream: Stream
    def __init__(self, stream: _Optional[_Union[Stream, _Mapping]] = ...) -> None: ...

class Exception(_message.Message):
    __slots__ = ["documentation", "name"]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    documentation: str
    name: str
    def __init__(self, name: _Optional[str] = ..., documentation: _Optional[str] = ...) -> None: ...

class List(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, items: _Optional[_Iterable[bytes]] = ...) -> None: ...

class MultiplexedRequest(_message.Message):
    __slots__ = ["connection_request", "request"]
    CONNECTION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    connection_request: ConnectionRequest
    request: Request
    def __init__(self, connection_request: _Optional[_Union[ConnectionRequest, _Mapping]] = ..., request: _Optional[_Union[Request, _Mapping]] = ...) -> None: ...

class MultiplexedResponse(_message.Message):
    __slots__ = ["response", "stream_update"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STREAM_UPDATE_FIELD_NUMBER: _ClassVar[int]
    response: Response
    stream_update: StreamUpdate
    def __init__(self, response: _Optional[_Union[Response, _Mapping]] = ..., stream_update: _Optional[_Union[StreamUpdate, _Mapping]] = ...) -> None: ...

class Parameter(_message.Message):
    __slots__ = ["default_value", "name", "nullable", "type"]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    default_value: bytes
    name: str
    nullable: bool
    type: Type
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[Type, _Mapping]] = ..., default_value: _Optional[bytes] = ..., nullable: bool = ...) -> None: ...

class Procedure(_message.Message):
    __slots__ = ["documentation", "game_scenes", "name", "parameters", "return_is_nullable", "return_type"]
    class GameScene(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    EDITOR_SPH: Procedure.GameScene
    EDITOR_VAB: Procedure.GameScene
    FLIGHT: Procedure.GameScene
    GAME_SCENES_FIELD_NUMBER: _ClassVar[int]
    MISSION_BUILDER: Procedure.GameScene
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    RETURN_IS_NULLABLE_FIELD_NUMBER: _ClassVar[int]
    RETURN_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPACE_CENTER: Procedure.GameScene
    TRACKING_STATION: Procedure.GameScene
    documentation: str
    game_scenes: _containers.RepeatedScalarFieldContainer[Procedure.GameScene]
    name: str
    parameters: _containers.RepeatedCompositeFieldContainer[Parameter]
    return_is_nullable: bool
    return_type: Type
    def __init__(self, name: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[Parameter, _Mapping]]] = ..., return_type: _Optional[_Union[Type, _Mapping]] = ..., return_is_nullable: bool = ..., game_scenes: _Optional[_Iterable[_Union[Procedure.GameScene, str]]] = ..., documentation: _Optional[str] = ...) -> None: ...

class ProcedureCall(_message.Message):
    __slots__ = ["arguments", "procedure", "procedure_id", "service", "service_id"]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    arguments: _containers.RepeatedCompositeFieldContainer[Argument]
    procedure: str
    procedure_id: int
    service: str
    service_id: int
    def __init__(self, service: _Optional[str] = ..., procedure: _Optional[str] = ..., service_id: _Optional[int] = ..., procedure_id: _Optional[int] = ..., arguments: _Optional[_Iterable[_Union[Argument, _Mapping]]] = ...) -> None: ...

class ProcedureResult(_message.Message):
    __slots__ = ["error", "value"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    error: Error
    value: bytes
    def __init__(self, error: _Optional[_Union[Error, _Mapping]] = ..., value: _Optional[bytes] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ["calls"]
    CALLS_FIELD_NUMBER: _ClassVar[int]
    calls: _containers.RepeatedCompositeFieldContainer[ProcedureCall]
    def __init__(self, calls: _Optional[_Iterable[_Union[ProcedureCall, _Mapping]]] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["error", "results"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    error: Error
    results: _containers.RepeatedCompositeFieldContainer[ProcedureResult]
    def __init__(self, error: _Optional[_Union[Error, _Mapping]] = ..., results: _Optional[_Iterable[_Union[ProcedureResult, _Mapping]]] = ...) -> None: ...

class Service(_message.Message):
    __slots__ = ["classes", "documentation", "enumerations", "exceptions", "name", "procedures"]
    CLASSES_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    ENUMERATIONS_FIELD_NUMBER: _ClassVar[int]
    EXCEPTIONS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROCEDURES_FIELD_NUMBER: _ClassVar[int]
    classes: _containers.RepeatedCompositeFieldContainer[Class]
    documentation: str
    enumerations: _containers.RepeatedCompositeFieldContainer[Enumeration]
    exceptions: _containers.RepeatedCompositeFieldContainer[Exception]
    name: str
    procedures: _containers.RepeatedCompositeFieldContainer[Procedure]
    def __init__(self, name: _Optional[str] = ..., procedures: _Optional[_Iterable[_Union[Procedure, _Mapping]]] = ..., classes: _Optional[_Iterable[_Union[Class, _Mapping]]] = ..., enumerations: _Optional[_Iterable[_Union[Enumeration, _Mapping]]] = ..., exceptions: _Optional[_Iterable[_Union[Exception, _Mapping]]] = ..., documentation: _Optional[str] = ...) -> None: ...

class Services(_message.Message):
    __slots__ = ["services"]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedCompositeFieldContainer[Service]
    def __init__(self, services: _Optional[_Iterable[_Union[Service, _Mapping]]] = ...) -> None: ...

class Set(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, items: _Optional[_Iterable[bytes]] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ["adaptive_rate_control", "blocking_recv", "bytes_read", "bytes_read_rate", "bytes_written", "bytes_written_rate", "exec_time_per_rpc_update", "max_time_per_update", "one_rpc_per_update", "poll_time_per_rpc_update", "recv_timeout", "rpc_rate", "rpcs_executed", "stream_rpc_rate", "stream_rpcs", "stream_rpcs_executed", "time_per_rpc_update", "time_per_stream_update", "version"]
    ADAPTIVE_RATE_CONTROL_FIELD_NUMBER: _ClassVar[int]
    BLOCKING_RECV_FIELD_NUMBER: _ClassVar[int]
    BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    BYTES_READ_RATE_FIELD_NUMBER: _ClassVar[int]
    BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    BYTES_WRITTEN_RATE_FIELD_NUMBER: _ClassVar[int]
    EXEC_TIME_PER_RPC_UPDATE_FIELD_NUMBER: _ClassVar[int]
    MAX_TIME_PER_UPDATE_FIELD_NUMBER: _ClassVar[int]
    ONE_RPC_PER_UPDATE_FIELD_NUMBER: _ClassVar[int]
    POLL_TIME_PER_RPC_UPDATE_FIELD_NUMBER: _ClassVar[int]
    RECV_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    RPCS_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    RPC_RATE_FIELD_NUMBER: _ClassVar[int]
    STREAM_RPCS_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    STREAM_RPCS_FIELD_NUMBER: _ClassVar[int]
    STREAM_RPC_RATE_FIELD_NUMBER: _ClassVar[int]
    TIME_PER_RPC_UPDATE_FIELD_NUMBER: _ClassVar[int]
    TIME_PER_STREAM_UPDATE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    adaptive_rate_control: bool
    blocking_recv: bool
    bytes_read: int
    bytes_read_rate: float
    bytes_written: int
    bytes_written_rate: float
    exec_time_per_rpc_update: float
    max_time_per_update: int
    one_rpc_per_update: bool
    poll_time_per_rpc_update: float
    recv_timeout: int
    rpc_rate: float
    rpcs_executed: int
    stream_rpc_rate: float
    stream_rpcs: int
    stream_rpcs_executed: int
    time_per_rpc_update: float
    time_per_stream_update: float
    version: str
    def __init__(self, version: _Optional[str] = ..., bytes_read: _Optional[int] = ..., bytes_written: _Optional[int] = ..., bytes_read_rate: _Optional[float] = ..., bytes_written_rate: _Optional[float] = ..., rpcs_executed: _Optional[int] = ..., rpc_rate: _Optional[float] = ..., one_rpc_per_update: bool = ..., max_time_per_update: _Optional[int] = ..., adaptive_rate_control: bool = ..., blocking_recv: bool = ..., recv_timeout: _Optional[int] = ..., time_per_rpc_update: _Optional[float] = ..., poll_time_per_rpc_update: _Optional[float] = ..., exec_time_per_rpc_update: _Optional[float] = ..., stream_rpcs: _Optional[int] = ..., stream_rpcs_executed: _Optional[int] = ..., stream_rpc_rate: _Optional[float] = ..., time_per_stream_update: _Optional[float] = ...) -> None: ...

class Stream(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class StreamResult(_message.Message):
    __slots__ = ["id", "result"]
    ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    id: int
    result: ProcedureResult
    def __init__(self, id: _Optional[int] = ..., result: _Optional[_Union[ProcedureResult, _Mapping]] = ...) -> None: ...

class StreamUpdate(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[StreamResult]
    def __init__(self, results: _Optional[_Iterable[_Union[StreamResult, _Mapping]]] = ...) -> None: ...

class Tuple(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, items: _Optional[_Iterable[bytes]] = ...) -> None: ...

class Type(_message.Message):
    __slots__ = ["code", "name", "service", "types"]
    class TypeCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BOOL: Type.TypeCode
    BYTES: Type.TypeCode
    CLASS: Type.TypeCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    DICTIONARY: Type.TypeCode
    DOUBLE: Type.TypeCode
    ENUMERATION: Type.TypeCode
    EVENT: Type.TypeCode
    FLOAT: Type.TypeCode
    LIST: Type.TypeCode
    NAME_FIELD_NUMBER: _ClassVar[int]
    NONE: Type.TypeCode
    PROCEDURE_CALL: Type.TypeCode
    SERVICES: Type.TypeCode
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SET: Type.TypeCode
    SINT32: Type.TypeCode
    SINT64: Type.TypeCode
    STATUS: Type.TypeCode
    STREAM: Type.TypeCode
    STRING: Type.TypeCode
    TUPLE: Type.TypeCode
    TYPES_FIELD_NUMBER: _ClassVar[int]
    UINT32: Type.TypeCode
    UINT64: Type.TypeCode
    code: Type.TypeCode
    name: str
    service: str
    types: _containers.RepeatedCompositeFieldContainer[Type]
    def __init__(self, code: _Optional[_Union[Type.TypeCode, str]] = ..., service: _Optional[str] = ..., name: _Optional[str] = ..., types: _Optional[_Iterable[_Union[Type, _Mapping]]] = ...) -> None: ...
