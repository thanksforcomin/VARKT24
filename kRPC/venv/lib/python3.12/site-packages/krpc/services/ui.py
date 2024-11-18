# pylint: disable=line-too-long,invalid-name,redefined-builtin,too-many-lines
from __future__ import annotations
from typing import Tuple, Set, Dict, List, Optional, TYPE_CHECKING
import krpc.schema
from krpc.schema import KRPC_pb2
from krpc.types import TypeBase, ClassBase, WrappedClass, DocEnum
from krpc.event import Event
if TYPE_CHECKING:
    from krpc.services import Client


class FontStyle(DocEnum):
    """
    Font style.
    """
    normal = 0, """
Normal.
"""
    bold = 1, """
Bold.
"""
    italic = 2, """
Italic.
"""
    bold_and_italic = 3, """
Bold and italic.
"""


class MessagePosition(DocEnum):
    """
    Message position.
    """
    bottom_center = 0, """
Bottom center.
"""
    top_center = 1, """
Top center.
"""
    top_left = 2, """
Top left.
"""
    top_right = 3, """
Top right.
"""


class TextAlignment(DocEnum):
    """
    Text alignment.
    """
    left = 0, """
Left aligned.
"""
    right = 1, """
Right aligned.
"""
    center = 2, """
Center aligned.
"""


class TextAnchor(DocEnum):
    """
    Text alignment.
    """
    lower_center = 0, """
Lower center.
"""
    lower_left = 1, """
Lower left.
"""
    lower_right = 2, """
Lower right.
"""
    middle_center = 3, """
Middle center.
"""
    middle_left = 4, """
Middle left.
"""
    middle_right = 5, """
Middle right.
"""
    upper_center = 6, """
Upper center.
"""
    upper_left = 7, """
Upper left.
"""
    upper_right = 8, """
Upper right.
"""


class Button(ClassBase):
    """
    A text label. See UI.Panel#addButton.
    """
    @property
    def clicked(self) -> bool:
        """
        Whether the button has been clicked.

        This property is set to true when the user clicks the button.
        A client script should reset the property to false in order to detect subsequent button presses.
        """
        return self._client._invoke(
            "UI",
            "Button_get_Clicked",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Button")],
            self._client._types.bool_type
        )

    @clicked.setter
    def clicked(self, value: bool) -> None:
        return self._client._invoke(
            "UI",
            "Button_set_Clicked",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "Button"), self._client._types.bool_type],
            None
        )

    def _return_type_clicked(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_clicked(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Button_get_Clicked",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Button")],
            self._client._types.bool_type
        )

    @property
    def rect_transform(self) -> RectTransform:
        """
        The rect transform for the text.
        """
        return self._client._invoke(
            "UI",
            "Button_get_RectTransform",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Button")],
            self._client._types.class_type("UI", "RectTransform")
        )

    def _return_type_rect_transform(self) -> TypeBase:
        return self._client._types.class_type("UI", "RectTransform")

    def _build_call_rect_transform(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Button_get_RectTransform",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Button")],
            self._client._types.class_type("UI", "RectTransform")
        )

    @property
    def text(self) -> Text:
        """
        The text for the button.
        """
        return self._client._invoke(
            "UI",
            "Button_get_Text",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Button")],
            self._client._types.class_type("UI", "Text")
        )

    def _return_type_text(self) -> TypeBase:
        return self._client._types.class_type("UI", "Text")

    def _build_call_text(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Button_get_Text",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Button")],
            self._client._types.class_type("UI", "Text")
        )

    @property
    def visible(self) -> bool:
        """
        Whether the UI object is visible.
        """
        return self._client._invoke(
            "UI",
            "Button_get_Visible",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Button")],
            self._client._types.bool_type
        )

    @visible.setter
    def visible(self, value: bool) -> None:
        return self._client._invoke(
            "UI",
            "Button_set_Visible",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "Button"), self._client._types.bool_type],
            None
        )

    def _return_type_visible(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_visible(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Button_get_Visible",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Button")],
            self._client._types.bool_type
        )

    def remove(self) -> None:
        """
        Remove the UI object.
        """
        return self._client._invoke(
            "UI",
            "Button_Remove",
            [self, ],
            ["self", ],
            [self._client._types.class_type("UI", "Button"), ],
            None
        )

    def _return_type_remove(self) -> TypeBase:
        return None

    def _build_call_remove(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Button_Remove",
            [self, ],
            ["self", ],
            [self._client._types.class_type("UI", "Button"), ],
            None
        )



