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


class AlarmAction(DocEnum):
    """
    The action performed by an alarm when it fires.
    """
    do_nothing = 0, """
Don't do anything at all...
"""
    do_nothing_delete_when_passed = 1, """
Don't do anything, and delete the alarm.
"""
    kill_warp = 2, """
Drop out of time warp.
"""
    kill_warp_only = 3, """
Drop out of time warp.
"""
    message_only = 4, """
Display a message.
"""
    pause_game = 5, """
Pause the game.
"""


class AlarmType(DocEnum):
    """
    The type of an alarm.
    """
    raw = 0, """
An alarm for a specific date/time or a specific period in the future.
"""
    maneuver = 1, """
An alarm based on the next maneuver node on the current ships flight path.
This node will be stored and can be restored when you come back to the ship.
"""
    maneuver_auto = 2, """
See KerbalAlarmClock.AlarmType#maneuver.
"""
    apoapsis = 3, """
An alarm for furthest part of the orbit from the planet.
"""
    periapsis = 4, """
An alarm for nearest part of the orbit from the planet.
"""
    ascending_node = 5, """
Ascending node for the targeted object, or equatorial ascending node.
"""
    descending_node = 6, """
Descending node for the targeted object, or equatorial descending node.
"""
    closest = 7, """
An alarm based on the closest approach of this vessel to the targeted
vessel, some number of orbits into the future.
"""
    contract = 8, """
An alarm based on the expiry or deadline of contracts in career modes.
"""
    contract_auto = 9, """
See KerbalAlarmClock.AlarmType#contract.
"""
    crew = 10, """
An alarm that is attached to a crew member.
"""
    distance = 11, """
An alarm that is triggered when a selected target comes within a chosen distance.
"""
    earth_time = 12, """
An alarm based on the time in the "Earth" alternative Universe (aka the Real World).
"""
    launch_rendevous = 13, """
An alarm that fires as your landed craft passes under the orbit of your target.
"""
    soi_change = 14, """
An alarm manually based on when the next SOI point is on the flight path
or set to continually monitor the active flight path and add alarms as it
detects SOI changes.
"""
    soi_change_auto = 15, """
See KerbalAlarmClock.AlarmType#sOIChange.
"""
    transfer = 16, """
An alarm based on Interplanetary Transfer Phase Angles, i.e. when should
I launch to planet X? Based on Kosmo Not's post and used in Olex's
Calculator.
"""
    transfer_modelled = 17, """
See KerbalAlarmClock.AlarmType#transfer.
"""


