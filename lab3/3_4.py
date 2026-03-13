import math

class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

square = Square(5)
circle = Circle(3)
print("Площадь квадрата:", square.area())
print("Периметр круга:", circle.perimeter())
