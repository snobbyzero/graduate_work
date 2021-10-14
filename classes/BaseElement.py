class BaseElement:
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
            min_width: int = None,
            min_height: int = None,
            max_width: int = None,
            max_height: int = None,
            label: str = "b"
    ):
        # coordinates inside parent
        self.row_x = row_x
        self.col_y = col_y

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

        self.min_width = min_width
        self.min_height = min_height
        self.max_width = max_width
        self.max_height = max_height

        self.label = label

    def add_children(self, child_element):
        child_element.parent = self
        self.children.append(child_element)
