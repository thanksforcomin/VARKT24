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


class Target(DocEnum):
    """
    The type of object an antenna is targetting.
    See RemoteTech.Antenna#target.
    """
    active_vessel = 0, """
The active vessel.
"""
    celestial_body = 1, """
A celestial body.
"""
    ground_station = 2, """
A ground station.
"""
    vessel = 3, """
A specific vessel.
"""
    none = 4, """
No target.
"""


class Antenna(ClassBase):
    """
    A RemoteTech antenna. Obtained by calling RemoteTech.Comms#antennas or RemoteTech#antenna.
    """
    @property
    def has_connection(self) -> bool:
        """
        Whether the antenna has a connection.
        """
        return self._client._invoke(
            "RemoteTech",
            "Antenna_get_HasConnection",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Antenna")],
            self._client._types.bool_type
        )

    def _return_type_has_connection(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_has_connection(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "RemoteTech",
            "Antenna_get_HasConnection",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Antenna")],
            self._client._types.bool_type
        )

    @property
    def part(self) -> spacecenter.Part:
        """
        Get the part containing this antenna.
        """
        return self._client._invoke(
            "RemoteTech",
            "Antenna_get_Part",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Antenna")],
            self._client._types.class_type("SpaceCenter", "Part")
        )

    def _return_type_part(self) -> TypeBase:
        return self._client._types.class_type("SpaceCenter", "Part")

    def _build_call_part(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "RemoteTech",
            "Antenna_get_Part",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Antenna")],
            self._client._types.class_type("SpaceCenter", "Part")
        )

    @property
    def target(self) -> Target:
        """
        The object that the antenna is targetting.
        This property can be used to set the target to RemoteTech.Target#none or RemoteTech.Target#activeVessel.
        To set the target to a celestial body, ground station or vessel see RemoteTech.Antenna#targetBody,
        RemoteTech.Antenna#targetGroundStation and RemoteTech.Antenna#targetVessel.
        """
        return self._client._invoke(
            "RemoteTech",
            "Antenna_get_Target",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Antenna")],
            self._client._types.enumeration_type("RemoteTech", "Target")
        )

    @target.setter
    def target(self, value: Target) -> None:
        return self._client._invoke(
            "RemoteTech",
            "Antenna_set_Target",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("RemoteTech", "Antenna"), self._client._types.enumeration_type("RemoteTech", "Target")],
            None
        )

    def _return_type_target(self) -> TypeBase:
        return self._client._types.enumeration_type("RemoteTech", "Target")

    def _build_call_target(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "RemoteTech",
            "Antenna_get_Target",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Antenna")],
            self._client._types.enumeration_type("RemoteTech", "Target")
        )

    @property
    def target_body(self) -> spacecenter.CelestialBody:
        """
        The celestial body the antenna is targetting.
        """
        return self._client._invoke(
            "RemoteTech",
            "Antenna_get_TargetBody",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Antenna")],
            self._client._types.class_type("SpaceCenter", "CelestialBody")
        )

    @target_body.setter
    def target_body(self, value: spacecenter.CelestialBody) -> None:
        return self._client._invoke(
            "RemoteTech",
            "Antenna_set_TargetBody",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("RemoteTech", "Antenna"), self._client._types.class_type("SpaceCenter", "CelestialBody")],
            None
        )

    def _return_type_target_body(self) -> TypeBase:
        return self._client._types.class_type("SpaceCenter", "CelestialBody")

    def _build_call_target_body(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "RemoteTech",
            "Antenna_get_TargetBody",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Antenna")],
            self._client._types.class_type("SpaceCenter", "CelestialBody")
        )

    @property
    def target_ground_station(self) -> str:
        """
        The ground station the antenna is targetting.
        """
        return self._client._invoke(
            "RemoteTech",
            "Antenna_get_TargetGroundStation",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Antenna")],
            self._client._types.string_type
        )

    @target_ground_station.setter
    def target_ground_station(self, value: str) -> None:
        return self._client._invoke(
            "RemoteTech",
            "Antenna_set_TargetGroundStation",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("RemoteTech", "Antenna"), self._client._types.string_type],
            None
        )

    def _return_type_target_ground_station(self) -> TypeBase:
        return self._client._types.string_type

    def _build_call_target_ground_station(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "RemoteTech",
            "Antenna_get_TargetGroundStation",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Antenna")],
            self._client._types.string_type
        )

    @property
    def target_vessel(self) -> spacecenter.Vessel:
        """
        The vessel the antenna is targetting.
        """
        return self._client._invoke(
            "RemoteTech",
            "Antenna_get_TargetVessel",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Antenna")],
            self._client._types.class_type("SpaceCenter", "Vessel")
        )

    @target_vessel.setter
    def target_vessel(self, value: spacecenter.Vessel) -> None:
        return self._client._invoke(
            "RemoteTech",
            "Antenna_set_TargetVessel",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("RemoteTech", "Antenna"), self._client._types.class_type("SpaceCenter", "Vessel")],
            None
        )

    def _return_type_target_vessel(self) -> TypeBase:
        return self._client._types.class_type("SpaceCenter", "Vessel")

    def _build_call_target_vessel(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "RemoteTech",
            "Antenna_get_TargetVessel",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Antenna")],
            self._client._types.class_type("SpaceCenter", "Vessel")
        )



