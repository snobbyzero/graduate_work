from classes.BaseElement import BaseElement


class IconElement(BaseElement):
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
            parent=None,
            children: [] = None,
            width: int = None,
            height: int = None,
            min_width: int = 0,
            min_height: int = 0,
            max_width: int = None,
            max_height: int = None,
            min_margin_right=0,
            min_margin_left=0,
            min_margin_top=0,
            min_margin_bottom=0,
            max_margin_right=0,
            max_margin_left=0,
            max_margin_top=0,
            max_margin_bottom=0,
            label: str = "i",
            name: str = "icon",
            link: str = "",
    ):
        self.name = name
        self.link = link
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
            parent=parent,
            children=children,
            width=width,
            height=height,
            min_width=min_width,
            min_height=min_height,
            max_width=max_width,
            max_height=max_height,
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
