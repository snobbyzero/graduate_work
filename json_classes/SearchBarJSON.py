from json_classes.BaseElementJSON import BaseElementJSON
from json_classes.Measure import Measure
from json_classes.ValueJSON import ValueJSON


class SearchBarJSON(BaseElementJSON):
    def __init__(self,
                 parent=None,
                 attrs: [] = None,
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
        else:
            self.attrs = attrs
        self.attrs.append(('type', 'text'))
        self.attrs.append(('placeholder', 'Search'))
        BaseElementJSON.__init__(
            self,
            tag="input",
            parent=parent,
            attrs=self.attrs,
            text=text,
            x=x,
            y=y,
            width=width,
            height=height,
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
