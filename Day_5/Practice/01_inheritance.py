"""
## 2.1 Квадрат
сделать класс Square - квадрат, который наследуется от прямоугольника

Класс Point(x: int, y: int)

# прямоугольник создаем на основе двух точек (class Point)
Класс Rect(p1, p2)

rect = Rect(p1: Point, p2: Point)
p1 = left_bottom -> (1, 1)  # левая нижняя
p2 = right_top -> (4, 5)    # правая верхняя
methods: area, perimeter (можно через property)


class Square(Rect):
    def __init__(self, p1, size):
        # ...

    # добавить метод вычисления диагонали
    def diagonal():
        pass
    
sq = Square(p1, 5)  # Квадрат 5x5
print(sq.area())
print(sq.perimeter())
print(sq.diagonal())
print(sq)
"""

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Rect:
    def __init__(self, p1: Point, p2: Point):
        self.a = p2.x - p1.x
        self.b = p2.y - p1.y


    def area(self):
        return self.a * self.b

    def __str__(self):
        return f'{self.__class__.__name__}({self.a}x{self.b})'

    def perimeter(self):
        return (self.a + self.b) * 2

class Square(Rect):

    def __init__(self, p1: Point, size: int):
        self.p2 = Point(p1.x + size, p1.y + size)
        self.size = size
        Rect.__init__(self, p1, p2)

    def diagonal(self):
        return (2 * self.size ** 2) ** 0.5

    def __str__(self):
        return f"Квадрат {self.size}x{self.size}"

p1 = Point(1, 1)  # левая нижняя
p2 = Point(4, 5)    # правая верхняя
rect = Rect(p1, p2)
sq = Square(p1, 5)  # Квадрат 5x5
print(sq.area())
print(sq.perimeter())
print(sq.diagonal())
print(sq)
