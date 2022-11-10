from math import pi, sqrt

class Triangle:
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    def square(self):
        per = self.perimeter() / 2
        return sqrt(per * (per - self.side_1) * (per - self.side_2) * (per - self.side_3))

trian = Triangle(5, 5, 5)
print(trian.perimeter())
print(trian.square())

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def length(self):
        return 2 * pi * self.radius

    def square(self):
        return pi * (self.radius ** 2)

circ = Circle(4)
print(circ.length())
print(circ.square())



