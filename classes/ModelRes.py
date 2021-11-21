class ModelRes:
    def __init__(self, m, res_arr, parent=None):
        self.m = m
        self.children = []
        self.res_arr = res_arr
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)