class Alarm(ClassBase):
    """
    Represents an alarm. Obtained by calling
    KerbalAlarmClock#alarms,
    KerbalAlarmClock#alarmWithName or
    KerbalAlarmClock#alarmsWithType.
    """
    @property
    def action(self) -> AlarmAction:
        """
        The action that the alarm triggers.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_get_Action",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.enumeration_type("KerbalAlarmClock", "AlarmAction")
        )

    @action.setter
    def action(self, value: AlarmAction) -> None:
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_set_Action",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm"), self._client._types.enumeration_type("KerbalAlarmClock", "AlarmAction")],
            None
        )

    def _return_type_action(self) -> TypeBase:
        return self._client._types.enumeration_type("KerbalAlarmClock", "AlarmAction")

    def _build_call_action(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KerbalAlarmClock",
            "Alarm_get_Action",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.enumeration_type("KerbalAlarmClock", "AlarmAction")
        )

    @property
    def id(self) -> str:
        """
        The unique identifier for the alarm.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_get_ID",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.string_type
        )

    def _return_type_id(self) -> TypeBase:
        return self._client._types.string_type

    def _build_call_id(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KerbalAlarmClock",
            "Alarm_get_ID",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.string_type
        )

    @property
    def margin(self) -> float:
        """
        The number of seconds before the event that the alarm will fire.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_get_Margin",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.double_type
        )

    @margin.setter
    def margin(self, value: float) -> None:
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_set_Margin",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm"), self._client._types.double_type],
            None
        )

    def _return_type_margin(self) -> TypeBase:
        return self._client._types.double_type

    def _build_call_margin(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KerbalAlarmClock",
            "Alarm_get_Margin",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.double_type
        )

    @property
    def name(self) -> str:
        """
        The short name of the alarm.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_get_Name",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.string_type
        )

    @name.setter
    def name(self, value: str) -> None:
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_set_Name",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm"), self._client._types.string_type],
            None
        )

    def _return_type_name(self) -> TypeBase:
        return self._client._types.string_type

    def _build_call_name(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KerbalAlarmClock",
            "Alarm_get_Name",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.string_type
        )

    @property
    def notes(self) -> str:
        """
        The long description of the alarm.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_get_Notes",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.string_type
        )

    @notes.setter
    def notes(self, value: str) -> None:
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_set_Notes",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm"), self._client._types.string_type],
            None
        )

    def _return_type_notes(self) -> TypeBase:
        return self._client._types.string_type

    def _build_call_notes(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KerbalAlarmClock",
            "Alarm_get_Notes",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.string_type
        )

    @property
    def remaining(self) -> float:
        """
        The number of seconds until the alarm will fire.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_get_Remaining",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.double_type
        )

    def _return_type_remaining(self) -> TypeBase:
        return self._client._types.double_type

    def _build_call_remaining(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KerbalAlarmClock",
            "Alarm_get_Remaining",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.double_type
        )

    @property
    def repeat(self) -> bool:
        """
        Whether the alarm will be repeated after it has fired.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_get_Repeat",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.bool_type
        )

    @repeat.setter
    def repeat(self, value: bool) -> None:
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_set_Repeat",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm"), self._client._types.bool_type],
            None
        )

    def _return_type_repeat(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_repeat(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KerbalAlarmClock",
            "Alarm_get_Repeat",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.bool_type
        )

    @property
    def repeat_period(self) -> float:
        """
        The time delay to automatically create an alarm after it has fired.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_get_RepeatPeriod",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.double_type
        )

    @repeat_period.setter
    def repeat_period(self, value: float) -> None:
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_set_RepeatPeriod",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm"), self._client._types.double_type],
            None
        )

    def _return_type_repeat_period(self) -> TypeBase:
        return self._client._types.double_type

    def _build_call_repeat_period(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KerbalAlarmClock",
            "Alarm_get_RepeatPeriod",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.double_type
        )

    @property
    def time(self) -> float:
        """
        The time at which the alarm will fire.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_get_Time",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.double_type
        )

    @time.setter
    def time(self, value: float) -> None:
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_set_Time",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm"), self._client._types.double_type],
            None
        )

    def _return_type_time(self) -> TypeBase:
        return self._client._types.double_type

    def _build_call_time(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KerbalAlarmClock",
            "Alarm_get_Time",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.double_type
        )

    @property
    def type(self) -> AlarmType:
        """
        The type of the alarm.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_get_Type",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.enumeration_type("KerbalAlarmClock", "AlarmType")
        )

    def _return_type_type(self) -> TypeBase:
        return self._client._types.enumeration_type("KerbalAlarmClock", "AlarmType")

    def _build_call_type(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KerbalAlarmClock",
            "Alarm_get_Type",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.enumeration_type("KerbalAlarmClock", "AlarmType")
        )

    @property
    def vessel(self) -> spacecenter.Vessel:
        """
        The vessel that the alarm is attached to.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_get_Vessel",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.class_type("SpaceCenter", "Vessel")
        )

    @vessel.setter
    def vessel(self, value: spacecenter.Vessel) -> None:
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_set_Vessel",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm"), self._client._types.class_type("SpaceCenter", "Vessel")],
            None
        )

    def _return_type_vessel(self) -> TypeBase:
        return self._client._types.class_type("SpaceCenter", "Vessel")

    def _build_call_vessel(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KerbalAlarmClock",
            "Alarm_get_Vessel",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.class_type("SpaceCenter", "Vessel")
        )

    @property
    def xfer_origin_body(self) -> spacecenter.CelestialBody:
        """
        The celestial body the vessel is departing from.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_get_XferOriginBody",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.class_type("SpaceCenter", "CelestialBody")
        )

    @xfer_origin_body.setter
    def xfer_origin_body(self, value: spacecenter.CelestialBody) -> None:
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_set_XferOriginBody",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm"), self._client._types.class_type("SpaceCenter", "CelestialBody")],
            None
        )

    def _return_type_xfer_origin_body(self) -> TypeBase:
        return self._client._types.class_type("SpaceCenter", "CelestialBody")

    def _build_call_xfer_origin_body(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KerbalAlarmClock",
            "Alarm_get_XferOriginBody",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.class_type("SpaceCenter", "CelestialBody")
        )

    @property
    def xfer_target_body(self) -> spacecenter.CelestialBody:
        """
        The celestial body the vessel is arriving at.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_get_XferTargetBody",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.class_type("SpaceCenter", "CelestialBody")
        )

    @xfer_target_body.setter
    def xfer_target_body(self, value: spacecenter.CelestialBody) -> None:
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_set_XferTargetBody",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm"), self._client._types.class_type("SpaceCenter", "CelestialBody")],
            None
        )

    def _return_type_xfer_target_body(self) -> TypeBase:
        return self._client._types.class_type("SpaceCenter", "CelestialBody")

    def _build_call_xfer_target_body(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KerbalAlarmClock",
            "Alarm_get_XferTargetBody",
            [self],
            ["self"],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm")],
            self._client._types.class_type("SpaceCenter", "CelestialBody")
        )

    def remove(self) -> None:
        """
        Removes the alarm.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
            "Alarm_Remove",
            [self, ],
            ["self", ],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm"), ],
            None
        )

    def _return_type_remove(self) -> TypeBase:
        return None

    def _build_call_remove(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KerbalAlarmClock",
            "Alarm_Remove",
            [self, ],
            ["self", ],
            [self._client._types.class_type("KerbalAlarmClock", "Alarm"), ],
            None
        )



