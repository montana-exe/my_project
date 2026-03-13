class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        return self.area() + other.area()

rect1 = Rectangle(3, 4)
rect2 = Rectangle(5, 6)
print("Сумма площадей:", rect1 + rect2)
