from math import sqrt


class Polygon:

    def __init__(self, n_sides, len):
        self.n_sides = n_sides
        self.len = len

    def perimeter(self):
        print(f"Soy un polígono con perímetro")

    def area(self):
        print(f"Soy un polígono con área")


class Square(Polygon):

    def area(self):
        print(f"Área: {self.len * self.len} u^2")

    def perimeter(self):
        print(f"Perímetro: {self.len * self.n_sides} u")


class Triangle(Polygon):
    def __init__(self, n_sides, a, b, c):
        """a,b,c are the len of each side"""
        self.n_sides = n_sides
        self.a = a
        self.b = b
        self.c = c
        self.semiperimeter = (self.a + self.b + self.c) / 2

    def area(self):
        """"Calculated using the semiperimeter method"""
        print(
            f"Área: {(self.semiperimeter * (self.semiperimeter - self.a) * (self.semiperimeter - self.b) * (self.semiperimeter - self.c)) ** 0.5} u^2")

    def perimeter(self):
        print(f"Perímetro: {self.semiperimeter * 2} u")


class Pentagon(Polygon):
    def area(self):
        res = (sqrt(5 * (5 + 2 * (sqrt(5)))) * self.len * self.len) / 4
        print(f"Área: {res} u^2")

    def perimeter(self):
        print(f"Perímetro: {self.len * 5} u")


if __name__ == "__main__":
    s = Square(4, 5)
    s.area()
    s.perimeter()

    t = Triangle(3, 4, 5, 6)
    t.area()
    t.perimeter()

    p = Pentagon(5, 10)
    p.area()
    p.perimeter()