class KerbalAlarmClock:
    """
    This service provides functionality to interact with
    `Kerbal Alarm Clock <https://forum.kerbalspaceprogram.com/index.php?/topic/22809-13x-kerbal-alarm-clock-v3850-may-30/>`_.
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
        "Alarm": Alarm,
    }
    _enumerations = {
        "AlarmAction": AlarmAction,
        "AlarmType": AlarmType,
    }
    _exceptions = {
    }

    @property
    def alarms(self) -> List[Alarm]:
        """
        A list of all the alarms.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
            "get_Alarms",
            [],
            [],
            [],
            self._client._types.list_type(self._client._types.class_type("KerbalAlarmClock", "Alarm"))
        )

    def _return_type_alarms(self) -> TypeBase:
        return self._client._types.list_type(self._client._types.class_type("KerbalAlarmClock", "Alarm"))

    def _build_call_alarms(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KerbalAlarmClock",
            "get_Alarms",
            [],
            [],
            [],
            self._client._types.list_type(self._client._types.class_type("KerbalAlarmClock", "Alarm"))
        )

    @property
    def available(self) -> bool:
        """
        Whether Kerbal Alarm Clock is available.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
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
            "KerbalAlarmClock",
            "get_Available",
            [],
            [],
            [],
            self._client._types.bool_type
        )

    def alarm_with_name(self, name: str) -> Optional[Alarm]:
        """
        Get the alarm with the given name, or ``None``
        if no alarms have that name. If more than one alarm has the name,
        only returns one of them.

        :param name: Name of the alarm to search for.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
            "AlarmWithName",
            [name],
            ["name"],
            [self._client._types.string_type],
            self._client._types.class_type("KerbalAlarmClock", "Alarm")
        )

    def _return_type_alarm_with_name(self) -> TypeBase:
        return self._client._types.class_type("KerbalAlarmClock", "Alarm")

    def _build_call_alarm_with_name(self, name: str) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KerbalAlarmClock",
            "AlarmWithName",
            [name],
            ["name"],
            [self._client._types.string_type],
            self._client._types.class_type("KerbalAlarmClock", "Alarm")
        )

    def alarms_with_type(self, type: AlarmType) -> List[Alarm]:
        """
        Get a list of alarms of the specified type.

        :param type: Type of alarm to return.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
            "AlarmsWithType",
            [type],
            ["type"],
            [self._client._types.enumeration_type("KerbalAlarmClock", "AlarmType")],
            self._client._types.list_type(self._client._types.class_type("KerbalAlarmClock", "Alarm"))
        )

    def _return_type_alarms_with_type(self) -> TypeBase:
        return self._client._types.list_type(self._client._types.class_type("KerbalAlarmClock", "Alarm"))

    def _build_call_alarms_with_type(self, type: AlarmType) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KerbalAlarmClock",
            "AlarmsWithType",
            [type],
            ["type"],
            [self._client._types.enumeration_type("KerbalAlarmClock", "AlarmType")],
            self._client._types.list_type(self._client._types.class_type("KerbalAlarmClock", "Alarm"))
        )

    def create_alarm(self, type: AlarmType, name: str, ut: float) -> Alarm:
        """
        Create a new alarm and return it.

        :param type: Type of the new alarm.

        :param name: Name of the new alarm.

        :param ut: Time at which the new alarm should trigger.
        """
        return self._client._invoke(
            "KerbalAlarmClock",
            "CreateAlarm",
            [type, name, ut],
            ["type", "name", "ut"],
            [self._client._types.enumeration_type("KerbalAlarmClock", "AlarmType"), self._client._types.string_type, self._client._types.double_type],
            self._client._types.class_type("KerbalAlarmClock", "Alarm")
        )

    def _return_type_create_alarm(self) -> TypeBase:
        return self._client._types.class_type("KerbalAlarmClock", "Alarm")

    def _build_call_create_alarm(self, type: AlarmType, name: str, ut: float) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KerbalAlarmClock",
            "CreateAlarm",
            [type, name, ut],
            ["type", "name", "ut"],
            [self._client._types.enumeration_type("KerbalAlarmClock", "AlarmType"), self._client._types.string_type, self._client._types.double_type],
            self._client._types.class_type("KerbalAlarmClock", "Alarm")
        )
