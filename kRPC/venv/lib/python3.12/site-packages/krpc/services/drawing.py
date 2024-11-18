# pylint: disable=line-too-long,invalid-name,redefined-builtin,too-many-lines
from __future__ import annotations
from typing import Tuple, Set, Dict, List, Optional, TYPE_CHECKING
import krpc.schema
from krpc.schema import KRPC_pb2
from krpc.types import TypeBase, ClassBase, WrappedClass, DocEnum
from krpc.event import Event
if TYPE_CHECKING:
    from krpc.services import Client
from krpc.services import ui
from krpc.services import spacecenter


class Line(ClassBase):
    """
    A line. Created using Drawing#addLine.
    """
    @property
    def color(self) -> Tuple[float,float,float]:
        """
        Set the color
        """
        return self._client._invoke(
            "Drawing",
            "Line_get_Color",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Line")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @color.setter
    def color(self, value: Tuple[float,float,float]) -> None:
        return self._client._invoke(
            "Drawing",
            "Line_set_Color",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Line"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)],
            None
        )

    def _return_type_color(self) -> TypeBase:
        return self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)

    def _build_call_color(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Line_get_Color",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Line")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @property
    def end(self) -> Tuple[float,float,float]:
        """
        End position of the line.
        """
        return self._client._invoke(
            "Drawing",
            "Line_get_End",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Line")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @end.setter
    def end(self, value: Tuple[float,float,float]) -> None:
        return self._client._invoke(
            "Drawing",
            "Line_set_End",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Line"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)],
            None
        )

    def _return_type_end(self) -> TypeBase:
        return self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)

    def _build_call_end(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Line_get_End",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Line")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @property
    def material(self) -> str:
        """
        Material used to render the object.
        Creates the material from a shader with the given name.
        """
        return self._client._invoke(
            "Drawing",
            "Line_get_Material",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Line")],
            self._client._types.string_type
        )

    @material.setter
    def material(self, value: str) -> None:
        return self._client._invoke(
            "Drawing",
            "Line_set_Material",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Line"), self._client._types.string_type],
            None
        )

    def _return_type_material(self) -> TypeBase:
        return self._client._types.string_type

    def _build_call_material(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Line_get_Material",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Line")],
            self._client._types.string_type
        )

    @property
    def reference_frame(self) -> spacecenter.ReferenceFrame:
        """
        Reference frame for the positions of the object.
        """
        return self._client._invoke(
            "Drawing",
            "Line_get_ReferenceFrame",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Line")],
            self._client._types.class_type("SpaceCenter", "ReferenceFrame")
        )

    @reference_frame.setter
    def reference_frame(self, value: spacecenter.ReferenceFrame) -> None:
        return self._client._invoke(
            "Drawing",
            "Line_set_ReferenceFrame",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Line"), self._client._types.class_type("SpaceCenter", "ReferenceFrame")],
            None
        )

    def _return_type_reference_frame(self) -> TypeBase:
        return self._client._types.class_type("SpaceCenter", "ReferenceFrame")

    def _build_call_reference_frame(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Line_get_ReferenceFrame",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Line")],
            self._client._types.class_type("SpaceCenter", "ReferenceFrame")
        )

    @property
    def start(self) -> Tuple[float,float,float]:
        """
        Start position of the line.
        """
        return self._client._invoke(
            "Drawing",
            "Line_get_Start",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Line")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @start.setter
    def start(self, value: Tuple[float,float,float]) -> None:
        return self._client._invoke(
            "Drawing",
            "Line_set_Start",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Line"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)],
            None
        )

    def _return_type_start(self) -> TypeBase:
        return self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)

    def _build_call_start(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Line_get_Start",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Line")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @property
    def thickness(self) -> float:
        """
        Set the thickness
        """
        return self._client._invoke(
            "Drawing",
            "Line_get_Thickness",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Line")],
            self._client._types.float_type
        )

    @thickness.setter
    def thickness(self, value: float) -> None:
        return self._client._invoke(
            "Drawing",
            "Line_set_Thickness",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Line"), self._client._types.float_type],
            None
        )

    def _return_type_thickness(self) -> TypeBase:
        return self._client._types.float_type

    def _build_call_thickness(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Line_get_Thickness",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Line")],
            self._client._types.float_type
        )

    @property
    def visible(self) -> bool:
        """
        Whether the object is visible.
        """
        return self._client._invoke(
            "Drawing",
            "Line_get_Visible",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Line")],
            self._client._types.bool_type
        )

    @visible.setter
    def visible(self, value: bool) -> None:
        return self._client._invoke(
            "Drawing",
            "Line_set_Visible",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Line"), self._client._types.bool_type],
            None
        )

    def _return_type_visible(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_visible(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Line_get_Visible",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Line")],
            self._client._types.bool_type
        )

    def remove(self) -> None:
        """
        Remove the object.
        """
        return self._client._invoke(
            "Drawing",
            "Line_Remove",
            [self, ],
            ["self", ],
            [self._client._types.class_type("Drawing", "Line"), ],
            None
        )

    def _return_type_remove(self) -> TypeBase:
        return None

    def _build_call_remove(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Line_Remove",
            [self, ],
            ["self", ],
            [self._client._types.class_type("Drawing", "Line"), ],
            None
        )