class Canvas(ClassBase):
    """
    A canvas for user interface elements. See UI#stockCanvas and UI#addCanvas.
    """
    @property
    def rect_transform(self) -> RectTransform:
        """
        The rect transform for the canvas.
        """
        return self._client._invoke(
            "UI",
            "Canvas_get_RectTransform",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Canvas")],
            self._client._types.class_type("UI", "RectTransform")
        )

    def _return_type_rect_transform(self) -> TypeBase:
        return self._client._types.class_type("UI", "RectTransform")

    def _build_call_rect_transform(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Canvas_get_RectTransform",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Canvas")],
            self._client._types.class_type("UI", "RectTransform")
        )

    @property
    def visible(self) -> bool:
        """
        Whether the UI object is visible.
        """
        return self._client._invoke(
            "UI",
            "Canvas_get_Visible",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Canvas")],
            self._client._types.bool_type
        )

    @visible.setter
    def visible(self, value: bool) -> None:
        return self._client._invoke(
            "UI",
            "Canvas_set_Visible",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "Canvas"), self._client._types.bool_type],
            None
        )

    def _return_type_visible(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_visible(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Canvas_get_Visible",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Canvas")],
            self._client._types.bool_type
        )

    def add_button(self, content: str, visible: bool = True) -> Button:
        """
        Add a button to the canvas.

        :param content: The label for the button.

        :param visible: Whether the button is visible.
        """
        return self._client._invoke(
            "UI",
            "Canvas_AddButton",
            [self, content, visible],
            ["self", "content", "visible"],
            [self._client._types.class_type("UI", "Canvas"), self._client._types.string_type, self._client._types.bool_type],
            self._client._types.class_type("UI", "Button")
        )

    def _return_type_add_button(self) -> TypeBase:
        return self._client._types.class_type("UI", "Button")

    def _build_call_add_button(self, content: str, visible: bool = True) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Canvas_AddButton",
            [self, content, visible],
            ["self", "content", "visible"],
            [self._client._types.class_type("UI", "Canvas"), self._client._types.string_type, self._client._types.bool_type],
            self._client._types.class_type("UI", "Button")
        )

    def add_input_field(self, visible: bool = True) -> InputField:
        """
        Add an input field to the canvas.

        :param visible: Whether the input field is visible.
        """
        return self._client._invoke(
            "UI",
            "Canvas_AddInputField",
            [self, visible],
            ["self", "visible"],
            [self._client._types.class_type("UI", "Canvas"), self._client._types.bool_type],
            self._client._types.class_type("UI", "InputField")
        )

    def _return_type_add_input_field(self) -> TypeBase:
        return self._client._types.class_type("UI", "InputField")

    def _build_call_add_input_field(self, visible: bool = True) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Canvas_AddInputField",
            [self, visible],
            ["self", "visible"],
            [self._client._types.class_type("UI", "Canvas"), self._client._types.bool_type],
            self._client._types.class_type("UI", "InputField")
        )

    def add_panel(self, visible: bool = True) -> Panel:
        """
        Create a new container for user interface elements.

        :param visible: Whether the panel is visible.
        """
        return self._client._invoke(
            "UI",
            "Canvas_AddPanel",
            [self, visible],
            ["self", "visible"],
            [self._client._types.class_type("UI", "Canvas"), self._client._types.bool_type],
            self._client._types.class_type("UI", "Panel")
        )

    def _return_type_add_panel(self) -> TypeBase:
        return self._client._types.class_type("UI", "Panel")

    def _build_call_add_panel(self, visible: bool = True) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Canvas_AddPanel",
            [self, visible],
            ["self", "visible"],
            [self._client._types.class_type("UI", "Canvas"), self._client._types.bool_type],
            self._client._types.class_type("UI", "Panel")
        )

    def add_text(self, content: str, visible: bool = True) -> Text:
        """
        Add text to the canvas.

        :param content: The text.

        :param visible: Whether the text is visible.
        """
        return self._client._invoke(
            "UI",
            "Canvas_AddText",
            [self, content, visible],
            ["self", "content", "visible"],
            [self._client._types.class_type("UI", "Canvas"), self._client._types.string_type, self._client._types.bool_type],
            self._client._types.class_type("UI", "Text")
        )

    def _return_type_add_text(self) -> TypeBase:
        return self._client._types.class_type("UI", "Text")

    def _build_call_add_text(self, content: str, visible: bool = True) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Canvas_AddText",
            [self, content, visible],
            ["self", "content", "visible"],
            [self._client._types.class_type("UI", "Canvas"), self._client._types.string_type, self._client._types.bool_type],
            self._client._types.class_type("UI", "Text")
        )

    def remove(self) -> None:
        """
        Remove the UI object.
        """
        return self._client._invoke(
            "UI",
            "Canvas_Remove",
            [self, ],
            ["self", ],
            [self._client._types.class_type("UI", "Canvas"), ],
            None
        )

    def _return_type_remove(self) -> TypeBase:
        return None

    def _build_call_remove(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Canvas_Remove",
            [self, ],
            ["self", ],
            [self._client._types.class_type("UI", "Canvas"), ],
            None
        )



