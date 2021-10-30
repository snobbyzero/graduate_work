from classes.BaseElement import BaseElement


class IconsListElement(BaseElement):
    def __init__(
            self,
            x,
            y,
            col_count,
            row_count,
            margin_right,  # for solver
            margin_left,  # for solver
            margin_bottom,  # for solver
            margin_top,  # for solver
            order: int,
            mutable_elements=None,  # for solver
            is_fullwidth: bool = False,
            is_fullheight: bool = False,
            is_flexwidth: bool = False,
            is_flexheight: bool = False,
            justify_left: bool = False,
            justify_right: bool = False,
            justify_center: bool = False,
            center_horizontal: bool = False,  # for children
            center_vertical: bool = False,
            is_top: bool = False,
            is_bottom: bool = False,
            is_left: bool = False,
            is_right: bool = False,
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
            x=x,
            y=y,
            col_count=col_count,
            row_count=row_count,
            margin_right=margin_right,
            margin_left=margin_left,
            margin_bottom=margin_bottom,
            margin_top=margin_top,
            order=order,
            mutable_elements=mutable_elements,
            is_fullwidth=is_fullwidth,
            is_fullheight=is_fullheight,
            is_flexwidth=is_flexwidth,
            is_flexheight=is_flexheight,
            justify_left=justify_left,
            justify_right=justify_right,
            justify_center=justify_center,
            center_horizontal=center_horizontal,
            center_vertical=center_vertical,
            is_top=is_top,
            is_bottom=is_bottom,
            is_left=is_left,
            is_right=is_right,
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

    def add_children(self, children):
        self.children = children
        self.min_width = sum([i.width + i.min_margin_left + i.min_margin_right for i in children])
        self.min_height = max([i.height + i.min_margin_top + i.min_margin_bottom for i in children])
        self.max_width = sum([i.width + i.max_margin_left + i.max_margin_right for i in children])
        self.max_height = max([i.height + i.max_margin_top + i.max_margin_bottom for i in children])
