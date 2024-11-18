# pylint: disable=line-too-long,invalid-name,redefined-builtin,too-many-lines
from __future__ import annotations
from typing import Tuple, Set, Dict, List, Optional, TYPE_CHECKING
import krpc.schema
from krpc.schema import KRPC_pb2
from krpc.types import TypeBase, ClassBase, WrappedClass, DocEnum
from krpc.event import Event
if TYPE_CHECKING:
    from krpc.services import Client


class GameScene(DocEnum):
    """
    The game scene. See KRPC#currentGameScene.
    """
    space_center = 0, """
The game scene showing the Kerbal Space Center buildings.
"""
    flight = 1, """
The game scene showing a vessel in flight (or on the launchpad/runway).
"""
    tracking_station = 2, """
The tracking station.
"""
    editor_vab = 3, """
The Vehicle Assembly Building.
"""
    editor_sph = 4, """
The Space Plane Hangar.
"""


class ArgumentException(RuntimeError):
    """
    A method was invoked where at least one of the passed arguments does not
    meet the parameter specification of the method.
    """
    pass


class ArgumentNullException(RuntimeError):
    """
    A null reference was passed to a method that does not accept it as a valid argument.
    """
    pass


class ArgumentOutOfRangeException(RuntimeError):
    """
    The value of an argument is outside the allowable range of values as defined by the invoked method.
    """
    pass


class InvalidOperationException(RuntimeError):
    """
    A method call was made to a method that is invalid
    given the current state of the object.
    """
    pass


