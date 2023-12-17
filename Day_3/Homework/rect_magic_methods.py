"""
Используем класс Rect() с длиной и шириной в качестве атрибутов
Дополнительные задания на magic methods:
1) __repr__() - отобразить в виде текста

2) __str__() - отобразить в виде текста

3) r1 * 5 (__mul__()) - обе стороны станут в 5 раз больше
   добавить проверкy, что тип аргумента метода __mul__ это int или float
   # Variant 1, но python -O отключает все assert'ы
   assert type(arg) in (int, float), 'Bad type'

   # Variant 2
   if type(arg) in (int, float):
       pass
   else:
       raise TypeError

4) r1 < r2, r1 == r2, r1 <= r1 и т.п.

Шесть методов для сравнения:
__lt__() -> '<'
__gt__() -> '>'
__le__() -> '<='
__ge__() -> '>='
__eq__() -> '=='
__ne__() -> '!='
Сравнить по площади.

def __gt__(self, other):
	# ...
	# return True/False
"""

class Rect:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'

    def __str__(self):
        return f'Rectangle with length {self.length} and width {self.width}'

    def __mul__(self, arg):
        if isinstance(arg, (int, float)):
            return Rect(self.length * arg, self.width * arg)
        else:
            raise TypeError("Multiplier must be an int or float")

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()


# Пример использования:
r1 = Rect(2, 3)
r2 = Rect(4, 5)

print(repr(r1))  # Вывод: Rectangle(2, 3)
print(str(r1))   # Вывод: Rectangle with length 2 and width 3

r3 = r1 * 5
print(repr(r3))  # Вывод: Rectangle(10, 15)

print(r1 < r2)   # Вывод: True
print(r1 == r2)  # Вывод: False
print(r1 <= r2)  # Вывод: True
print(r1 > r2)   # Вывод: False
print(r1 >= r2)  # Вывод: False
print(r1 != r2)  # Вывод: True
