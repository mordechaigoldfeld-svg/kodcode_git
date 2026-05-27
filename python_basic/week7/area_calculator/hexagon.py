from calculator import Shape
from math import sqrt


class Hexagon(Shape):
    def __init__(self,side):
        self.side=side
    def get_area(self):
        return (3*sqrt(3)*self.side**2)/2
    def get_perimeter(self):
        return 6*self.side
    def __str__(self):
        return f'shape:Square\nArea{self.get_area():.1f}\nPerimeter:{self.get_perimeter()}'