class Expression(ClassBase):
    """
    A server side expression.
    """
    @classmethod
    def add(cls, arg0: Expression, arg1: Expression) -> Expression:
        """
        Numerical addition.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Add",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_add(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_add(cls, arg0: Expression, arg1: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Add",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def aggregate(cls, arg: Expression, func: Expression) -> Expression:
        """
        Applies an accumulator function over a sequence.

        :returns: The accumulated value.

        :param arg: The collection.

        :param func: The accumulator function.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Aggregate",
            [arg, func],
            ["arg", "func"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_aggregate(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_aggregate(cls, arg: Expression, func: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Aggregate",
            [arg, func],
            ["arg", "func"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def aggregate_with_seed(cls, arg: Expression, seed: Expression, func: Expression) -> Expression:
        """
        Applies an accumulator function over a sequence, with a given seed.

        :returns: The accumulated value.

        :param arg: The collection.

        :param seed: The seed value.

        :param func: The accumulator function.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_AggregateWithSeed",
            [arg, seed, func],
            ["arg", "seed", "func"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_aggregate_with_seed(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_aggregate_with_seed(cls, arg: Expression, seed: Expression, func: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_AggregateWithSeed",
            [arg, seed, func],
            ["arg", "seed", "func"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def all(cls, arg: Expression, predicate: Expression) -> Expression:
        """
        Determine whether all items in a collection satisfy a boolean predicate.

        :returns: Whether all items satisfy the predicate.

        :param arg: The collection.

        :param predicate: The predicate function.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_All",
            [arg, predicate],
            ["arg", "predicate"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_all(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_all(cls, arg: Expression, predicate: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_All",
            [arg, predicate],
            ["arg", "predicate"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def and_(cls, arg0: Expression, arg1: Expression) -> Expression:
        """
        Boolean and operator.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_And",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_and_(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_and_(cls, arg0: Expression, arg1: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_And",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def any(cls, arg: Expression, predicate: Expression) -> Expression:
        """
        Determine whether any item in a collection satisfies a boolean predicate.

        :returns: Whether any item satisfies the predicate.

        :param arg: The collection.

        :param predicate: The predicate function.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Any",
            [arg, predicate],
            ["arg", "predicate"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_any(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_any(cls, arg: Expression, predicate: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Any",
            [arg, predicate],
            ["arg", "predicate"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def average(cls, arg: Expression) -> Expression:
        """
        Minimum of all elements in a collection.

        :returns: The minimum elements in the collection.

        :param arg: The list or set.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Average",
            [arg],
            ["arg"],
            [self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_average(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_average(cls, arg: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Average",
            [arg],
            ["arg"],
            [self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def call(cls, call: KRPC_pb2.ProcedureCall) -> Expression:
        """
        An RPC call.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Call",
            [call],
            ["call"],
            [self._client._types.procedure_call_type],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_call(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_call(cls, call: KRPC_pb2.ProcedureCall) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Call",
            [call],
            ["call"],
            [self._client._types.procedure_call_type],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def cast(cls, arg: Expression, type: Type) -> Expression:
        """
        Perform a cast to the given type.

        :param type: Type to cast the argument to.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Cast",
            [arg, type],
            ["arg", "type"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Type")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_cast(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_cast(cls, arg: Expression, type: Type) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Cast",
            [arg, type],
            ["arg", "type"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Type")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def concat(cls, arg1: Expression, arg2: Expression) -> Expression:
        """
        Concatenate two sequences.

        :returns: The first sequence followed by the second sequence.

        :param arg1: The first sequence.

        :param arg2: The second sequence.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Concat",
            [arg1, arg2],
            ["arg1", "arg2"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_concat(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_concat(cls, arg1: Expression, arg2: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Concat",
            [arg1, arg2],
            ["arg1", "arg2"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def constant_bool(cls, value: bool) -> Expression:
        """
        A constant value of boolean type.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_ConstantBool",
            [value],
            ["value"],
            [self._client._types.bool_type],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_constant_bool(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_constant_bool(cls, value: bool) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_ConstantBool",
            [value],
            ["value"],
            [self._client._types.bool_type],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def constant_double(cls, value: float) -> Expression:
        """
        A constant value of double precision floating point type.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_ConstantDouble",
            [value],
            ["value"],
            [self._client._types.double_type],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_constant_double(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_constant_double(cls, value: float) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_ConstantDouble",
            [value],
            ["value"],
            [self._client._types.double_type],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def constant_float(cls, value: float) -> Expression:
        """
        A constant value of single precision floating point type.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_ConstantFloat",
            [value],
            ["value"],
            [self._client._types.float_type],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_constant_float(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_constant_float(cls, value: float) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_ConstantFloat",
            [value],
            ["value"],
            [self._client._types.float_type],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def constant_int(cls, value: int) -> Expression:
        """
        A constant value of integer type.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_ConstantInt",
            [value],
            ["value"],
            [self._client._types.sint32_type],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_constant_int(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_constant_int(cls, value: int) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_ConstantInt",
            [value],
            ["value"],
            [self._client._types.sint32_type],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def constant_string(cls, value: str) -> Expression:
        """
        A constant value of string type.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_ConstantString",
            [value],
            ["value"],
            [self._client._types.string_type],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_constant_string(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_constant_string(cls, value: str) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_ConstantString",
            [value],
            ["value"],
            [self._client._types.string_type],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def contains(cls, arg: Expression, value: Expression) -> Expression:
        """
        Determine if a collection contains a value.

        :returns: Whether the collection contains a value.

        :param arg: The collection.

        :param value: The value to look for.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Contains",
            [arg, value],
            ["arg", "value"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_contains(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_contains(cls, arg: Expression, value: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Contains",
            [arg, value],
            ["arg", "value"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def count(cls, arg: Expression) -> Expression:
        """
        Number of elements in a collection.

        :returns: The number of elements in the collection.

        :param arg: The list, set or dictionary.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Count",
            [arg],
            ["arg"],
            [self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_count(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_count(cls, arg: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Count",
            [arg],
            ["arg"],
            [self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def create_dictionary(cls, keys: List[Expression], values: List[Expression]) -> Expression:
        """
        Construct a dictionary, from a list of corresponding keys and values.

        :returns: The dictionary.

        :param keys: The keys. Should all be of the same type.

        :param values: The values. Should all be of the same type.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_CreateDictionary",
            [keys, values],
            ["keys", "values"],
            [self._client._types.list_type(self._client._types.class_type("KRPC", "Expression")), self._client._types.list_type(self._client._types.class_type("KRPC", "Expression"))],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_create_dictionary(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_create_dictionary(cls, keys: List[Expression], values: List[Expression]) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_CreateDictionary",
            [keys, values],
            ["keys", "values"],
            [self._client._types.list_type(self._client._types.class_type("KRPC", "Expression")), self._client._types.list_type(self._client._types.class_type("KRPC", "Expression"))],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def create_list(cls, values: List[Expression]) -> Expression:
        """
        Construct a list.

        :returns: The list.

        :param values: The value. Should all be of the same type.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_CreateList",
            [values],
            ["values"],
            [self._client._types.list_type(self._client._types.class_type("KRPC", "Expression"))],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_create_list(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_create_list(cls, values: List[Expression]) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_CreateList",
            [values],
            ["values"],
            [self._client._types.list_type(self._client._types.class_type("KRPC", "Expression"))],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def create_set(cls, values: Set[Expression]) -> Expression:
        """
        Construct a set.

        :returns: The set.

        :param values: The values. Should all be of the same type.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_CreateSet",
            [values],
            ["values"],
            [self._client._types.set_type(self._client._types.class_type("KRPC", "Expression"))],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_create_set(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_create_set(cls, values: Set[Expression]) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_CreateSet",
            [values],
            ["values"],
            [self._client._types.set_type(self._client._types.class_type("KRPC", "Expression"))],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def create_tuple(cls, elements: List[Expression]) -> Expression:
        """
        Construct a tuple.

        :returns: The tuple.

        :param elements: The elements.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_CreateTuple",
            [elements],
            ["elements"],
            [self._client._types.list_type(self._client._types.class_type("KRPC", "Expression"))],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_create_tuple(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_create_tuple(cls, elements: List[Expression]) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_CreateTuple",
            [elements],
            ["elements"],
            [self._client._types.list_type(self._client._types.class_type("KRPC", "Expression"))],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def divide(cls, arg0: Expression, arg1: Expression) -> Expression:
        """
        Numerical division.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Divide",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_divide(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_divide(cls, arg0: Expression, arg1: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Divide",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def equal(cls, arg0: Expression, arg1: Expression) -> Expression:
        """
        Equality comparison.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Equal",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_equal(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_equal(cls, arg0: Expression, arg1: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Equal",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def exclusive_or(cls, arg0: Expression, arg1: Expression) -> Expression:
        """
        Boolean exclusive-or operator.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_ExclusiveOr",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_exclusive_or(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_exclusive_or(cls, arg0: Expression, arg1: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_ExclusiveOr",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def function(cls, parameters: List[Expression], body: Expression) -> Expression:
        """
        A function.

        :returns: A function.

        :param parameters: The parameters of the function.

        :param body: The body of the function.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Function",
            [parameters, body],
            ["parameters", "body"],
            [self._client._types.list_type(self._client._types.class_type("KRPC", "Expression")), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_function(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_function(cls, parameters: List[Expression], body: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Function",
            [parameters, body],
            ["parameters", "body"],
            [self._client._types.list_type(self._client._types.class_type("KRPC", "Expression")), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def get(cls, arg: Expression, index: Expression) -> Expression:
        """
        Access an element in a tuple, list or dictionary.

        :returns: The element.

        :param arg: The tuple, list or dictionary.

        :param index: The index of the element to access.
                      A zero indexed integer for a tuple or list, or a key for a dictionary.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Get",
            [arg, index],
            ["arg", "index"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_get(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_get(cls, arg: Expression, index: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Get",
            [arg, index],
            ["arg", "index"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def greater_than(cls, arg0: Expression, arg1: Expression) -> Expression:
        """
        Greater than numerical comparison.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_GreaterThan",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_greater_than(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_greater_than(cls, arg0: Expression, arg1: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_GreaterThan",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def greater_than_or_equal(cls, arg0: Expression, arg1: Expression) -> Expression:
        """
        Greater than or equal numerical comparison.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_GreaterThanOrEqual",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_greater_than_or_equal(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_greater_than_or_equal(cls, arg0: Expression, arg1: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_GreaterThanOrEqual",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def invoke(cls, function: Expression, args: Dict[str, Expression]) -> Expression:
        """
        A function call.

        :returns: A function call.

        :param function: The function to call.

        :param args: The arguments to call the function with.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Invoke",
            [function, args],
            ["function", "args"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.dictionary_type(self._client._types.string_type, self._client._types.class_type("KRPC", "Expression"))],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_invoke(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_invoke(cls, function: Expression, args: Dict[str, Expression]) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Invoke",
            [function, args],
            ["function", "args"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.dictionary_type(self._client._types.string_type, self._client._types.class_type("KRPC", "Expression"))],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def left_shift(cls, arg0: Expression, arg1: Expression) -> Expression:
        """
        Bitwise left shift.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_LeftShift",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_left_shift(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_left_shift(cls, arg0: Expression, arg1: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_LeftShift",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def less_than(cls, arg0: Expression, arg1: Expression) -> Expression:
        """
        Less than numerical comparison.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_LessThan",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_less_than(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_less_than(cls, arg0: Expression, arg1: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_LessThan",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def less_than_or_equal(cls, arg0: Expression, arg1: Expression) -> Expression:
        """
        Less than or equal numerical comparison.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_LessThanOrEqual",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_less_than_or_equal(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_less_than_or_equal(cls, arg0: Expression, arg1: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_LessThanOrEqual",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def max(cls, arg: Expression) -> Expression:
        """
        Maximum of all elements in a collection.

        :returns: The maximum elements in the collection.

        :param arg: The list or set.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Max",
            [arg],
            ["arg"],
            [self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_max(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_max(cls, arg: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Max",
            [arg],
            ["arg"],
            [self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def min(cls, arg: Expression) -> Expression:
        """
        Minimum of all elements in a collection.

        :returns: The minimum elements in the collection.

        :param arg: The list or set.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Min",
            [arg],
            ["arg"],
            [self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_min(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_min(cls, arg: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Min",
            [arg],
            ["arg"],
            [self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def modulo(cls, arg0: Expression, arg1: Expression) -> Expression:
        """
        Numerical modulo operator.

        :returns: The remainder of arg0 divided by arg1
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Modulo",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_modulo(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_modulo(cls, arg0: Expression, arg1: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Modulo",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def multiply(cls, arg0: Expression, arg1: Expression) -> Expression:
        """
        Numerical multiplication.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Multiply",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_multiply(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_multiply(cls, arg0: Expression, arg1: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Multiply",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def not_(cls, arg: Expression) -> Expression:
        """
        Boolean negation operator.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Not",
            [arg],
            ["arg"],
            [self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_not_(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_not_(cls, arg: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Not",
            [arg],
            ["arg"],
            [self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def not_equal(cls, arg0: Expression, arg1: Expression) -> Expression:
        """
        Inequality comparison.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_NotEqual",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_not_equal(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_not_equal(cls, arg0: Expression, arg1: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_NotEqual",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def or_(cls, arg0: Expression, arg1: Expression) -> Expression:
        """
        Boolean or operator.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Or",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_or_(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_or_(cls, arg0: Expression, arg1: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Or",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def order_by(cls, arg: Expression, key: Expression) -> Expression:
        """
        Order a collection using a key function.

        :returns: The ordered collection.

        :param arg: The collection to order.

        :param key: A function that takes a value from the collection and generates a key to sort on.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_OrderBy",
            [arg, key],
            ["arg", "key"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_order_by(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_order_by(cls, arg: Expression, key: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_OrderBy",
            [arg, key],
            ["arg", "key"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def parameter(cls, name: str, type: Type) -> Expression:
        """
        A named parameter of type double.

        :returns: A named parameter.

        :param name: The name of the parameter.

        :param type: The type of the parameter.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Parameter",
            [name, type],
            ["name", "type"],
            [self._client._types.string_type, self._client._types.class_type("KRPC", "Type")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_parameter(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_parameter(cls, name: str, type: Type) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Parameter",
            [name, type],
            ["name", "type"],
            [self._client._types.string_type, self._client._types.class_type("KRPC", "Type")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def power(cls, arg0: Expression, arg1: Expression) -> Expression:
        """
        Numerical power operator.

        :returns: arg0 raised to the power of arg1, with type of arg0
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Power",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_power(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_power(cls, arg0: Expression, arg1: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Power",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def right_shift(cls, arg0: Expression, arg1: Expression) -> Expression:
        """
        Bitwise right shift.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_RightShift",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_right_shift(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_right_shift(cls, arg0: Expression, arg1: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_RightShift",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def select(cls, arg: Expression, func: Expression) -> Expression:
        """
        Run a function on every element in the collection.

        :returns: The modified collection.

        :param arg: The list or set.

        :param func: The function.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Select",
            [arg, func],
            ["arg", "func"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_select(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_select(cls, arg: Expression, func: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Select",
            [arg, func],
            ["arg", "func"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def subtract(cls, arg0: Expression, arg1: Expression) -> Expression:
        """
        Numerical subtraction.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Subtract",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_subtract(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_subtract(cls, arg0: Expression, arg1: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Subtract",
            [arg0, arg1],
            ["arg0", "arg1"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def sum(cls, arg: Expression) -> Expression:
        """
        Sum all elements of a collection.

        :returns: The sum of the elements in the collection.

        :param arg: The list or set.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Sum",
            [arg],
            ["arg"],
            [self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_sum(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_sum(cls, arg: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Sum",
            [arg],
            ["arg"],
            [self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def to_list(cls, arg: Expression) -> Expression:
        """
        Convert a collection to a list.

        :returns: The collection as a list.

        :param arg: The collection.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_ToList",
            [arg],
            ["arg"],
            [self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_to_list(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_to_list(cls, arg: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_ToList",
            [arg],
            ["arg"],
            [self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def to_set(cls, arg: Expression) -> Expression:
        """
        Convert a collection to a set.

        :returns: The collection as a set.

        :param arg: The collection.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_ToSet",
            [arg],
            ["arg"],
            [self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_to_set(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_to_set(cls, arg: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_ToSet",
            [arg],
            ["arg"],
            [self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def where(cls, arg: Expression, func: Expression) -> Expression:
        """
        Run a function on every element in the collection.

        :returns: The modified collection.

        :param arg: The list or set.

        :param func: The function.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Expression_static_Where",
            [arg, func],
            ["arg", "func"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )

    @classmethod
    def _return_type_where(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Expression")

    @classmethod
    def _build_call_where(cls, arg: Expression, func: Expression) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Expression_static_Where",
            [arg, func],
            ["arg", "func"],
            [self._client._types.class_type("KRPC", "Expression"), self._client._types.class_type("KRPC", "Expression")],
            self._client._types.class_type("KRPC", "Expression")
        )



class Type(ClassBase):
    """
    A server side expression.
    """
    @classmethod
    def bool(cls, ) -> Type:
        """
        Bool type.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Type_static_Bool",
            [],
            [],
            [],
            self._client._types.class_type("KRPC", "Type")
        )

    @classmethod
    def _return_type_bool(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Type")

    @classmethod
    def _build_call_bool(cls, ) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Type_static_Bool",
            [],
            [],
            [],
            self._client._types.class_type("KRPC", "Type")
        )

    @classmethod
    def double(cls, ) -> Type:
        """
        Double type.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Type_static_Double",
            [],
            [],
            [],
            self._client._types.class_type("KRPC", "Type")
        )

    @classmethod
    def _return_type_double(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Type")

    @classmethod
    def _build_call_double(cls, ) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Type_static_Double",
            [],
            [],
            [],
            self._client._types.class_type("KRPC", "Type")
        )

    @classmethod
    def float(cls, ) -> Type:
        """
        Float type.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Type_static_Float",
            [],
            [],
            [],
            self._client._types.class_type("KRPC", "Type")
        )

    @classmethod
    def _return_type_float(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Type")

    @classmethod
    def _build_call_float(cls, ) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Type_static_Float",
            [],
            [],
            [],
            self._client._types.class_type("KRPC", "Type")
        )

    @classmethod
    def int(cls, ) -> Type:
        """
        Int type.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Type_static_Int",
            [],
            [],
            [],
            self._client._types.class_type("KRPC", "Type")
        )

    @classmethod
    def _return_type_int(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Type")

    @classmethod
    def _build_call_int(cls, ) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Type_static_Int",
            [],
            [],
            [],
            self._client._types.class_type("KRPC", "Type")
        )

    @classmethod
    def string(cls, ) -> Type:
        """
        String type.
        """
        self = cls
        return cls._client._invoke(
            "KRPC",
            "Type_static_String",
            [],
            [],
            [],
            self._client._types.class_type("KRPC", "Type")
        )

    @classmethod
    def _return_type_string(cls) -> TypeBase:
        self = cls
        return self._client._types.class_type("KRPC", "Type")

    @classmethod
    def _build_call_string(cls, ) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "KRPC",
            "Type_static_String",
            [],
            [],
            [],
            self._client._types.class_type("KRPC", "Type")
        )



class KRPC:
    """
    Main kRPC service, used by clients to interact with basic server functionality.
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
        "Expression": Expression,
        "Type": Type,
    }
    _enumerations = {
        "GameScene": GameScene,
    }
    _exceptions = {
        "ArgumentException": ArgumentException,
        "ArgumentNullException": ArgumentNullException,
        "ArgumentOutOfRangeException": ArgumentOutOfRangeException,
        "InvalidOperationException": InvalidOperationException,
    }

    @property
    def clients(self) -> List[Tuple[bytes,str,str]]:
        """
        A list of RPC clients that are currently connected to the server.
        Each entry in the list is a clients identifier, name and address.
        """
        return self._client._invoke(
            "KRPC",
            "get_Clients",
            [],
            [],
            [],
            self._client._types.list_type(self._client._types.tuple_type(self._client._types.bytes_type, self._client._types.string_type, self._client._types.string_type))
        )

    def _return_type_clients(self) -> TypeBase:
        return self._client._types.list_type(self._client._types.tuple_type(self._client._types.bytes_type, self._client._types.string_type, self._client._types.string_type))

    def _build_call_clients(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KRPC",
            "get_Clients",
            [],
            [],
            [],
            self._client._types.list_type(self._client._types.tuple_type(self._client._types.bytes_type, self._client._types.string_type, self._client._types.string_type))
        )

    @property
    def current_game_scene(self) -> GameScene:
        """
        Get the current game scene.
        """
        return self._client._invoke(
            "KRPC",
            "get_CurrentGameScene",
            [],
            [],
            [],
            self._client._types.enumeration_type("KRPC", "GameScene")
        )

    def _return_type_current_game_scene(self) -> TypeBase:
        return self._client._types.enumeration_type("KRPC", "GameScene")

    def _build_call_current_game_scene(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KRPC",
            "get_CurrentGameScene",
            [],
            [],
            [],
            self._client._types.enumeration_type("KRPC", "GameScene")
        )

    @property
    def paused(self) -> bool:
        """
        Whether the game is paused.
        """
        return self._client._invoke(
            "KRPC",
            "get_Paused",
            [],
            [],
            [],
            self._client._types.bool_type
        )

    @paused.setter
    def paused(self, value: bool) -> None:
        return self._client._invoke(
            "KRPC",
            "set_Paused",
            [value],
            ["value"],
            [self._client._types.bool_type],
            None
        )

    def _return_type_paused(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_paused(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KRPC",
            "get_Paused",
            [],
            [],
            [],
            self._client._types.bool_type
        )

    def add_event(self, expression: Expression) -> Event:
        """
        Create an event from a server side expression.
        """
        return self._client._invoke(
            "KRPC",
            "AddEvent",
            [expression],
            ["expression"],
            [self._client._types.class_type("KRPC", "Expression")],
            self._client._types.event_type
        )

    def _return_type_add_event(self) -> TypeBase:
        return self._client._types.event_type

    def _build_call_add_event(self, expression: Expression) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KRPC",
            "AddEvent",
            [expression],
            ["expression"],
            [self._client._types.class_type("KRPC", "Expression")],
            self._client._types.event_type
        )

    def add_stream(self, call: KRPC_pb2.ProcedureCall, start: bool = True) -> KRPC_pb2.Stream:
        """
        Add a streaming request and return its identifier.
        """
        return self._client._invoke(
            "KRPC",
            "AddStream",
            [call, start],
            ["call", "start"],
            [self._client._types.procedure_call_type, self._client._types.bool_type],
            self._client._types.stream_type
        )

    def _return_type_add_stream(self) -> TypeBase:
        return self._client._types.stream_type

    def _build_call_add_stream(self, call: KRPC_pb2.ProcedureCall, start: bool = True) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KRPC",
            "AddStream",
            [call, start],
            ["call", "start"],
            [self._client._types.procedure_call_type, self._client._types.bool_type],
            self._client._types.stream_type
        )

    def get_client_id(self) -> bytes:
        """
        Returns the identifier for the current client.
        """
        return self._client._invoke(
            "KRPC",
            "GetClientID",
            [],
            [],
            [],
            self._client._types.bytes_type
        )

    def _return_type_get_client_id(self) -> TypeBase:
        return self._client._types.bytes_type

    def _build_call_get_client_id(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KRPC",
            "GetClientID",
            [],
            [],
            [],
            self._client._types.bytes_type
        )

    def get_client_name(self) -> str:
        """
        Returns the name of the current client.
        This is an empty string if the client has no name.
        """
        return self._client._invoke(
            "KRPC",
            "GetClientName",
            [],
            [],
            [],
            self._client._types.string_type
        )

    def _return_type_get_client_name(self) -> TypeBase:
        return self._client._types.string_type

    def _build_call_get_client_name(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KRPC",
            "GetClientName",
            [],
            [],
            [],
            self._client._types.string_type
        )

    def get_services(self) -> KRPC_pb2.Services:
        """
        Returns information on all services, procedures, classes, properties etc. provided by the server.
        Can be used by client libraries to automatically create functionality such as stubs.
        """
        return self._client._invoke(
            "KRPC",
            "GetServices",
            [],
            [],
            [],
            self._client._types.services_type
        )

    def _return_type_get_services(self) -> TypeBase:
        return self._client._types.services_type

    def _build_call_get_services(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KRPC",
            "GetServices",
            [],
            [],
            [],
            self._client._types.services_type
        )

    def get_status(self) -> KRPC_pb2.Status:
        """
        Returns some information about the server, such as the version.
        """
        return self._client._invoke(
            "KRPC",
            "GetStatus",
            [],
            [],
            [],
            self._client._types.status_type
        )

    def _return_type_get_status(self) -> TypeBase:
        return self._client._types.status_type

    def _build_call_get_status(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KRPC",
            "GetStatus",
            [],
            [],
            [],
            self._client._types.status_type
        )

    def remove_stream(self, id: int) -> None:
        """
        Remove a streaming request.
        """
        return self._client._invoke(
            "KRPC",
            "RemoveStream",
            [id],
            ["id"],
            [self._client._types.uint64_type],
            None
        )

    def _return_type_remove_stream(self) -> TypeBase:
        return None

    def _build_call_remove_stream(self, id: int) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KRPC",
            "RemoveStream",
            [id],
            ["id"],
            [self._client._types.uint64_type],
            None
        )

    def set_stream_rate(self, id: int, rate: float) -> None:
        """
        Set the update rate for a stream in Hz.
        """
        return self._client._invoke(
            "KRPC",
            "SetStreamRate",
            [id, rate],
            ["id", "rate"],
            [self._client._types.uint64_type, self._client._types.float_type],
            None
        )

    def _return_type_set_stream_rate(self) -> TypeBase:
        return None

    def _build_call_set_stream_rate(self, id: int, rate: float) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KRPC",
            "SetStreamRate",
            [id, rate],
            ["id", "rate"],
            [self._client._types.uint64_type, self._client._types.float_type],
            None
        )

    def start_stream(self, id: int) -> None:
        """
        Start a previously added streaming request.
        """
        return self._client._invoke(
            "KRPC",
            "StartStream",
            [id],
            ["id"],
            [self._client._types.uint64_type],
            None
        )

    def _return_type_start_stream(self) -> TypeBase:
        return None

    def _build_call_start_stream(self, id: int) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "KRPC",
            "StartStream",
            [id],
            ["id"],
            [self._client._types.uint64_type],
            None
        )
