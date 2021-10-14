from classes.BaseElement import BaseElement


class ListElement(BaseElement):
    def __init__(
            self,
            row_x: int = None,
            col_y: int = None,
            is_fullwidth: bool = False,
            is_fullheight: bool = False,
            is_flexwidth: bool = False,
            is_flexheight: bool = False,
            parent=None,
            children: [] = None,
            table=None,
            width: int = None,
            height: int = None,
            max_width: int = None,
            max_height: int = None,
            label: str = "b",
            links_list=None
    ):
        self.links_list = links_list
        BaseElement.__init__(
            self,
            row_x=row_x,
            col_y=col_y,
            is_fullwidth=is_fullwidth,
            is_fullheight=is_fullheight,
            is_flexwidth=is_flexwidth,
            is_flexheight=is_flexheight,
            parent=parent,
            children=children,
            table=table,
            width=width,
            height=height,
            min_width=self.links_list.min_width,
            min_height=self.links_list.min_height,
            max_width=max_width,
            max_height=max_height,
            label=label
        )
