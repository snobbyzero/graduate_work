import json
import random

from json_classes.BaseElementJSON import BaseElementJSON
from json_classes.Measure import Measure
from json_classes.ValueJSON import ValueJSON


class IconButtonJSON(BaseElementJSON):
    def __init__(self,
                 icon_name,
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
                 attrs: [] = None,
                 text="",
                 text_align="center",
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
                 padding_bottom=ValueJSON(0, Measure.EM),
                 css={}
                 ):
        BaseElementJSON.__init__(
            self,
            tag="i",
            parent=parent,
            children=children,
            attrs=attrs,
            text=text,
            text_align=text_align,
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
            padding_bottom=padding_bottom,
            css=css
        )
        self.icon_name = icon_name
        self.set_icon(icon_name)

    def set_icon(self, icon_name):
        if icon_name == 'profile':
            self.attrs.append(('class', 'far fa-user'))
        elif icon_name == 'cart':
            self.attrs.append(('class', 'far fa-shopping-cart'))
        elif icon_name == 'vk':
            self.attrs.append(('class', 'fab fa-vk'))
        elif icon_name == 'twitter':
            self.attrs.append(('class', 'fab fa-twitter'))
        elif icon_name == 'facebook':
            self.attrs.append(('class', 'fab fa-facebook'))
        elif icon_name == 'github':
            self.attrs.append(('class', 'fab fa-github'))
        elif icon_name == 'wishlist':
            self.attrs.append(('class', 'far fa-heart'))
        elif icon_name == 'compare':
            self.attrs.append(('class', 'far fa-chart-bar'))
        elif icon_name == 'rating':
            self.attrs.append(('class', 'far fa-star'))
        elif icon_name == 'comment':
            self.attrs.append(('class', 'far fa-comment'))
        elif icon_name == 'search':
            self.attrs.append(('class', 'fas fa-search'))
        else:
            self.attrs.append(('class', f'far fa-{icon_name}'))
