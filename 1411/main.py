from math import pi

class NotValidFigure(Exception):
    pass

class Triangle:
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        if not self.is_valid():
            raise NotValidFigure
    
    def is_valid(self):
        sides = [self.side_1, self.side_2, self.side_3]
        if all([isinstance(side,(int, float)) for side in sides]): 
            if all([side > 0 for side in sides]):
                sorted_sides = sorted(sides)
                return sorted_sides[-1] < sorted_sides[0] + sorted_sides[1]
        
    def perimeter(self):
        return round(self.side_1 + self.side_2 + self.side_3, 3)
    
    def square(self):
        per = self.perimeter() / 2
        return round((per * (per - self.side_1) * (per - self.side_2) * (per - self.side_3)) ** 0.5, 3)
    
trian = Triangle(.2, .2, .2)
print(trian.perimeter())
print(trian.square())


class Circle:
    def __init__(self, radius):
        self.radius = radius
        if not self.is_valid():
            raise NotValidFigure

    def is_valid(self):
        if isinstance(self.radius, (int, float)):
            return self.radius > 0
        
    def length(self):
        return round(2 * pi * self.radius, 3)

    def square(self):
        return round(pi * (self.radius ** 2), 3)

circ = Circle(3)
print(circ.radius)
print(circ.length())
print(circ.square())