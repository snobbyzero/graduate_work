from classes.BaseElement import BaseElement


class IconsListElement(BaseElement):
    def __init__(
            self,
            x,
            y,
            col_count,
            row_count,
            order: int,
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
            width: int = None,
            height: int = None,
            label: str = "i",
    ):
        BaseElement.__init__(
            self,
            x=x,
            y=y,
            col_count=col_count,
            row_count=row_count,
            order=order,
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
            width=width,
            height=height,
            min_width=None,
            min_height=None,
            max_width=None,
            max_height=None,
            label=label
        )

    def add_children(self, children):
        self.children = children
        self.min_width = sum([i.icon_width for i in children])
        self.min_height = max([i.icon_height for i in children])
        self.max_width = sum([i.icon_width for i in children])
        self.max_height = max([i.icon_height for i in children])
