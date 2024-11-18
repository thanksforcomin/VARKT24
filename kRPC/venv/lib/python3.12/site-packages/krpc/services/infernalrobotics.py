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


class Servo(ClassBase):
    """
    Represents a servo. Obtained using
    InfernalRobotics.ServoGroup#servos,
    InfernalRobotics.ServoGroup#servoWithName
    or InfernalRobotics#servoWithName.
    """
    @property
    def acceleration(self) -> float:
        """
        The current speed multiplier set in the UI.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_get_Acceleration",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.float_type
        )

    @acceleration.setter
    def acceleration(self, value: float) -> None:
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_set_Acceleration",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("InfernalRobotics", "Servo"), self._client._types.float_type],
            None
        )

    def _return_type_acceleration(self) -> TypeBase:
        return self._client._types.float_type

    def _build_call_acceleration(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_get_Acceleration",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.float_type
        )

    @property
    def config_speed(self) -> float:
        """
        The speed multiplier of the servo, specified by the part configuration.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_get_ConfigSpeed",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.float_type
        )

    def _return_type_config_speed(self) -> TypeBase:
        return self._client._types.float_type

    def _build_call_config_speed(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_get_ConfigSpeed",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.float_type
        )

    @property
    def current_speed(self) -> float:
        """
        The current speed at which the servo is moving.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_get_CurrentSpeed",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.float_type
        )

    def _return_type_current_speed(self) -> TypeBase:
        return self._client._types.float_type

    def _build_call_current_speed(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_get_CurrentSpeed",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.float_type
        )

    @property
    def highlight(self) -> bool:
        raise NotImplementedError

    @highlight.setter
    def highlight(self, value: bool) -> None:
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_set_Highlight",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("InfernalRobotics", "Servo"), self._client._types.bool_type],
            None
        )

    @property
    def is_axis_inverted(self) -> bool:
        """
        Whether the servos axis is inverted.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_get_IsAxisInverted",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.bool_type
        )

    @is_axis_inverted.setter
    def is_axis_inverted(self, value: bool) -> None:
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_set_IsAxisInverted",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("InfernalRobotics", "Servo"), self._client._types.bool_type],
            None
        )

    def _return_type_is_axis_inverted(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_is_axis_inverted(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_get_IsAxisInverted",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.bool_type
        )

    @property
    def is_free_moving(self) -> bool:
        """
        Whether the servo is freely moving.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_get_IsFreeMoving",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.bool_type
        )

    def _return_type_is_free_moving(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_is_free_moving(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_get_IsFreeMoving",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.bool_type
        )

    @property
    def is_locked(self) -> bool:
        """
        Whether the servo is locked.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_get_IsLocked",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.bool_type
        )

    @is_locked.setter
    def is_locked(self, value: bool) -> None:
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_set_IsLocked",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("InfernalRobotics", "Servo"), self._client._types.bool_type],
            None
        )

    def _return_type_is_locked(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_is_locked(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_get_IsLocked",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.bool_type
        )

    @property
    def is_moving(self) -> bool:
        """
        Whether the servo is moving.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_get_IsMoving",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.bool_type
        )

    def _return_type_is_moving(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_is_moving(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_get_IsMoving",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.bool_type
        )

    @property
    def max_config_position(self) -> float:
        """
        The maximum position of the servo, specified by the part configuration.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_get_MaxConfigPosition",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.float_type
        )

    def _return_type_max_config_position(self) -> TypeBase:
        return self._client._types.float_type

    def _build_call_max_config_position(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_get_MaxConfigPosition",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.float_type
        )

    @property
    def max_position(self) -> float:
        """
        The maximum position of the servo, specified by the in-game tweak menu.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_get_MaxPosition",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.float_type
        )

    @max_position.setter
    def max_position(self, value: float) -> None:
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_set_MaxPosition",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("InfernalRobotics", "Servo"), self._client._types.float_type],
            None
        )

    def _return_type_max_position(self) -> TypeBase:
        return self._client._types.float_type

    def _build_call_max_position(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_get_MaxPosition",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.float_type
        )

    @property
    def min_config_position(self) -> float:
        """
        The minimum position of the servo, specified by the part configuration.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_get_MinConfigPosition",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.float_type
        )

    def _return_type_min_config_position(self) -> TypeBase:
        return self._client._types.float_type

    def _build_call_min_config_position(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_get_MinConfigPosition",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.float_type
        )

    @property
    def min_position(self) -> float:
        """
        The minimum position of the servo, specified by the in-game tweak menu.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_get_MinPosition",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.float_type
        )

    @min_position.setter
    def min_position(self, value: float) -> None:
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_set_MinPosition",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("InfernalRobotics", "Servo"), self._client._types.float_type],
            None
        )

    def _return_type_min_position(self) -> TypeBase:
        return self._client._types.float_type

    def _build_call_min_position(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_get_MinPosition",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.float_type
        )

    @property
    def name(self) -> str:
        """
        The name of the servo.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_get_Name",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.string_type
        )

    @name.setter
    def name(self, value: str) -> None:
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_set_Name",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("InfernalRobotics", "Servo"), self._client._types.string_type],
            None
        )

    def _return_type_name(self) -> TypeBase:
        return self._client._types.string_type

    def _build_call_name(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_get_Name",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.string_type
        )

    @property
    def part(self) -> spacecenter.Part:
        """
        The part containing the servo.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_get_Part",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.class_type("SpaceCenter", "Part")
        )

    def _return_type_part(self) -> TypeBase:
        return self._client._types.class_type("SpaceCenter", "Part")

    def _build_call_part(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_get_Part",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.class_type("SpaceCenter", "Part")
        )

    @property
    def position(self) -> float:
        """
        The position of the servo.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_get_Position",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.float_type
        )

    def _return_type_position(self) -> TypeBase:
        return self._client._types.float_type

    def _build_call_position(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_get_Position",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.float_type
        )

    @property
    def speed(self) -> float:
        """
        The speed multiplier of the servo, specified by the in-game tweak menu.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_get_Speed",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.float_type
        )

    @speed.setter
    def speed(self, value: float) -> None:
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_set_Speed",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("InfernalRobotics", "Servo"), self._client._types.float_type],
            None
        )

    def _return_type_speed(self) -> TypeBase:
        return self._client._types.float_type

    def _build_call_speed(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_get_Speed",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "Servo")],
            self._client._types.float_type
        )

    def move_center(self) -> None:
        """
        Moves the servo to the center.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_MoveCenter",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "Servo"), ],
            None
        )

    def _return_type_move_center(self) -> TypeBase:
        return None

    def _build_call_move_center(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_MoveCenter",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "Servo"), ],
            None
        )

    def move_left(self) -> None:
        """
        Moves the servo to the left.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_MoveLeft",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "Servo"), ],
            None
        )

    def _return_type_move_left(self) -> TypeBase:
        return None

    def _build_call_move_left(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_MoveLeft",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "Servo"), ],
            None
        )

    def move_right(self) -> None:
        """
        Moves the servo to the right.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_MoveRight",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "Servo"), ],
            None
        )

    def _return_type_move_right(self) -> TypeBase:
        return None

    def _build_call_move_right(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_MoveRight",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "Servo"), ],
            None
        )

    def move_to(self, position: float, speed: float) -> None:
        """
        Moves the servo to position and sets the
        speed multiplier to speed.

        :param position: The position to move the servo to.

        :param speed: Speed multiplier for the movement.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_MoveTo",
            [self, position, speed],
            ["self", "position", "speed"],
            [self._client._types.class_type("InfernalRobotics", "Servo"), self._client._types.float_type, self._client._types.float_type],
            None
        )

    def _return_type_move_to(self) -> TypeBase:
        return None

    def _build_call_move_to(self, position: float, speed: float) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_MoveTo",
            [self, position, speed],
            ["self", "position", "speed"],
            [self._client._types.class_type("InfernalRobotics", "Servo"), self._client._types.float_type, self._client._types.float_type],
            None
        )

    def stop(self) -> None:
        """
        Stops the servo.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "Servo_Stop",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "Servo"), ],
            None
        )

    def _return_type_stop(self) -> TypeBase:
        return None

    def _build_call_stop(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "Servo_Stop",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "Servo"), ],
            None
        )



