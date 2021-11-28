from classes.BaseElement import BaseElement


class CardElement(BaseElement):
    def __init__(
            self,
            name,
            size="sm",
            right_elements=None,  # this elements can be righter than this
            left_elements=None,
            top_elements=None,
            bottom_elements=None,
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
            center_horizontal=False,
            center_vertical=False,
            label: str = "c",
    ):
        self.size = size
        BaseElement.__init__(
            self,
            name,
            right_elements=right_elements,
            left_elements=left_elements,
            top_elements=top_elements,
            bottom_elements=bottom_elements,
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
            center_horizontal=center_horizontal,
            center_vertical=center_vertical,
            label=label
        )