class Comms(ClassBase):
    """
    Communications for a vessel.
    """
    @property
    def antennas(self) -> List[Antenna]:
        """
        The antennas for this vessel.
        """
        return self._client._invoke(
            "RemoteTech",
            "Comms_get_Antennas",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Comms")],
            self._client._types.list_type(self._client._types.class_type("RemoteTech", "Antenna"))
        )

    def _return_type_antennas(self) -> TypeBase:
        return self._client._types.list_type(self._client._types.class_type("RemoteTech", "Antenna"))

    def _build_call_antennas(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "RemoteTech",
            "Comms_get_Antennas",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Comms")],
            self._client._types.list_type(self._client._types.class_type("RemoteTech", "Antenna"))
        )

    @property
    def has_connection(self) -> bool:
        """
        Whether the vessel has any connection.
        """
        return self._client._invoke(
            "RemoteTech",
            "Comms_get_HasConnection",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Comms")],
            self._client._types.bool_type
        )

    def _return_type_has_connection(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_has_connection(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "RemoteTech",
            "Comms_get_HasConnection",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Comms")],
            self._client._types.bool_type
        )

    @property
    def has_connection_to_ground_station(self) -> bool:
        """
        Whether the vessel has a connection to a ground station.
        """
        return self._client._invoke(
            "RemoteTech",
            "Comms_get_HasConnectionToGroundStation",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Comms")],
            self._client._types.bool_type
        )

    def _return_type_has_connection_to_ground_station(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_has_connection_to_ground_station(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "RemoteTech",
            "Comms_get_HasConnectionToGroundStation",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Comms")],
            self._client._types.bool_type
        )

    @property
    def has_flight_computer(self) -> bool:
        """
        Whether the vessel has a flight computer on board.
        """
        return self._client._invoke(
            "RemoteTech",
            "Comms_get_HasFlightComputer",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Comms")],
            self._client._types.bool_type
        )

    def _return_type_has_flight_computer(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_has_flight_computer(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "RemoteTech",
            "Comms_get_HasFlightComputer",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Comms")],
            self._client._types.bool_type
        )

    @property
    def has_local_control(self) -> bool:
        """
        Whether the vessel can be controlled locally.
        """
        return self._client._invoke(
            "RemoteTech",
            "Comms_get_HasLocalControl",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Comms")],
            self._client._types.bool_type
        )

    def _return_type_has_local_control(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_has_local_control(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "RemoteTech",
            "Comms_get_HasLocalControl",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Comms")],
            self._client._types.bool_type
        )

    @property
    def signal_delay(self) -> float:
        """
        The shortest signal delay to the vessel, in seconds.
        """
        return self._client._invoke(
            "RemoteTech",
            "Comms_get_SignalDelay",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Comms")],
            self._client._types.double_type
        )

    def _return_type_signal_delay(self) -> TypeBase:
        return self._client._types.double_type

    def _build_call_signal_delay(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "RemoteTech",
            "Comms_get_SignalDelay",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Comms")],
            self._client._types.double_type
        )

    @property
    def signal_delay_to_ground_station(self) -> float:
        """
        The signal delay between the vessel and the closest ground station, in seconds.
        """
        return self._client._invoke(
            "RemoteTech",
            "Comms_get_SignalDelayToGroundStation",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Comms")],
            self._client._types.double_type
        )

    def _return_type_signal_delay_to_ground_station(self) -> TypeBase:
        return self._client._types.double_type

    def _build_call_signal_delay_to_ground_station(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "RemoteTech",
            "Comms_get_SignalDelayToGroundStation",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Comms")],
            self._client._types.double_type
        )

    @property
    def vessel(self) -> spacecenter.Vessel:
        """
        Get the vessel.
        """
        return self._client._invoke(
            "RemoteTech",
            "Comms_get_Vessel",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Comms")],
            self._client._types.class_type("SpaceCenter", "Vessel")
        )

    def _return_type_vessel(self) -> TypeBase:
        return self._client._types.class_type("SpaceCenter", "Vessel")

    def _build_call_vessel(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "RemoteTech",
            "Comms_get_Vessel",
            [self],
            ["self"],
            [self._client._types.class_type("RemoteTech", "Comms")],
            self._client._types.class_type("SpaceCenter", "Vessel")
        )

    def signal_delay_to_vessel(self, other: spacecenter.Vessel) -> float:
        """
        The signal delay between the this vessel and another vessel, in seconds.
        """
        return self._client._invoke(
            "RemoteTech",
            "Comms_SignalDelayToVessel",
            [self, other],
            ["self", "other"],
            [self._client._types.class_type("RemoteTech", "Comms"), self._client._types.class_type("SpaceCenter", "Vessel")],
            self._client._types.double_type
        )

    def _return_type_signal_delay_to_vessel(self) -> TypeBase:
        return self._client._types.double_type

    def _build_call_signal_delay_to_vessel(self, other: spacecenter.Vessel) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "RemoteTech",
            "Comms_SignalDelayToVessel",
            [self, other],
            ["self", "other"],
            [self._client._types.class_type("RemoteTech", "Comms"), self._client._types.class_type("SpaceCenter", "Vessel")],
            self._client._types.double_type
        )



class RemoteTech:
    """
    This service provides functionality to interact with
    `RemoteTech <https://forum.kerbalspaceprogram.com/index.php?/topic/139167-13-remotetech-v188-2017-09-03/>`_.
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
        "Antenna": Antenna,
        "Comms": Comms,
    }
    _enumerations = {
        "Target": Target,
    }
    _exceptions = {
    }

    @property
    def available(self) -> bool:
        """
        Whether RemoteTech is installed.
        """
        return self._client._invoke(
            "RemoteTech",
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
            "RemoteTech",
            "get_Available",
            [],
            [],
            [],
            self._client._types.bool_type
        )

    @property
    def ground_stations(self) -> List[str]:
        """
        The names of the ground stations.
        """
        return self._client._invoke(
            "RemoteTech",
            "get_GroundStations",
            [],
            [],
            [],
            self._client._types.list_type(self._client._types.string_type)
        )

    def _return_type_ground_stations(self) -> TypeBase:
        return self._client._types.list_type(self._client._types.string_type)

    def _build_call_ground_stations(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "RemoteTech",
            "get_GroundStations",
            [],
            [],
            [],
            self._client._types.list_type(self._client._types.string_type)
        )

    def antenna(self, part: spacecenter.Part) -> Antenna:
        """
        Get the antenna object for a particular part.
        """
        return self._client._invoke(
            "RemoteTech",
            "Antenna",
            [part],
            ["part"],
            [self._client._types.class_type("SpaceCenter", "Part")],
            self._client._types.class_type("RemoteTech", "Antenna")
        )

    def _return_type_antenna(self) -> TypeBase:
        return self._client._types.class_type("RemoteTech", "Antenna")

    def _build_call_antenna(self, part: spacecenter.Part) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "RemoteTech",
            "Antenna",
            [part],
            ["part"],
            [self._client._types.class_type("SpaceCenter", "Part")],
            self._client._types.class_type("RemoteTech", "Antenna")
        )

    def comms(self, vessel: spacecenter.Vessel) -> Comms:
        """
        Get a communications object, representing the communication capability of a particular vessel.
        """
        return self._client._invoke(
            "RemoteTech",
            "Comms",
            [vessel],
            ["vessel"],
            [self._client._types.class_type("SpaceCenter", "Vessel")],
            self._client._types.class_type("RemoteTech", "Comms")
        )

    def _return_type_comms(self) -> TypeBase:
        return self._client._types.class_type("RemoteTech", "Comms")

    def _build_call_comms(self, vessel: spacecenter.Vessel) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "RemoteTech",
            "Comms",
            [vessel],
            ["vessel"],
            [self._client._types.class_type("SpaceCenter", "Vessel")],
            self._client._types.class_type("RemoteTech", "Comms")
        )
