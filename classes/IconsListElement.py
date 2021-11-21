from classes.BaseElement import BaseElement


class IconsListElement(BaseElement):
    def __init__(
            self,
            name,
            right_elements=None,  # this elements can be righter than this
            left_elements=None,
            top_elements=None,
            bottom_elements=None,
            rules=None,  # for solver
            is_vertical=False,
            is_fullwidth: bool = False,
            is_fullheight: bool = False,
            is_flexwidth: bool = False,
            is_flexheight: bool = False,
            justify_left: bool = False,
            justify_right: bool = False,
            justify_center: bool = False,
            center_horizontal: bool = False,  # for children
            center_vertical: bool = False,
            parent=None,
            children: [] = None,
            table=None,
            min_margin_right=0,
            min_margin_left=0,
            min_margin_top=0,
            min_margin_bottom=0,
            max_margin_right=0,
            max_margin_left=0,
            max_margin_top=0,
            max_margin_bottom=0,
            label: str = "i",
    ):
        BaseElement.__init__(
            self,
            name,
            right_elements=right_elements,
            left_elements=left_elements,
            top_elements=top_elements,
            bottom_elements=bottom_elements,
            rules=rules,
            is_fullwidth=is_fullwidth,
            is_fullheight=is_fullheight,
            is_flexwidth=is_flexwidth,
            is_flexheight=is_flexheight,
            justify_left=justify_left,
            justify_right=justify_right,
            justify_center=justify_center,
            center_horizontal=center_horizontal,
            center_vertical=center_vertical,
            parent=parent,
            children=children,
            table=table,
            min_width=None,
            min_height=None,
            max_width=None,
            max_height=None,
            min_margin_right=min_margin_right,
            min_margin_left=min_margin_left,
            min_margin_top=min_margin_top,
            min_margin_bottom=min_margin_bottom,
            max_margin_right=max_margin_right,
            max_margin_left=max_margin_left,
            max_margin_top=max_margin_top,
            max_margin_bottom=max_margin_bottom,
            label=label
        )
        self.is_vertical = is_vertical

    def add_children(self, children):
        self.children = children
        if self.is_vertical:
            self.min_width = max([i.width + i.min_margin_left + i.min_margin_right for i in children])
            self.min_height = sum([i.height + i.min_margin_top + i.min_margin_bottom for i in children])
            self.max_width = max([i.width + i.max_margin_left + i.max_margin_right for i in children])
            self.max_height = sum([i.height + i.max_margin_top + i.max_margin_bottom for i in children])
        else:
            self.min_width = sum([i.width + i.min_margin_left + i.min_margin_right for i in children])
            self.min_height = max([i.height + i.min_margin_top + i.min_margin_bottom for i in children])
            self.max_width = sum([i.width + i.max_margin_left + i.max_margin_right for i in children])
            self.max_height = max([i.height + i.max_margin_top + i.max_margin_bottom for i in children])
