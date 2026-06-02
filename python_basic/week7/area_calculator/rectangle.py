from calculator import Shape


class Rectangle(Shape):
    def __init__(self,width,height):
        super().__init__()
        self.width=width
        self.height=height
    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*(self.height+self.width)

    def __str__(self):
        return f'shape:Rectangle\nArea:{self.get_area()}\nPerimeter:{self.get_perimeter()}'