class InputField(ClassBase):
    """
    An input field. See UI.Panel#addInputField.
    """
    @property
    def changed(self) -> bool:
        """
        Whether the input field has been changed.

        This property is set to true when the user modifies the value of the input field.
        A client script should reset the property to false in order to detect subsequent changes.
        """
        return self._client._invoke(
            "UI",
            "InputField_get_Changed",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "InputField")],
            self._client._types.bool_type
        )

    @changed.setter
    def changed(self, value: bool) -> None:
        return self._client._invoke(
            "UI",
            "InputField_set_Changed",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "InputField"), self._client._types.bool_type],
            None
        )

    def _return_type_changed(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_changed(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "InputField_get_Changed",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "InputField")],
            self._client._types.bool_type
        )

    @property
    def rect_transform(self) -> RectTransform:
        """
        The rect transform for the input field.
        """
        return self._client._invoke(
            "UI",
            "InputField_get_RectTransform",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "InputField")],
            self._client._types.class_type("UI", "RectTransform")
        )

    def _return_type_rect_transform(self) -> TypeBase:
        return self._client._types.class_type("UI", "RectTransform")

    def _build_call_rect_transform(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "InputField_get_RectTransform",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "InputField")],
            self._client._types.class_type("UI", "RectTransform")
        )

    @property
    def text(self) -> Text:
        """
        The text component of the input field.

        Use UI.InputField#value to get and set the value in the field.
        This object can be used to alter the style of the input field's text.
        """
        return self._client._invoke(
            "UI",
            "InputField_get_Text",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "InputField")],
            self._client._types.class_type("UI", "Text")
        )

    def _return_type_text(self) -> TypeBase:
        return self._client._types.class_type("UI", "Text")

    def _build_call_text(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "InputField_get_Text",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "InputField")],
            self._client._types.class_type("UI", "Text")
        )

    @property
    def value(self) -> str:
        """
        The value of the input field.
        """
        return self._client._invoke(
            "UI",
            "InputField_get_Value",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "InputField")],
            self._client._types.string_type
        )

    @value.setter
    def value(self, value: str) -> None:
        return self._client._invoke(
            "UI",
            "InputField_set_Value",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "InputField"), self._client._types.string_type],
            None
        )

    def _return_type_value(self) -> TypeBase:
        return self._client._types.string_type

    def _build_call_value(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "InputField_get_Value",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "InputField")],
            self._client._types.string_type
        )

    @property
    def visible(self) -> bool:
        """
        Whether the UI object is visible.
        """
        return self._client._invoke(
            "UI",
            "InputField_get_Visible",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "InputField")],
            self._client._types.bool_type
        )

    @visible.setter
    def visible(self, value: bool) -> None:
        return self._client._invoke(
            "UI",
            "InputField_set_Visible",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "InputField"), self._client._types.bool_type],
            None
        )

    def _return_type_visible(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_visible(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "InputField_get_Visible",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "InputField")],
            self._client._types.bool_type
        )

    def remove(self) -> None:
        """
        Remove the UI object.
        """
        return self._client._invoke(
            "UI",
            "InputField_Remove",
            [self, ],
            ["self", ],
            [self._client._types.class_type("UI", "InputField"), ],
            None
        )

    def _return_type_remove(self) -> TypeBase:
        return None

    def _build_call_remove(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "InputField_Remove",
            [self, ],
            ["self", ],
            [self._client._types.class_type("UI", "InputField"), ],
            None
        )



