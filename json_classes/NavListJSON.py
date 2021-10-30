import json

from json_classes.BaseElementJSON import BaseElementJSON
from json_classes.Measure import Measure
from json_classes.ValueJSON import ValueJSON


class NavListJSON(BaseElementJSON):
    def __init__(self,
                 nav_list,
                 x,  # needs only for sorting
                 y,  # needs only for sorting
                 width,
                 height,
                 margin_right,
                 margin_left,
                 margin_top,
                 margin_bottom,
                 label,
                 text_align="center",
                 min_width=None,
                 min_height=None,
                 parent=None,
                 children=None,
                 attrs: [] = None,
                 fullwidth=False,
                 fullheight=False,
                 flexgrow=0,
                 flexflow="row wrap",
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
        BaseElementJSON.__init__(
            self,
            tag="nav",
            parent=parent,
            children=children,
            attrs=attrs,
            x=x,
            y=y,
            width=width,
            height=height,
            min_width=min_width,
            min_height=min_height,
            label=label,
            fullwidth=fullwidth,
            fullheight=fullheight,
            flexgrow=flexgrow,
            flexflow=flexflow,
            center_horizontal=center_horizontal,
            center_vertical=center_vertical,
            justify_left=justify_left,
            justify_right=justify_right,
            font_size=font_size,
            margin_right=margin_right,
            margin_left=margin_left,
            margin_top=margin_top,
            margin_bottom=margin_bottom,
            padding_right=padding_right,
            padding_left=padding_left,
            padding_top=padding_top,
            padding_bottom=padding_bottom
        )
        self.nav_list = nav_list
        self.set_children()

    def set_children(self):
        for link in self.nav_list:
            self.children.append(BaseElementJSON(
                "a",
                label="nav-a",
                x=0,
                y=0,
                width=ValueJSON("auto", Measure.WORD),
                height=ValueJSON("auto", Measure.WORD),
                margin_right=ValueJSON(1, Measure.EM),
                margin_left=ValueJSON(0, Measure.EM),
                margin_top=ValueJSON(0, Measure.EM),
                margin_bottom=ValueJSON(0, Measure.EM),
                padding_right=ValueJSON(1, Measure.REM),
                padding_left=ValueJSON(1, Measure.REM),
                padding_top=ValueJSON(1, Measure.REM),
                padding_bottom=ValueJSON(1, Measure.REM),
                text=link,
                text_align=self.text_align
            ))
