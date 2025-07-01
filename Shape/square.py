from .point import Point
from .rectangle import Rectangle

# square.py
class Square(Rectangle):
    def __init__(self, center: Point, side_length: float):
        super().__init__(2, center, side_length, side_length)
        self.is_regular = True
