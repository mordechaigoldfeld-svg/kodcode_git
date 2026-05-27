from calculator import Shape
from math import pi



class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def get_area(self):
        return pi*self.radius**2
    def get_perimeter(self):
        return 2*pi*self.radius
    def __str__(self):
        return f'shape:Circle\nArea{self.get_area():.1f}\nPerimeter:{self.get_perimeter():.1f}'




