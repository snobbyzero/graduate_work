from classes.BaseElement import BaseElement


class IconElement(BaseElement):
    def __init__(
            self,
            x,
            y,
            col_count,
            row_count,
            order: int,
            parent=None,
            children: [] = None,
            width: int = None,
            height: int = None,
            min_width: int = 0,
            min_height: int = 0,
            max_width: int = None,
            max_height: int = None,
            label: str = "i",
            name: str = "icon",
            link: str = "",
            icon_width: int = 50,
            icon_height: int = 50,
    ):
        self.name = name
        self.link = link
        self.icon_width = icon_width
        self.icon_height = icon_height
        BaseElement.__init__(
            self,
            x=x,
            y=y,
            col_count=col_count,
            row_count=row_count,
            order=order,
            parent=parent,
            children=children,
            width=width,
            height=height,
            min_width=min_width,
            min_height=min_height,
            max_width=max_width,
            max_height=max_height,
            label=label
        )