class ServoGroup(ClassBase):
    """
    A group of servos, obtained by calling InfernalRobotics#servoGroups
    or InfernalRobotics#servoGroupWithName. Represents the "Servo Groups"
    in the InfernalRobotics UI.
    """
    @property
    def expanded(self) -> bool:
        """
        Whether the group is expanded in the InfernalRobotics UI.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_get_Expanded",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup")],
            self._client._types.bool_type
        )

    @expanded.setter
    def expanded(self, value: bool) -> None:
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_set_Expanded",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), self._client._types.bool_type],
            None
        )

    def _return_type_expanded(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_expanded(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "ServoGroup_get_Expanded",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup")],
            self._client._types.bool_type
        )

    @property
    def forward_key(self) -> str:
        """
        The key assigned to be the "forward" key for the group.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_get_ForwardKey",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup")],
            self._client._types.string_type
        )

    @forward_key.setter
    def forward_key(self, value: str) -> None:
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_set_ForwardKey",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), self._client._types.string_type],
            None
        )

    def _return_type_forward_key(self) -> TypeBase:
        return self._client._types.string_type

    def _build_call_forward_key(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "ServoGroup_get_ForwardKey",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup")],
            self._client._types.string_type
        )

    @property
    def name(self) -> str:
        """
        The name of the group.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_get_Name",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup")],
            self._client._types.string_type
        )

    @name.setter
    def name(self, value: str) -> None:
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_set_Name",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), self._client._types.string_type],
            None
        )

    def _return_type_name(self) -> TypeBase:
        return self._client._types.string_type

    def _build_call_name(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "ServoGroup_get_Name",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup")],
            self._client._types.string_type
        )

    @property
    def parts(self) -> List[spacecenter.Part]:
        """
        The parts containing the servos in the group.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_get_Parts",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup")],
            self._client._types.list_type(self._client._types.class_type("SpaceCenter", "Part"))
        )

    def _return_type_parts(self) -> TypeBase:
        return self._client._types.list_type(self._client._types.class_type("SpaceCenter", "Part"))

    def _build_call_parts(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "ServoGroup_get_Parts",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup")],
            self._client._types.list_type(self._client._types.class_type("SpaceCenter", "Part"))
        )

    @property
    def reverse_key(self) -> str:
        """
        The key assigned to be the "reverse" key for the group.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_get_ReverseKey",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup")],
            self._client._types.string_type
        )

    @reverse_key.setter
    def reverse_key(self, value: str) -> None:
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_set_ReverseKey",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), self._client._types.string_type],
            None
        )

    def _return_type_reverse_key(self) -> TypeBase:
        return self._client._types.string_type

    def _build_call_reverse_key(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "ServoGroup_get_ReverseKey",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup")],
            self._client._types.string_type
        )

    @property
    def servos(self) -> List[Servo]:
        """
        The servos that are in the group.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_get_Servos",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup")],
            self._client._types.list_type(self._client._types.class_type("InfernalRobotics", "Servo"))
        )

    def _return_type_servos(self) -> TypeBase:
        return self._client._types.list_type(self._client._types.class_type("InfernalRobotics", "Servo"))

    def _build_call_servos(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "ServoGroup_get_Servos",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup")],
            self._client._types.list_type(self._client._types.class_type("InfernalRobotics", "Servo"))
        )

    @property
    def speed(self) -> float:
        """
        The speed multiplier for the group.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_get_Speed",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup")],
            self._client._types.float_type
        )

    @speed.setter
    def speed(self, value: float) -> None:
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_set_Speed",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), self._client._types.float_type],
            None
        )

    def _return_type_speed(self) -> TypeBase:
        return self._client._types.float_type

    def _build_call_speed(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "ServoGroup_get_Speed",
            [self],
            ["self"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup")],
            self._client._types.float_type
        )

    def move_center(self) -> None:
        """
        Moves all of the servos in the group to the center.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_MoveCenter",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), ],
            None
        )

    def _return_type_move_center(self) -> TypeBase:
        return None

    def _build_call_move_center(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "ServoGroup_MoveCenter",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), ],
            None
        )

    def move_left(self) -> None:
        """
        Moves all of the servos in the group to the left.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_MoveLeft",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), ],
            None
        )

    def _return_type_move_left(self) -> TypeBase:
        return None

    def _build_call_move_left(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "ServoGroup_MoveLeft",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), ],
            None
        )

    def move_next_preset(self) -> None:
        """
        Moves all of the servos in the group to the next preset.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_MoveNextPreset",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), ],
            None
        )

    def _return_type_move_next_preset(self) -> TypeBase:
        return None

    def _build_call_move_next_preset(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "ServoGroup_MoveNextPreset",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), ],
            None
        )

    def move_prev_preset(self) -> None:
        """
        Moves all of the servos in the group to the previous preset.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_MovePrevPreset",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), ],
            None
        )

    def _return_type_move_prev_preset(self) -> TypeBase:
        return None

    def _build_call_move_prev_preset(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "ServoGroup_MovePrevPreset",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), ],
            None
        )

    def move_right(self) -> None:
        """
        Moves all of the servos in the group to the right.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_MoveRight",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), ],
            None
        )

    def _return_type_move_right(self) -> TypeBase:
        return None

    def _build_call_move_right(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "ServoGroup_MoveRight",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), ],
            None
        )

    def servo_with_name(self, name: str) -> Optional[Servo]:
        """
        Returns the servo with the given name from this group,
        or ``None`` if none exists.

        :param name: Name of servo to find.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_ServoWithName",
            [self, name],
            ["self", "name"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), self._client._types.string_type],
            self._client._types.class_type("InfernalRobotics", "Servo")
        )

    def _return_type_servo_with_name(self) -> TypeBase:
        return self._client._types.class_type("InfernalRobotics", "Servo")

    def _build_call_servo_with_name(self, name: str) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "ServoGroup_ServoWithName",
            [self, name],
            ["self", "name"],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), self._client._types.string_type],
            self._client._types.class_type("InfernalRobotics", "Servo")
        )

    def stop(self) -> None:
        """
        Stops the servos in the group.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroup_Stop",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), ],
            None
        )

    def _return_type_stop(self) -> TypeBase:
        return None

    def _build_call_stop(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "ServoGroup_Stop",
            [self, ],
            ["self", ],
            [self._client._types.class_type("InfernalRobotics", "ServoGroup"), ],
            None
        )