class Panel(ClassBase):
    """
    A container for user interface elements. See UI.Canvas#addPanel.
    """
    @property
    def rect_transform(self) -> RectTransform:
        """
        The rect transform for the panel.
        """
        return self._client._invoke(
            "UI",
            "Panel_get_RectTransform",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Panel")],
            self._client._types.class_type("UI", "RectTransform")
        )

    def _return_type_rect_transform(self) -> TypeBase:
        return self._client._types.class_type("UI", "RectTransform")

    def _build_call_rect_transform(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Panel_get_RectTransform",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Panel")],
            self._client._types.class_type("UI", "RectTransform")
        )

    @property
    def visible(self) -> bool:
        """
        Whether the UI object is visible.
        """
        return self._client._invoke(
            "UI",
            "Panel_get_Visible",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Panel")],
            self._client._types.bool_type
        )

    @visible.setter
    def visible(self, value: bool) -> None:
        return self._client._invoke(
            "UI",
            "Panel_set_Visible",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "Panel"), self._client._types.bool_type],
            None
        )

    def _return_type_visible(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_visible(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Panel_get_Visible",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Panel")],
            self._client._types.bool_type
        )

    def add_button(self, content: str, visible: bool = True) -> Button:
        """
        Add a button to the panel.

        :param content: The label for the button.

        :param visible: Whether the button is visible.
        """
        return self._client._invoke(
            "UI",
            "Panel_AddButton",
            [self, content, visible],
            ["self", "content", "visible"],
            [self._client._types.class_type("UI", "Panel"), self._client._types.string_type, self._client._types.bool_type],
            self._client._types.class_type("UI", "Button")
        )

    def _return_type_add_button(self) -> TypeBase:
        return self._client._types.class_type("UI", "Button")

    def _build_call_add_button(self, content: str, visible: bool = True) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Panel_AddButton",
            [self, content, visible],
            ["self", "content", "visible"],
            [self._client._types.class_type("UI", "Panel"), self._client._types.string_type, self._client._types.bool_type],
            self._client._types.class_type("UI", "Button")
        )

    def add_input_field(self, visible: bool = True) -> InputField:
        """
        Add an input field to the panel.

        :param visible: Whether the input field is visible.
        """
        return self._client._invoke(
            "UI",
            "Panel_AddInputField",
            [self, visible],
            ["self", "visible"],
            [self._client._types.class_type("UI", "Panel"), self._client._types.bool_type],
            self._client._types.class_type("UI", "InputField")
        )

    def _return_type_add_input_field(self) -> TypeBase:
        return self._client._types.class_type("UI", "InputField")

    def _build_call_add_input_field(self, visible: bool = True) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Panel_AddInputField",
            [self, visible],
            ["self", "visible"],
            [self._client._types.class_type("UI", "Panel"), self._client._types.bool_type],
            self._client._types.class_type("UI", "InputField")
        )

    def add_panel(self, visible: bool = True) -> Panel:
        """
        Create a panel within this panel.

        :param visible: Whether the new panel is visible.
        """
        return self._client._invoke(
            "UI",
            "Panel_AddPanel",
            [self, visible],
            ["self", "visible"],
            [self._client._types.class_type("UI", "Panel"), self._client._types.bool_type],
            self._client._types.class_type("UI", "Panel")
        )

    def _return_type_add_panel(self) -> TypeBase:
        return self._client._types.class_type("UI", "Panel")

    def _build_call_add_panel(self, visible: bool = True) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Panel_AddPanel",
            [self, visible],
            ["self", "visible"],
            [self._client._types.class_type("UI", "Panel"), self._client._types.bool_type],
            self._client._types.class_type("UI", "Panel")
        )

    def add_text(self, content: str, visible: bool = True) -> Text:
        """
        Add text to the panel.

        :param content: The text.

        :param visible: Whether the text is visible.
        """
        return self._client._invoke(
            "UI",
            "Panel_AddText",
            [self, content, visible],
            ["self", "content", "visible"],
            [self._client._types.class_type("UI", "Panel"), self._client._types.string_type, self._client._types.bool_type],
            self._client._types.class_type("UI", "Text")
        )

    def _return_type_add_text(self) -> TypeBase:
        return self._client._types.class_type("UI", "Text")

    def _build_call_add_text(self, content: str, visible: bool = True) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Panel_AddText",
            [self, content, visible],
            ["self", "content", "visible"],
            [self._client._types.class_type("UI", "Panel"), self._client._types.string_type, self._client._types.bool_type],
            self._client._types.class_type("UI", "Text")
        )

    def remove(self) -> None:
        """
        Remove the UI object.
        """
        return self._client._invoke(
            "UI",
            "Panel_Remove",
            [self, ],
            ["self", ],
            [self._client._types.class_type("UI", "Panel"), ],
            None
        )

    def _return_type_remove(self) -> TypeBase:
        return None

    def _build_call_remove(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Panel_Remove",
            [self, ],
            ["self", ],
            [self._client._types.class_type("UI", "Panel"), ],
            None
        )



