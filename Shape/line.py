# line.py
class Line:
    def __init__(self, start_point, end_point):
        self.start = start_point
        self.end = end_point
        self.length = self.start.distance_to(self.end)