class Polygon(ClassBase):
    """
    A polygon. Created using Drawing#addPolygon.
    """
    @property
    def color(self) -> Tuple[float,float,float]:
        """
        Set the color
        """
        return self._client._invoke(
            "Drawing",
            "Polygon_get_Color",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Polygon")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @color.setter
    def color(self, value: Tuple[float,float,float]) -> None:
        return self._client._invoke(
            "Drawing",
            "Polygon_set_Color",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Polygon"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)],
            None
        )

    def _return_type_color(self) -> TypeBase:
        return self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)

    def _build_call_color(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Polygon_get_Color",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Polygon")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @property
    def material(self) -> str:
        """
        Material used to render the object.
        Creates the material from a shader with the given name.
        """
        return self._client._invoke(
            "Drawing",
            "Polygon_get_Material",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Polygon")],
            self._client._types.string_type
        )

    @material.setter
    def material(self, value: str) -> None:
        return self._client._invoke(
            "Drawing",
            "Polygon_set_Material",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Polygon"), self._client._types.string_type],
            None
        )

    def _return_type_material(self) -> TypeBase:
        return self._client._types.string_type

    def _build_call_material(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Polygon_get_Material",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Polygon")],
            self._client._types.string_type
        )

    @property
    def reference_frame(self) -> spacecenter.ReferenceFrame:
        """
        Reference frame for the positions of the object.
        """
        return self._client._invoke(
            "Drawing",
            "Polygon_get_ReferenceFrame",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Polygon")],
            self._client._types.class_type("SpaceCenter", "ReferenceFrame")
        )

    @reference_frame.setter
    def reference_frame(self, value: spacecenter.ReferenceFrame) -> None:
        return self._client._invoke(
            "Drawing",
            "Polygon_set_ReferenceFrame",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Polygon"), self._client._types.class_type("SpaceCenter", "ReferenceFrame")],
            None
        )

    def _return_type_reference_frame(self) -> TypeBase:
        return self._client._types.class_type("SpaceCenter", "ReferenceFrame")

    def _build_call_reference_frame(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Polygon_get_ReferenceFrame",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Polygon")],
            self._client._types.class_type("SpaceCenter", "ReferenceFrame")
        )

    @property
    def thickness(self) -> float:
        """
        Set the thickness
        """
        return self._client._invoke(
            "Drawing",
            "Polygon_get_Thickness",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Polygon")],
            self._client._types.float_type
        )

    @thickness.setter
    def thickness(self, value: float) -> None:
        return self._client._invoke(
            "Drawing",
            "Polygon_set_Thickness",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Polygon"), self._client._types.float_type],
            None
        )

    def _return_type_thickness(self) -> TypeBase:
        return self._client._types.float_type

    def _build_call_thickness(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Polygon_get_Thickness",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Polygon")],
            self._client._types.float_type
        )

    @property
    def vertices(self) -> List[Tuple[float,float,float]]:
        """
        Vertices for the polygon.
        """
        return self._client._invoke(
            "Drawing",
            "Polygon_get_Vertices",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Polygon")],
            self._client._types.list_type(self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type))
        )

    @vertices.setter
    def vertices(self, value: List[Tuple[float,float,float]]) -> None:
        return self._client._invoke(
            "Drawing",
            "Polygon_set_Vertices",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Polygon"), self._client._types.list_type(self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type))],
            None
        )

    def _return_type_vertices(self) -> TypeBase:
        return self._client._types.list_type(self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type))

    def _build_call_vertices(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Polygon_get_Vertices",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Polygon")],
            self._client._types.list_type(self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type))
        )

    @property
    def visible(self) -> bool:
        """
        Whether the object is visible.
        """
        return self._client._invoke(
            "Drawing",
            "Polygon_get_Visible",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Polygon")],
            self._client._types.bool_type
        )

    @visible.setter
    def visible(self, value: bool) -> None:
        return self._client._invoke(
            "Drawing",
            "Polygon_set_Visible",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Polygon"), self._client._types.bool_type],
            None
        )

    def _return_type_visible(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_visible(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Polygon_get_Visible",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Polygon")],
            self._client._types.bool_type
        )

    def remove(self) -> None:
        """
        Remove the object.
        """
        return self._client._invoke(
            "Drawing",
            "Polygon_Remove",
            [self, ],
            ["self", ],
            [self._client._types.class_type("Drawing", "Polygon"), ],
            None
        )

    def _return_type_remove(self) -> TypeBase:
        return None

    def _build_call_remove(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Polygon_Remove",
            [self, ],
            ["self", ],
            [self._client._types.class_type("Drawing", "Polygon"), ],
            None
        )



