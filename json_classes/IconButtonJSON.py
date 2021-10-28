import json

from json_classes.BaseElementJSON import BaseElementJSON
from json_classes.Measure import Measure
from json_classes.ValueJSON import ValueJSON


class IconButtonJSON(BaseElementJSON):
    def __init__(self,
                 icon_name,
                 parent=None,
                 children=None,
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
        BaseElementJSON.__init__(
            self,
            tag="button",
            parent=parent,
            children=children,
            attrs=attrs,
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
        self.icon_name = icon_name
        self.set_icon(icon_name)

    def set_icon(self, icon_name):
        if icon_name == 'profile':
            self.attrs.append(('class', 'fa fa-user'))
        elif icon_name == 'cart':
            self.attrs.append(('class', 'fa fa-shopping-cart'))
        elif icon_name == 'vk':
            self.attrs.append(('class', 'fa fa-vk'))
        elif icon_name == 'twitter':
            self.attrs.append(('class', 'fa fa-twitter'))
        elif icon_name == 'facebook':
            self.attrs.append(('class', 'fa fa-facebook'))

