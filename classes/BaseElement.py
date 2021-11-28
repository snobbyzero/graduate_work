from z3 import *


class BaseElement:
    def __init__(
            self,
            name,
            right_elements=None,  # this elements can be righter than this
            left_elements=None,
            top_elements=None,
            bottom_elements=None,
            rules=None,  # for solver
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
            label: str = "b"
    ):
        self.name = name
        # coordinates inside parent
        if bottom_elements is None:
            self.bottom_elements = []
        else:
            self.bottom_elements = []
        if top_elements is None:
            self.top_elements = []
        else:
            self.top_elements = top_elements
        if left_elements is None:
            self.left_elements = []
        else:
            self.left_elements = left_elements
        if right_elements is None:
            self.right_elements = []
        else:
            self.right_elements = right_elements
        self.x = Int(name + "_x")
        self.y = Int(name + "_y")

        self.col_count = Int(name + "_col_count")
        self.row_count = Int(name + "_row_count")

        self.margin_right = Int(name + "_margin_right")
        self.margin_left = Int(name + "_margin_left")
        self.margin_bottom = Int(name + "_margin_bottom")
        self.margin_top = Int(name + "_margin_top")

        self.models = []

        self.parent = parent

        if children is None:
            self.children = []

        if table is not None:
            self.table = table
        else:
            self.table = None

        if rules is None:
            self.rules = []
        else:
            self.rules = rules

        self.width = width
        self.height = height

        self.is_fullwidth = is_fullwidth
        self.is_fullheight = is_fullheight

        self.is_flexwidth = is_flexwidth
        self.is_flexheight = is_flexheight

        self.justify_left = justify_left
        self.justify_right = justify_right
        self.justify_center = justify_center

        self.center_horizontal = center_horizontal
        self.center_vertical = center_vertical

        #if is_fullwidth:
        #    self.min_width = parent.width
        #    self.max_width = parent.width
        #elif is_flexwidth:
        #    if min_width:
        #        self.min_width = min_width
        #    else:
        #        self.min_width = 0
        #    self.max_width = parent.width
        if width is not None:
            self.min_width = width
            self.max_width = width
        else:
            self.min_width = min_width
            if max_width or parent is None:
                self.max_width = max_width
            else:
                self.max_width = parent.width

        #if is_fullheight:
        #    self.min_height = parent.height
        #    self.max_height = parent.height
        #elif is_flexheight:
        #    if min_height:
        #        self.min_height = min_height
        #    else:
        #        self.min_height = 0
        #    self.max_height = parent.height
        if height is not None:
            self.min_height = height
            self.max_height = height
        else:
            self.min_height = min_height
            if max_height or parent is None:
                self.max_height = max_height
            else:
                self.max_height = parent.height

        self.min_margin_right = min_margin_right
        self.min_margin_left = min_margin_left
        self.min_margin_top = min_margin_top
        self.min_margin_bottom = min_margin_bottom
        self.max_margin_right = max_margin_right
        self.max_margin_left = max_margin_left
        self.max_margin_top = max_margin_top
        self.max_margin_bottom = max_margin_bottom

        self.label = label

    def add_children(self, children):
        self.children = children

    def add_child(self, child):
        self.children.append(child)

    def add_model(self, model):
        self.models.append(model)

    def set_neighbours(self, right_elements=None, left_elements=None, top_elements=None, bottom_elements=None):
        if bottom_elements is not None:
            self.bottom_elements = bottom_elements
        if top_elements is not None:
            self.top_elements = top_elements
        if left_elements is not None:
            self.left_elements = left_elements
        if right_elements is not None:
            self.right_elements = right_elements

    def get_width_with_parent(self, model):
        return self.parent.table.cell_width * model[self.col_count].as_long()

    def get_height_with_parent(self, model):
        return self.parent.table.cell_height * model[self.row_count].as_long()

    def set_min_size_by_children(self):
        self.min_width = max([child.min_width + child.min_margin_left + child.min_margin_right for child in self.children])
        self.min_height = max([child.min_height + child.min_margin_bottom + child.min_margin_top for child in self.children])

    def set_max_size_by_children(self):
        self.max_width = sum([child.max_width + child.max_margin_left + child.max_margin_right for child in self.children])
        self.max_height = sum([child.max_height + child.margin_bottom + child.max_margin_top for child in self.children])