class RectTransform(ClassBase):
    """
    A Unity engine Rect Transform for a UI object.
    See the `Unity manual <https://docs.unity3d.com/Manual/class-RectTransform.html>`_ for more details.
    """
    @property
    def anchor(self) -> Tuple[float,float]:
        raise NotImplementedError

    @anchor.setter
    def anchor(self, value: Tuple[float,float]) -> None:
        return self._client._invoke(
            "UI",
            "RectTransform_set_Anchor",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "RectTransform"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)],
            None
        )

    @property
    def anchor_max(self) -> Tuple[float,float]:
        """
        The anchor point for the lower left corner of the rectangle defined as a fraction of the size of the parent rectangle.
        """
        return self._client._invoke(
            "UI",
            "RectTransform_get_AnchorMax",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)
        )

    @anchor_max.setter
    def anchor_max(self, value: Tuple[float,float]) -> None:
        return self._client._invoke(
            "UI",
            "RectTransform_set_AnchorMax",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "RectTransform"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)],
            None
        )

    def _return_type_anchor_max(self) -> TypeBase:
        return self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)

    def _build_call_anchor_max(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "RectTransform_get_AnchorMax",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)
        )

    @property
    def anchor_min(self) -> Tuple[float,float]:
        """
        The anchor point for the upper right corner of the rectangle defined as a fraction of the size of the parent rectangle.
        """
        return self._client._invoke(
            "UI",
            "RectTransform_get_AnchorMin",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)
        )

    @anchor_min.setter
    def anchor_min(self, value: Tuple[float,float]) -> None:
        return self._client._invoke(
            "UI",
            "RectTransform_set_AnchorMin",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "RectTransform"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)],
            None
        )

    def _return_type_anchor_min(self) -> TypeBase:
        return self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)

    def _build_call_anchor_min(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "RectTransform_get_AnchorMin",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)
        )

    @property
    def local_position(self) -> Tuple[float,float,float]:
        """
        Position of the rectangles pivot point relative to the anchors.
        """
        return self._client._invoke(
            "UI",
            "RectTransform_get_LocalPosition",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @local_position.setter
    def local_position(self, value: Tuple[float,float,float]) -> None:
        return self._client._invoke(
            "UI",
            "RectTransform_set_LocalPosition",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "RectTransform"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)],
            None
        )

    def _return_type_local_position(self) -> TypeBase:
        return self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)

    def _build_call_local_position(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "RectTransform_get_LocalPosition",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @property
    def lower_left(self) -> Tuple[float,float]:
        """
        Position of the rectangles lower left corner relative to the anchors.
        """
        return self._client._invoke(
            "UI",
            "RectTransform_get_LowerLeft",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)
        )

    @lower_left.setter
    def lower_left(self, value: Tuple[float,float]) -> None:
        return self._client._invoke(
            "UI",
            "RectTransform_set_LowerLeft",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "RectTransform"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)],
            None
        )

    def _return_type_lower_left(self) -> TypeBase:
        return self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)

    def _build_call_lower_left(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "RectTransform_get_LowerLeft",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)
        )

    @property
    def pivot(self) -> Tuple[float,float]:
        """
        Location of the pivot point around which the rectangle rotates, defined as a fraction of the size of the rectangle itself.
        """
        return self._client._invoke(
            "UI",
            "RectTransform_get_Pivot",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)
        )

    @pivot.setter
    def pivot(self, value: Tuple[float,float]) -> None:
        return self._client._invoke(
            "UI",
            "RectTransform_set_Pivot",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "RectTransform"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)],
            None
        )

    def _return_type_pivot(self) -> TypeBase:
        return self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)

    def _build_call_pivot(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "RectTransform_get_Pivot",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)
        )

    @property
    def position(self) -> Tuple[float,float]:
        """
        Position of the rectangles pivot point relative to the anchors.
        """
        return self._client._invoke(
            "UI",
            "RectTransform_get_Position",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)
        )

    @position.setter
    def position(self, value: Tuple[float,float]) -> None:
        return self._client._invoke(
            "UI",
            "RectTransform_set_Position",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "RectTransform"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)],
            None
        )

    def _return_type_position(self) -> TypeBase:
        return self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)

    def _build_call_position(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "RectTransform_get_Position",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)
        )

    @property
    def rotation(self) -> Tuple[float,float,float,float]:
        """
        Rotation, as a quaternion, of the object around its pivot point.
        """
        return self._client._invoke(
            "UI",
            "RectTransform_get_Rotation",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @rotation.setter
    def rotation(self, value: Tuple[float,float,float,float]) -> None:
        return self._client._invoke(
            "UI",
            "RectTransform_set_Rotation",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "RectTransform"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)],
            None
        )

    def _return_type_rotation(self) -> TypeBase:
        return self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)

    def _build_call_rotation(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "RectTransform_get_Rotation",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @property
    def scale(self) -> Tuple[float,float,float]:
        """
        Scale factor applied to the object in the x, y and z dimensions.
        """
        return self._client._invoke(
            "UI",
            "RectTransform_get_Scale",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @scale.setter
    def scale(self, value: Tuple[float,float,float]) -> None:
        return self._client._invoke(
            "UI",
            "RectTransform_set_Scale",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "RectTransform"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)],
            None
        )

    def _return_type_scale(self) -> TypeBase:
        return self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)

    def _build_call_scale(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "RectTransform_get_Scale",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @property
    def size(self) -> Tuple[float,float]:
        """
        Width and height of the rectangle.
        """
        return self._client._invoke(
            "UI",
            "RectTransform_get_Size",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)
        )

    @size.setter
    def size(self, value: Tuple[float,float]) -> None:
        return self._client._invoke(
            "UI",
            "RectTransform_set_Size",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "RectTransform"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)],
            None
        )

    def _return_type_size(self) -> TypeBase:
        return self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)

    def _build_call_size(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "RectTransform_get_Size",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)
        )

    @property
    def upper_right(self) -> Tuple[float,float]:
        """
        Position of the rectangles upper right corner relative to the anchors.
        """
        return self._client._invoke(
            "UI",
            "RectTransform_get_UpperRight",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)
        )

    @upper_right.setter
    def upper_right(self, value: Tuple[float,float]) -> None:
        return self._client._invoke(
            "UI",
            "RectTransform_set_UpperRight",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "RectTransform"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)],
            None
        )

    def _return_type_upper_right(self) -> TypeBase:
        return self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)

    def _build_call_upper_right(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "RectTransform_get_UpperRight",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "RectTransform")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type)
        )



