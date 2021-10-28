from json_classes.Measure import Measure


class ValueJSON:

    def __init__(self, val, measure: Measure):
        self.val = val
        self.unit = measure
