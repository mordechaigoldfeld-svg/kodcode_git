from rectangle import Rectangle



class Square(Rectangle):
    def __init__(self,side):
        super().__init__(width=side,height=side)
        self.side=side
    def get_area(self):
        return super().get_area()
    def get_perimeter(self):
        return 4*self.side
    def __str__(self):
        return f'shape:Square\nArea{self.get_area()}\nPerimeter:{self.get_perimeter()}'


