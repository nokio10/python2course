from __future__ import annotations


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self: Point, other_point: Point) -> float:
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def perimeter(self):
        side1 = self.p1.distance(self.p2)
        side2 = self.p2.distance(self.p3)
        side3 = self.p3.distance(self.p1)
        return side1 + side2 + side3

    def area(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5




# Треугольник задан координатами трех точек
triangle = Triangle(Point(2, 4), Point(6, 8), Point(8, 0))

# Задание: 
# найдите площадь и периметр треугольника, реализовав методы area() и perimeter()

print("Периметр треугольника = ", triangle.perimeter())
print("Площадь треугольника = ", triangle.area())
