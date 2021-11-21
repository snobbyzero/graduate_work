from json_classes.BaseElementJSON import BaseElementJSON
from json_classes.Measure import Measure
from json_classes.ValueJSON import ValueJSON


class SearchBarJSON(BaseElementJSON):
    def __init__(self,
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
                 attrs: [] = None,
                 text="",
                 min_width=None,
                 min_height=None,
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
        self.attrs.append(('type', 'text'))
        self.attrs.append(('placeholder', 'Search'))
        BaseElementJSON.__init__(
            self,
            tag="input",
            parent=parent,
            attrs=self.attrs,
            text=text,
            text_align="left",
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
            align_content=align_content,
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
