class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1: Point, p2: Point) -> float:
    """ Расстояние между двумя точками """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии
# TODO: your code here...
def polyline_length(points: list) -> float:
    """ Вычисление длины ломаной линии """
    total_length = 0
    for i in range(len(points) - 1):
        total_length += distance(points[i], points[i+1])
    return total_length

print("Длина ломаной линии = ", polyline_length(points))
