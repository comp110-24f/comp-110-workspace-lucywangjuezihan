class Coordinate:
    x1: float
    y1: float
    x2: float
    y2: float

    def __init__(self, x1: float, y1: float):
        self.x = x1
        self.y = y1

    def get_dist(self, other, x2: float, y2: float) -> float:
        """Get distance from this coord to other coord"""
        other.x = x2
        other.y = y2
        x_diffs: float = self.x - other.x
        y_diffs: float = self.y - other.y
        return y_diffs / x_diffs