class Text(ClassBase):
    """
    A text label. See UI.Panel#addText.
    """
    @property
    def alignment(self) -> TextAnchor:
        """
        Alignment.
        """
        return self._client._invoke(
            "UI",
            "Text_get_Alignment",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.enumeration_type("UI", "TextAnchor")
        )

    @alignment.setter
    def alignment(self, value: TextAnchor) -> None:
        return self._client._invoke(
            "UI",
            "Text_set_Alignment",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "Text"), self._client._types.enumeration_type("UI", "TextAnchor")],
            None
        )

    def _return_type_alignment(self) -> TypeBase:
        return self._client._types.enumeration_type("UI", "TextAnchor")

    def _build_call_alignment(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Text_get_Alignment",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.enumeration_type("UI", "TextAnchor")
        )

    @property
    def available_fonts(self) -> List[str]:
        """
        A list of all available fonts.
        """
        return self._client._invoke(
            "UI",
            "Text_get_AvailableFonts",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.list_type(self._client._types.string_type)
        )

    def _return_type_available_fonts(self) -> TypeBase:
        return self._client._types.list_type(self._client._types.string_type)

    def _build_call_available_fonts(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Text_get_AvailableFonts",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.list_type(self._client._types.string_type)
        )

    @property
    def color(self) -> Tuple[float,float,float]:
        """
        Set the color
        """
        return self._client._invoke(
            "UI",
            "Text_get_Color",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @color.setter
    def color(self, value: Tuple[float,float,float]) -> None:
        return self._client._invoke(
            "UI",
            "Text_set_Color",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "Text"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)],
            None
        )

    def _return_type_color(self) -> TypeBase:
        return self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)

    def _build_call_color(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Text_get_Color",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type)
        )

    @property
    def content(self) -> str:
        """
        The text string
        """
        return self._client._invoke(
            "UI",
            "Text_get_Content",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.string_type
        )

    @content.setter
    def content(self, value: str) -> None:
        return self._client._invoke(
            "UI",
            "Text_set_Content",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "Text"), self._client._types.string_type],
            None
        )

    def _return_type_content(self) -> TypeBase:
        return self._client._types.string_type

    def _build_call_content(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Text_get_Content",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.string_type
        )

    @property
    def font(self) -> str:
        """
        Name of the font
        """
        return self._client._invoke(
            "UI",
            "Text_get_Font",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.string_type
        )

    @font.setter
    def font(self, value: str) -> None:
        return self._client._invoke(
            "UI",
            "Text_set_Font",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "Text"), self._client._types.string_type],
            None
        )

    def _return_type_font(self) -> TypeBase:
        return self._client._types.string_type

    def _build_call_font(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Text_get_Font",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.string_type
        )

    @property
    def line_spacing(self) -> float:
        """
        Line spacing.
        """
        return self._client._invoke(
            "UI",
            "Text_get_LineSpacing",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.float_type
        )

    @line_spacing.setter
    def line_spacing(self, value: float) -> None:
        return self._client._invoke(
            "UI",
            "Text_set_LineSpacing",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "Text"), self._client._types.float_type],
            None
        )

    def _return_type_line_spacing(self) -> TypeBase:
        return self._client._types.float_type

    def _build_call_line_spacing(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Text_get_LineSpacing",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.float_type
        )

    @property
    def rect_transform(self) -> RectTransform:
        """
        The rect transform for the text.
        """
        return self._client._invoke(
            "UI",
            "Text_get_RectTransform",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.class_type("UI", "RectTransform")
        )

    def _return_type_rect_transform(self) -> TypeBase:
        return self._client._types.class_type("UI", "RectTransform")

    def _build_call_rect_transform(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Text_get_RectTransform",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.class_type("UI", "RectTransform")
        )

    @property
    def size(self) -> int:
        """
        Font size.
        """
        return self._client._invoke(
            "UI",
            "Text_get_Size",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.sint32_type
        )

    @size.setter
    def size(self, value: int) -> None:
        return self._client._invoke(
            "UI",
            "Text_set_Size",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "Text"), self._client._types.sint32_type],
            None
        )

    def _return_type_size(self) -> TypeBase:
        return self._client._types.sint32_type

    def _build_call_size(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Text_get_Size",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.sint32_type
        )

    @property
    def style(self) -> FontStyle:
        """
        Font style.
        """
        return self._client._invoke(
            "UI",
            "Text_get_Style",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.enumeration_type("UI", "FontStyle")
        )

    @style.setter
    def style(self, value: FontStyle) -> None:
        return self._client._invoke(
            "UI",
            "Text_set_Style",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "Text"), self._client._types.enumeration_type("UI", "FontStyle")],
            None
        )

    def _return_type_style(self) -> TypeBase:
        return self._client._types.enumeration_type("UI", "FontStyle")

    def _build_call_style(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Text_get_Style",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.enumeration_type("UI", "FontStyle")
        )

    @property
    def visible(self) -> bool:
        """
        Whether the UI object is visible.
        """
        return self._client._invoke(
            "UI",
            "Text_get_Visible",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.bool_type
        )

    @visible.setter
    def visible(self, value: bool) -> None:
        return self._client._invoke(
            "UI",
            "Text_set_Visible",
            [self, value],
            ["self", "value"],
            [self._client._types.class_type("UI", "Text"), self._client._types.bool_type],
            None
        )

    def _return_type_visible(self) -> TypeBase:
        return self._client._types.bool_type

    def _build_call_visible(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Text_get_Visible",
            [self],
            ["self"],
            [self._client._types.class_type("UI", "Text")],
            self._client._types.bool_type
        )

    def remove(self) -> None:
        """
        Remove the UI object.
        """
        return self._client._invoke(
            "UI",
            "Text_Remove",
            [self, ],
            ["self", ],
            [self._client._types.class_type("UI", "Text"), ],
            None
        )

    def _return_type_remove(self) -> TypeBase:
        return None

    def _build_call_remove(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Text_Remove",
            [self, ],
            ["self", ],
            [self._client._types.class_type("UI", "Text"), ],
            None
        )



