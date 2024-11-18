# pylint: disable=line-too-long,invalid-name,redefined-builtin,too-many-lines
from __future__ import annotations
from typing import Tuple, Set, Dict, List, Optional, TYPE_CHECKING
import krpc.schema
from krpc.schema import KRPC_pb2
from krpc.types import TypeBase, ClassBase, WrappedClass, DocEnum
from krpc.event import Event
if TYPE_CHECKING:
    from krpc.services import Client
from krpc.services import spacecenter


class Laser(ClassBase):
    """
    A LaserDist laser.
    """
    @property
    def cloud(self) -> List[float]:
        """
        Get the point cloud from the LiDAR.
        Returns an empty list on failure.
        """
        return self._client._invoke(
            "LiDAR",
            "Laser_get_Cloud",
            [self],
            ["self"],
            [self._client._types.class_type("LiDAR", "Laser")],
            self._client._types.list_type(self._client._types.double_type)
        )

    def _return_type_cloud(self) -> TypeBase:
        return self._client._types.list_type(self._client._types.double_type)

    def _build_call_cloud(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "LiDAR",
            "Laser_get_Cloud",
            [self],
            ["self"],
            [self._client._types.class_type("LiDAR", "Laser")],
            self._client._types.list_type(self._client._types.double_type)
        )

    @property
    def part(self) -> spacecenter.Part:
        """
        Get the part containing this LiDAR.
        """
        return self._client._invoke(
            "LiDAR",
            "Laser_get_Part",
            [self],
            ["self"],
            [self._client._types.class_type("LiDAR", "Laser")],
            self._client._types.class_type("SpaceCenter", "Part")
        )

    def _return_type_part(self) -> TypeBase:
        return self._client._types.class_type("SpaceCenter", "Part")

    def _build_call_part(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "LiDAR",
            "Laser_get_Part",
            [self],
            ["self"],
            [self._client._types.class_type("LiDAR", "Laser")],
            self._client._types.class_type("SpaceCenter", "Part")
        )



class LiDAR:
    """
    LaserDist service.
    """

    def __init__(self, client: Client) -> None:
        self._client = client

    def __getattribute__(self, name):
        # Intercepts calls to obtain classes from the service,
        # to inject the client instance so that it can be used
        # for static method calls
        classes = object.__getattribute__(self, "_classes")
        if name in classes:
            client = object.__getattribute__(self, "_client")
            return WrappedClass(client, classes[name])

        # Intercept calls to obtain enumeration types
        enumerations = object.__getattribute__(self, "_enumerations")
        if name in enumerations:
           return enumerations[name]

        # Intercept calls to obtain exception types
        exceptions = object.__getattribute__(self, "_exceptions")
        if name in exceptions:
           return exceptions[name]

        # Fall back to default behaviour
        return object.__getattribute__(self, name)

    def __dir__(self):
        result = object.__dir__(self)
        result.extend(object.__getattribute__(self, "_classes").keys())
        result.extend(object.__getattribute__(self, "_enumerations").keys())
        result.extend(object.__getattribute__(self, "_exceptions").keys())
        return result

    _classes = {
        "Laser": Laser,
    }
    _enumerations = {
    }
    _exceptions = {
    }

    @property
    def available(self) -> bool:
        """
        Check if the LaserDist API is available.
        """
        return self._client._invoke(
            "LiDAR",
            "get_Available",
            [],
            [],
            [],
            self._client._types.bool_type
        )

    def _return_type_available(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_available(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "LiDAR",
            "get_Available",
            [],
            [],
            [],
            self._client._types.bool_type
        )

    def laser(self, part: spacecenter.Part) -> Laser:
        """
        Get a LaserDist part.
        """
        return self._client._invoke(
            "LiDAR",
            "Laser",
            [part],
            ["part"],
            [self._client._types.class_type("SpaceCenter", "Part")],
            self._client._types.class_type("LiDAR", "Laser")
        )

    def _return_type_laser(self) -> TypeBase:
        return self._client._types.class_type("LiDAR", "Laser")

    def _build_call_laser(self, part: spacecenter.Part) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "LiDAR",
            "Laser",
            [part],
            ["part"],
            [self._client._types.class_type("SpaceCenter", "Part")],
            self._client._types.class_type("LiDAR", "Laser")
        )