class InfernalRobotics:
    """
    This service provides functionality to interact with
    `Infernal Robotics <https://forum.kerbalspaceprogram.com/index.php?/topic/184787-infernal-robotics-next/>`_.
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
        "Servo": Servo,
        "ServoGroup": ServoGroup,
    }
    _enumerations = {
    }
    _exceptions = {
    }

    @property
    def available(self) -> bool:
        """
        Whether Infernal Robotics is installed.
        """
        return self._client._invoke(
            "InfernalRobotics",
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
            "InfernalRobotics",
            "get_Available",
            [],
            [],
            [],
            self._client._types.bool_type
        )

    @property
    def ready(self) -> bool:
        """
        Whether Infernal Robotics API is ready.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "get_Ready",
            [],
            [],
            [],
            self._client._types.bool_type
        )

    def _return_type_ready(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_ready(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "get_Ready",
            [],
            [],
            [],
            self._client._types.bool_type
        )

    def servo_group_with_name(self, vessel: spacecenter.Vessel, name: str) -> Optional[ServoGroup]:
        """
        Returns the servo group in the given vessel with the given name,
        or ``None`` if none exists. If multiple servo groups have the same name, only one of them is returned.

        :param vessel: Vessel to check.

        :param name: Name of servo group to find.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroupWithName",
            [vessel, name],
            ["vessel", "name"],
            [self._client._types.class_type("SpaceCenter", "Vessel"), self._client._types.string_type],
            self._client._types.class_type("InfernalRobotics", "ServoGroup")
        )

    def _return_type_servo_group_with_name(self) -> TypeBase:
        return self._client._types.class_type("InfernalRobotics", "ServoGroup")

    def _build_call_servo_group_with_name(self, vessel: spacecenter.Vessel, name: str) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "ServoGroupWithName",
            [vessel, name],
            ["vessel", "name"],
            [self._client._types.class_type("SpaceCenter", "Vessel"), self._client._types.string_type],
            self._client._types.class_type("InfernalRobotics", "ServoGroup")
        )

    def servo_groups(self, vessel: spacecenter.Vessel) -> List[ServoGroup]:
        """
        A list of all the servo groups in the given vessel.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "ServoGroups",
            [vessel],
            ["vessel"],
            [self._client._types.class_type("SpaceCenter", "Vessel")],
            self._client._types.list_type(self._client._types.class_type("InfernalRobotics", "ServoGroup"))
        )

    def _return_type_servo_groups(self) -> TypeBase:
        return self._client._types.list_type(self._client._types.class_type("InfernalRobotics", "ServoGroup"))

    def _build_call_servo_groups(self, vessel: spacecenter.Vessel) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "ServoGroups",
            [vessel],
            ["vessel"],
            [self._client._types.class_type("SpaceCenter", "Vessel")],
            self._client._types.list_type(self._client._types.class_type("InfernalRobotics", "ServoGroup"))
        )

    def servo_with_name(self, vessel: spacecenter.Vessel, name: str) -> Optional[Servo]:
        """
        Returns the servo in the given vessel with the given name or
        ``None`` if none exists. If multiple servos have the same name, only one of them is returned.

        :param vessel: Vessel to check.

        :param name: Name of the servo to find.
        """
        return self._client._invoke(
            "InfernalRobotics",
            "ServoWithName",
            [vessel, name],
            ["vessel", "name"],
            [self._client._types.class_type("SpaceCenter", "Vessel"), self._client._types.string_type],
            self._client._types.class_type("InfernalRobotics", "Servo")
        )

    def _return_type_servo_with_name(self) -> TypeBase:
        return self._client._types.class_type("InfernalRobotics", "Servo")

    def _build_call_servo_with_name(self, vessel: spacecenter.Vessel, name: str) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "InfernalRobotics",
            "ServoWithName",
            [vessel, name],
            ["vessel", "name"],
            [self._client._types.class_type("SpaceCenter", "Vessel"), self._client._types.string_type],
            self._client._types.class_type("InfernalRobotics", "Servo")
        )
