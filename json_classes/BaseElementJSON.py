import json

from json_classes.Measure import Measure
from json_classes.ValueJSON import ValueJSON


class BaseElementJSON:
    def __init__(
            self,
            tag,
            x,  # needs only for sorting
            y,  # needs only for sorting
            width,
            height,
            margin_right,
            margin_left,
            margin_top,
            margin_bottom,
            label,
            parent=None,
            children=None,
            attrs=None,
            text="",
            text_align="center",
            min_width=ValueJSON(0, Measure.PERCENT),
            min_height=ValueJSON(0, Measure.PERCENT),
            fullwidth=False,
            fullheight=False,
            flexgrow=0,
            flexflow="row wrap",
            align_content="normal",
            center_horizontal=False,
            center_vertical=False,
            justify_left=False,
            justify_right=False,
            font_size: ValueJSON = ValueJSON(1, Measure.EM),
            padding_right=ValueJSON(0, Measure.EM),
            padding_left=ValueJSON(0, Measure.EM),
            padding_top=ValueJSON(0, Measure.EM),
            padding_bottom=ValueJSON(0, Measure.EM)
    ):
        if attrs is None:
            self.attrs = []
        else:
            self.attrs = attrs
        if children is None:
            self.children = []
        self.parent = parent

        self.tag = tag

        self.text = text
        self.text_align = text_align

        self.label = label

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.min_width = min_width
        self.min_height = min_height

        self.fullwidth = fullwidth
        self.fullheight = fullheight

        self.align_content = align_content

        if flexgrow:
            self.flexgrow = 1
        else:
            self.flexgrow = 0
        #if flexgrow == 1:
        #    self.width = ValueJSON(0, Measure.PERCENT)
        self.flexflow = flexflow

        self.center_horizontal = center_horizontal
        self.center_vertical = center_vertical
        self.justify_left = justify_left
        self.justify_right = justify_right

        self.font_size = font_size

        self.margin_right = margin_right
        self.margin_left = margin_left
        self.margin_top = margin_top
        self.margin_bottom = margin_bottom

        self.padding_right = padding_right
        self.padding_left = padding_left
        self.padding_bottom = padding_bottom
        self.padding_top = padding_top
