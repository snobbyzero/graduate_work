class BaseElement:
    def __init__(
            self,
            x,  # for solver
            y,  # for solver
            col_count,  # for solver
            row_count,  # for solver
            order: int,  # 0 = left, 2 = right, 1 = between 0 and 2
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
            min_width: int = 0,
            min_height: int = 0,
            max_width: int = None,
            max_height: int = None,
            label: str = "b"
    ):
        # coordinates inside parent
        self.x = x
        self.y = y

        self.col_count = col_count
        self.row_count = row_count

        self.order = order

        self.parent = parent

        if children is None:
            self.children = []

        if table is not None:
            self.table = table
        else:
            self.table = None

        self.width = width
        self.height = height

        self.is_fullwidth = is_fullwidth
        self.is_fullheight = is_fullheight

        self.is_flexwidth = is_flexwidth
        self.is_flexheight = is_flexheight

        self.is_top = is_top
        self.is_bottom = is_bottom
        self.is_left = is_left
        self.is_right = is_right

        self.justify_left = justify_left
        self.justify_right = justify_right
        self.justify_center = justify_center

        self.center_horizontal = center_horizontal
        self.center_vertical = center_vertical

        if is_fullwidth:
            self.min_width = parent.width
            self.max_width = parent.width
        elif is_flexwidth:
            if min_width:
                self.min_width = min_width
            else:
                self.min_width = 0
            self.max_width = parent.width
        else:
            self.min_width = min_width
            if max_width or parent is None:
                self.max_width = max_width
            else:
                self.max_width = parent.width

        if is_fullheight:
            self.min_height = parent.height
            self.max_height = parent.height
        elif is_flexheight:
            if min_height:
                self.min_height = min_height
            else:
                self.min_height = 0
            self.max_height = parent.height
        else:
            self.min_height = min_height
            if max_height or parent is None:
                self.max_height = max_height
            else:
                self.max_height = parent.height

        self.label = label

    def add_children(self, children):
        self.children = children

    def get_width_with_parent(self, model):
        return self.parent.table.cell_width * model[self.col_count].as_long()

    def get_height_with_parent(self, model):
        return self.parent.table.cell_height * model[self.row_count].as_long()