class UI:
    """
    Provides functionality for drawing and interacting with in-game user interface elements.

    For drawing 3D objects in the flight scene, see the Drawing service.
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
        "Button": Button,
        "Canvas": Canvas,
        "InputField": InputField,
        "Panel": Panel,
        "RectTransform": RectTransform,
        "Text": Text,
    }
    _enumerations = {
        "FontStyle": FontStyle,
        "MessagePosition": MessagePosition,
        "TextAlignment": TextAlignment,
        "TextAnchor": TextAnchor,
    }
    _exceptions = {
    }

    @property
    def stock_canvas(self) -> Canvas:
        """
        The stock UI canvas.
        """
        return self._client._invoke(
            "UI",
            "get_StockCanvas",
            [],
            [],
            [],
            self._client._types.class_type("UI", "Canvas")
        )

    def _return_type_stock_canvas(self) -> TypeBase:
        return self._client._types.class_type("UI", "Canvas")

    def _build_call_stock_canvas(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "get_StockCanvas",
            [],
            [],
            [],
            self._client._types.class_type("UI", "Canvas")
        )

    def add_canvas(self) -> Canvas:
        """
        Add a new canvas.

        If you want to add UI elements to KSPs stock UI canvas, use UI#stockCanvas.
        """
        return self._client._invoke(
            "UI",
            "AddCanvas",
            [],
            [],
            [],
            self._client._types.class_type("UI", "Canvas")
        )

    def _return_type_add_canvas(self) -> TypeBase:
        return self._client._types.class_type("UI", "Canvas")

    def _build_call_add_canvas(self) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "AddCanvas",
            [],
            [],
            [],
            self._client._types.class_type("UI", "Canvas")
        )

    def clear(self, client_only: bool = False) -> None:
        """
        Remove all user interface elements.

        :param client_only: If true, only remove objects created by the calling client.
        """
        return self._client._invoke(
            "UI",
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
            "UI",
            "Clear",
            [client_only],
            ["client_only"],
            [self._client._types.bool_type],
            None
        )

    def message(self, content: str, duration: float = 1.0, position: MessagePosition = MessagePosition(1), color: Tuple[float,float,float] = (1.0, 0.92, 0.016), size: float = 20.0) -> None:
        """
        Display a message on the screen.

        The message appears just like a stock message, for example quicksave or quickload messages.

        :param content: Message content.

        :param duration: Duration before the message disappears, in seconds.

        :param position: Position to display the message.

        :param size: Size of the message, differs per position.

        :param color: The color of the message.
        """
        return self._client._invoke(
            "UI",
            "Message",
            [content, duration, position, color, size],
            ["content", "duration", "position", "color", "size"],
            [self._client._types.string_type, self._client._types.float_type, self._client._types.enumeration_type("UI", "MessagePosition"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type), self._client._types.float_type],
            None
        )

    def _return_type_message(self) -> TypeBase:
        return None

    def _build_call_message(self, content: str, duration: float = 1.0, position: MessagePosition = MessagePosition(1), color: Tuple[float,float,float] = (1.0, 0.92, 0.016), size: float = 20.0) -> KRPC_pb2.ProcedureCall:
        return self._client._build_call(
            "UI",
            "Message",
            [content, duration, position, color, size],
            ["content", "duration", "position", "color", "size"],
            [self._client._types.string_type, self._client._types.float_type, self._client._types.enumeration_type("UI", "MessagePosition"), self._client._types.tuple_type(self._client._types.double_type, self._client._types.double_type, self._client._types.double_type), self._client._types.float_type],
            None
        )
