from rectangle import Rectangle


class Triangle(Rectangle):
    def __init__(self,base,height,side1,side2,side3):
        super().__init__(width=base,height=height)
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def get_area(self):
      return  super().get_area()/2
    def get_perimeter(self):
        return self.side1+self.side2+self.side3
    def __str__(self):
        return f'shape:Triangle\nArea{self.get_area()}\nPerimeter:{self.get_perimeter()}'

