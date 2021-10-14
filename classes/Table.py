import math


class Table:
    def __init__(self, cell_width: int, cell_height: int, row_count: int = None, col_count: int = None,
                 width: int = None, height: int = None):
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.row_count = row_count
        self.col_count = col_count
        if self.col_count is None and width is not None:
            self.col_count = self.get_col_count_from_width(width)
        if self.row_count is None and height is not None:
            self.row_count = self.get_row_count_from_height(height)
        self.matrix = [[0 for _ in range(self.col_count)] for _ in range(self.row_count)]

    def get_col_count_from_width(self, width):
        return int(math.ceil(width / self.cell_width))

    def get_row_count_from_height(self, height):
        return int(math.ceil(height / self.cell_height))

    def get_size(self):
        return self.cell_width * self.col_count, self.cell_height * self.row_count

    def get_height(self):
        return self.cell_height * self.row_count

    def get_width(self):
        return self.cell_width * self.col_count

    def __str__(self):
        return '\n'.join('\t'.join(str(x) for x in y) for y in self.matrix)