class Text(ClassBase):
    """
    Text. Created using Drawing#addText.
    """
    @property
    def alignment(self) -> ui.TextAlignment:
        """
        Alignment.
        """
        return self._client._invoke(
            "Drawing",
            "Text_get_Alignment",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.enumeration_type("UI", "TextAlignment")
        )

    @alignment.setter
    def alignment(self, value: ui.TextAlignment) -> None:
        return self._client._invoke(
            "Drawing",
            "Text_set_Alignment",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Text"), self._client._types.enumeration_type("UI", "TextAlignment")],
            None
        )

    def _return_type_alignment(self) -> TypeBase:
        return self._client._types.enumeration_type("UI", "TextAlignment")

    def _build_call_alignment(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Text_get_Alignment",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.enumeration_type("UI", "TextAlignment")
        )

    @property
    def anchor(self) -> ui.TextAnchor:
        """
        Anchor.
        """
        return self._client._invoke(
            "Drawing",
            "Text_get_Anchor",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.enumeration_type("UI", "TextAnchor")
        )

    @anchor.setter
    def anchor(self, value: ui.TextAnchor) -> None:
        return self._client._invoke(
            "Drawing",
            "Text_set_Anchor",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Text"), self._client._types.enumeration_type("UI", "TextAnchor")],
            None
        )

    def _return_type_anchor(self) -> TypeBase:
        return self._client._types.enumeration_type("UI", "TextAnchor")

    def _build_call_anchor(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Text_get_Anchor",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.enumeration_type("UI", "TextAnchor")
        )

    @property
    def character_size(self) -> float:
        """
        Character size.
        """
        return self._client._invoke(
            "Drawing",
            "Text_get_CharacterSize",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.float_type
        )

    @character_size.setter
    def character_size(self, value: float) -> None:
        return self._client._invoke(
            "Drawing",
            "Text_set_CharacterSize",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Text"), self._client._types.float_type],
            None
        )

    def _return_type_character_size(self) -> TypeBase:
        return self._client._types.float_type

    def _build_call_character_size(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Text_get_CharacterSize",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.float_type
        )

    @property
    def color(self) -> Tuple[float,float,float]:
        """
        Set the color
        """
        return self._client._invoke(
            "Drawing",
            "Text_get_Color",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @color.setter
    def color(self, value: Tuple[float,float,float]) -> None:
        return self._client._invoke(
            "Drawing",
            "Text_set_Color",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Text"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)],
            None
        )

    def _return_type_color(self) -> TypeBase:
        return self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)

    def _build_call_color(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Text_get_Color",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @property
    def content(self) -> str:
        """
        The text string
        """
        return self._client._invoke(
            "Drawing",
            "Text_get_Content",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.string_type
        )

    @content.setter
    def content(self, value: str) -> None:
        return self._client._invoke(
            "Drawing",
            "Text_set_Content",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Text"), self._client._types.string_type],
            None
        )

    def _return_type_content(self) -> TypeBase:
        return self._client._types.string_type

    def _build_call_content(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Text_get_Content",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.string_type
        )

    @property
    def font(self) -> str:
        """
        Name of the font
        """
        return self._client._invoke(
            "Drawing",
            "Text_get_Font",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.string_type
        )

    @font.setter
    def font(self, value: str) -> None:
        return self._client._invoke(
            "Drawing",
            "Text_set_Font",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Text"), self._client._types.string_type],
            None
        )

    def _return_type_font(self) -> TypeBase:
        return self._client._types.string_type

    def _build_call_font(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Text_get_Font",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.string_type
        )

    @property
    def line_spacing(self) -> float:
        """
        Line spacing.
        """
        return self._client._invoke(
            "Drawing",
            "Text_get_LineSpacing",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.float_type
        )

    @line_spacing.setter
    def line_spacing(self, value: float) -> None:
        return self._client._invoke(
            "Drawing",
            "Text_set_LineSpacing",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Text"), self._client._types.float_type],
            None
        )

    def _return_type_line_spacing(self) -> TypeBase:
        return self._client._types.float_type

    def _build_call_line_spacing(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Text_get_LineSpacing",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.float_type
        )

    @property
    def material(self) -> str:
        """
        Material used to render the object.
        Creates the material from a shader with the given name.
        """
        return self._client._invoke(
            "Drawing",
            "Text_get_Material",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.string_type
        )

    @material.setter
    def material(self, value: str) -> None:
        return self._client._invoke(
            "Drawing",
            "Text_set_Material",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Text"), self._client._types.string_type],
            None
        )

    def _return_type_material(self) -> TypeBase:
        return self._client._types.string_type

    def _build_call_material(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Text_get_Material",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.string_type
        )

    @property
    def position(self) -> Tuple[float,float,float]:
        """
        Position of the text.
        """
        return self._client._invoke(
            "Drawing",
            "Text_get_Position",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @position.setter
    def position(self, value: Tuple[float,float,float]) -> None:
        return self._client._invoke(
            "Drawing",
            "Text_set_Position",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Text"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)],
            None
        )

    def _return_type_position(self) -> TypeBase:
        return self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)

    def _build_call_position(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Text_get_Position",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @property
    def reference_frame(self) -> spacecenter.ReferenceFrame:
        """
        Reference frame for the positions of the object.
        """
        return self._client._invoke(
            "Drawing",
            "Text_get_ReferenceFrame",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.class_type("SpaceCenter", "ReferenceFrame")
        )

    @reference_frame.setter
    def reference_frame(self, value: spacecenter.ReferenceFrame) -> None:
        return self._client._invoke(
            "Drawing",
            "Text_set_ReferenceFrame",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Text"), self._client._types.class_type("SpaceCenter", "ReferenceFrame")],
            None
        )

    def _return_type_reference_frame(self) -> TypeBase:
        return self._client._types.class_type("SpaceCenter", "ReferenceFrame")

    def _build_call_reference_frame(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Text_get_ReferenceFrame",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.class_type("SpaceCenter", "ReferenceFrame")
        )

    @property
    def rotation(self) -> Tuple[float,float,float,float]:
        """
        Rotation of the text as a quaternion.
        """
        return self._client._invoke(
            "Drawing",
            "Text_get_Rotation",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @rotation.setter
    def rotation(self, value: Tuple[float,float,float,float]) -> None:
        return self._client._invoke(
            "Drawing",
            "Text_set_Rotation",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Text"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)],
            None
        )

    def _return_type_rotation(self) -> TypeBase:
        return self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)

    def _build_call_rotation(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Text_get_Rotation",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @property
    def size(self) -> int:
        """
        Font size.
        """
        return self._client._invoke(
            "Drawing",
            "Text_get_Size",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.sint32_type
        )

    @size.setter
    def size(self, value: int) -> None:
        return self._client._invoke(
            "Drawing",
            "Text_set_Size",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Text"), self._client._types.sint32_type],
            None
        )

    def _return_type_size(self) -> TypeBase:
        return self._client._types.sint32_type

    def _build_call_size(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Text_get_Size",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.sint32_type
        )

    @property
    def style(self) -> ui.FontStyle:
        """
        Font style.
        """
        return self._client._invoke(
            "Drawing",
            "Text_get_Style",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.enumeration_type("UI", "FontStyle")
        )

    @style.setter
    def style(self, value: ui.FontStyle) -> None:
        return self._client._invoke(
            "Drawing",
            "Text_set_Style",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Text"), self._client._types.enumeration_type("UI", "FontStyle")],
            None
        )

    def _return_type_style(self) -> TypeBase:
        return self._client._types.enumeration_type("UI", "FontStyle")

    def _build_call_style(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Text_get_Style",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.enumeration_type("UI", "FontStyle")
        )

    @property
    def visible(self) -> bool:
        """
        Whether the object is visible.
        """
        return self._client._invoke(
            "Drawing",
            "Text_get_Visible",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.bool_type
        )

    @visible.setter
    def visible(self, value: bool) -> None:
        return self._client._invoke(
            "Drawing",
            "Text_set_Visible",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("Drawing", "Text"), self._client._types.bool_type],
            None
        )

    def _return_type_visible(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_visible(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Text_get_Visible",
            [self],
            ["self"],
            [self._client._types.class_type("Drawing", "Text")],
            self._client._types.bool_type
        )

    def remove(self) -> None:
        """
        Remove the object.
        """
        return self._client._invoke(
            "Drawing",
            "Text_Remove",
            [self, ],
            ["self", ],
            [self._client._types.class_type("Drawing", "Text"), ],
            None
        )

    def _return_type_remove(self) -> TypeBase:
        return None

    def _build_call_remove(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Text_Remove",
            [self, ],
            ["self", ],
            [self._client._types.class_type("Drawing", "Text"), ],
            None
        )

    @classmethod
    def available_fonts(cls, ) -> List[str]:
        """
        A list of all available fonts.
        """
        self = cls
        return cls._client._invoke(
            "Drawing",
            "Text_static_AvailableFonts",
            [],
            [],
            [],
            self._client._types.list_type(self._client._types.string_type)
        )

    @classmethod
    def _return_type_available_fonts(cls) -> TypeBase:
        self = cls
        return self._client._types.list_type(self._client._types.string_type)

    @classmethod
    def _build_call_available_fonts(cls, ) -> KRPC_pb2.ProcedureCall:
        self = cls
        return self._client._build_call(
            "Drawing",
            "Text_static_AvailableFonts",
            [],
            [],
            [],
            self._client._types.list_type(self._client._types.string_type)
        )



class Drawing:
    """
    Provides functionality for drawing objects in the flight scene.

    For drawing and interacting with the user interface, see the UI service.
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
        "Line": Line,
        "Polygon": Polygon,
        "Text": Text,
    }
    _enumerations = {
    }
    _exceptions = {
    }

    def add_direction(self, direction: Tuple[float,float,float], reference_frame: spacecenter.ReferenceFrame, length: float = 10.0, visible: bool = True) -> Line:
        """
        Draw a direction vector in the scene, starting from the origin of the given reference frame.

        :param direction: Direction to draw the line in.

        :param reference_frame: Reference frame that the direction is in and defines the start position.

        :param length: The length of the line.

        :param visible: Whether the line is visible.
        """
        return self._client._invoke(
            "Drawing",
            "AddDirection",
            [direction, reference_frame, length, visible],
            ["direction", "reference_frame", "length", "visible"],
            [self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type), self._client._types.class_type("SpaceCenter", "ReferenceFrame"), self._client._types.float_type, self._client._types.bool_type],
            self._client._types.class_type("Drawing", "Line")
        )

    def _return_type_add_direction(self) -> TypeBase:
        return self._client._types.class_type("Drawing", "Line")

    def _build_call_add_direction(self, direction: Tuple[float,float,float], reference_frame: spacecenter.ReferenceFrame, length: float = 10.0, visible: bool = True) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "AddDirection",
            [direction, reference_frame, length, visible],
            ["direction", "reference_frame", "length", "visible"],
            [self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type), self._client._types.class_type("SpaceCenter", "ReferenceFrame"), self._client._types.float_type, self._client._types.bool_type],
            self._client._types.class_type("Drawing", "Line")
        )

    def add_direction_from_com(self, direction: Tuple[float,float,float], reference_frame: spacecenter.ReferenceFrame, length: float = 10.0, visible: bool = True) -> Line:
        """
        Draw a direction vector in the scene, from the center of mass of the active vessel.

        :param direction: Direction to draw the line in.

        :param reference_frame: Reference frame that the direction is in.

        :param length: The length of the line.

        :param visible: Whether the line is visible.
        """
        return self._client._invoke(
            "Drawing",
            "AddDirectionFromCom",
            [direction, reference_frame, length, visible],
            ["direction", "reference_frame", "length", "visible"],
            [self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type), self._client._types.class_type("SpaceCenter", "ReferenceFrame"), self._client._types.float_type, self._client._types.bool_type],
            self._client._types.class_type("Drawing", "Line")
        )

    def _return_type_add_direction_from_com(self) -> TypeBase:
        return self._client._types.class_type("Drawing", "Line")

    def _build_call_add_direction_from_com(self, direction: Tuple[float,float,float], reference_frame: spacecenter.ReferenceFrame, length: float = 10.0, visible: bool = True) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "AddDirectionFromCom",
            [direction, reference_frame, length, visible],
            ["direction", "reference_frame", "length", "visible"],
            [self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type), self._client._types.class_type("SpaceCenter", "ReferenceFrame"), self._client._types.float_type, self._client._types.bool_type],
            self._client._types.class_type("Drawing", "Line")
        )

    def add_line(self, start: Tuple[float,float,float], end: Tuple[float,float,float], reference_frame: spacecenter.ReferenceFrame, visible: bool = True) -> Line:
        """
        Draw a line in the scene.

        :param start: Position of the start of the line.

        :param end: Position of the end of the line.

        :param reference_frame: Reference frame that the positions are in.

        :param visible: Whether the line is visible.
        """
        return self._client._invoke(
            "Drawing",
            "AddLine",
            [start, end, reference_frame, visible],
            ["start", "end", "reference_frame", "visible"],
            [self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type), self._client._types.class_type("SpaceCenter", "ReferenceFrame"), self._client._types.bool_type],
            self._client._types.class_type("Drawing", "Line")
        )

    def _return_type_add_line(self) -> TypeBase:
        return self._client._types.class_type("Drawing", "Line")

    def _build_call_add_line(self, start: Tuple[float,float,float], end: Tuple[float,float,float], reference_frame: spacecenter.ReferenceFrame, visible: bool = True) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "AddLine",
            [start, end, reference_frame, visible],
            ["start", "end", "reference_frame", "visible"],
            [self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type), self._client._types.class_type("SpaceCenter", "ReferenceFrame"), self._client._types.bool_type],
            self._client._types.class_type("Drawing", "Line")
        )

    def add_polygon(self, vertices: List[Tuple[float,float,float]], reference_frame: spacecenter.ReferenceFrame, visible: bool = True) -> Polygon:
        """
        Draw a polygon in the scene, defined by a list of vertices.

        :param vertices: Vertices of the polygon.

        :param reference_frame: Reference frame that the vertices are in.

        :param visible: Whether the polygon is visible.
        """
        return self._client._invoke(
            "Drawing",
            "AddPolygon",
            [vertices, reference_frame, visible],
            ["vertices", "reference_frame", "visible"],
            [self._client._types.list_type(self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)), self._client._types.class_type("SpaceCenter", "ReferenceFrame"), self._client._types.bool_type],
            self._client._types.class_type("Drawing", "Polygon")
        )

    def _return_type_add_polygon(self) -> TypeBase:
        return self._client._types.class_type("Drawing", "Polygon")

    def _build_call_add_polygon(self, vertices: List[Tuple[float,float,float]], reference_frame: spacecenter.ReferenceFrame, visible: bool = True) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "AddPolygon",
            [vertices, reference_frame, visible],
            ["vertices", "reference_frame", "visible"],
            [self._client._types.list_type(self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)), self._client._types.class_type("SpaceCenter", "ReferenceFrame"), self._client._types.bool_type],
            self._client._types.class_type("Drawing", "Polygon")
        )

    def add_text(self, text: str, reference_frame: spacecenter.ReferenceFrame, position: Tuple[float,float,float], rotation: Tuple[float,float,float,float], visible: bool = True) -> Text:
        """
        Draw text in the scene.

        :param text: The string to draw.

        :param reference_frame: Reference frame that the text position is in.

        :param position: Position of the text.

        :param rotation: Rotation of the text, as a quaternion.

        :param visible: Whether the text is visible.
        """
        return self._client._invoke(
            "Drawing",
            "AddText",
            [text, reference_frame, position, rotation, visible],
            ["text", "reference_frame", "position", "rotation", "visible"],
            [self._client._types.string_type, self._client._types.class_type("SpaceCenter", "ReferenceFrame"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type, self._client._types.double_type), self._client._types.bool_type],
            self._client._types.class_type("Drawing", "Text")
        )

    def _return_type_add_text(self) -> TypeBase:
        return self._client._types.class_type("Drawing", "Text")

    def _build_call_add_text(self, text: str, reference_frame: spacecenter.ReferenceFrame, position: Tuple[float,float,float], rotation: Tuple[float,float,float,float], visible: bool = True) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "AddText",
            [text, reference_frame, position, rotation, visible],
            ["text", "reference_frame", "position", "rotation", "visible"],
            [self._client._types.string_type, self._client._types.class_type("SpaceCenter", "ReferenceFrame"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type, self._client._types.double_type), self._client._types.bool_type],
            self._client._types.class_type("Drawing", "Text")
        )

    def clear(self, client_only: bool = False) -> None:
        """
        Remove all objects being drawn.

        :param client_only: If true, only remove objects created by the calling client.
        """
        return self._client._invoke(
            "Drawing",
            "Clear",
            [client_only],
            ["client_only"],
            [self._client._types.bool_type],
            None
        )

    def _return_type_clear(self) -> TypeBase:
        return None

    def _build_call_clear(self, client_only: bool = False) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "Drawing",
            "Clear",
            [client_only],
            ["client_only"],
            [self._client._types.bool_type],
            None
        )
