from json_classes.Measure import Measure


class ValueJSON:

    def __init__(self, val, measure: Measure):
        self.val = val
        self.measure = measure

    def __str__(self):
        if self.measure == Measure.WORD:
            return self.measure.value
        return f"{self.val}{self.measure.value}"