class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of Circle =", 3.14 * self.radius * self.radius)


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area of Rectangle =", self.length * self.breadth)


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print("Area of Triangle =", 0.5 * self.base * self.height)


c = Circle(5)
r = Rectangle(10, 4)
t = Triangle(6, 8)

c.area()
r.area()
t.area()