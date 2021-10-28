import json

from json_classes.Measure import Measure
from json_classes.ValueJSON import ValueJSON


class BaseElementJSON:
    def __init__(
            self,
            tag,
            parent=None,
            children=None,
            attrs=None,
            text="",
            x=ValueJSON(0, Measure.PERCENT),
            y=ValueJSON(0, Measure.PERCENT),
            width=ValueJSON(0, Measure.PERCENT),
            height=ValueJSON(0, Measure.PERCENT),
            fullwidth=False,
            fullheight=False,
            flexgrow=0,
            flexflow="row wrap",
            center_horizontal=False,
            center_vertical=False,
            justify_left=False,
            justify_right=False,
            font_size: ValueJSON = ValueJSON(1, Measure.EM),
            margin_right=0,
            margin_left=0,
            margin_top=0,
            margin_bottom=0,
            padding_right=0,
            padding_left=0,
            padding_top=0,
            padding_bottom=0
    ):
        if attrs is None:
            self.attrs = []
        if children is None:
            self.children = []
        self.parent = parent

        self.tag = tag

        self.text = text

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fullwidth = fullwidth
        self.fullheight = fullheight

        self.flexgrow = flexgrow
        self.flexflow = flexflow

        self.center_horizontal = center_horizontal
        self.center_vertical = center_vertical
        self.justify_left = justify_left
        self.justify_right = justify_right

        if parent is not None:
            self.left = self.x.val == 0
            self.right = (self.x.val + self.width.val) == parent.width.val
            self.top = self.y.val == 0
            self.bottom = (self.y.val + self.height.val) == parent.height.val
        else:
            self.left = False
            self.right = False
            self.top = False
            self.bottom = False
        self.font_size = font_size

        self.margin_right = margin_right
        self.margin_left = margin_left
        self.margin_top = margin_top
        self.margin_bottom = margin_bottom

        self.padding_right = padding_right
        self.padding_left = padding_left
        self.padding_bottom = padding_bottom
        self.padding_top = padding_top
