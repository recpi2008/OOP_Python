"""
Перегрузка арифметических операторов

__gt__() — соответствует оператору «>».
__lt__() — соответствует оператору «<».
__ge__() — соответствует оператору «≥».
__le__() — соответствует оператору «≤».
__eq__() — соответствует оператору «==».
__add__() — срабатывает при участии объекта в операции сложения в качестве операнда с левой стороны,
обеспечивает перегрузку оператора сложения.
__iadd__() — соответствует операции «Сложение и присваивание» +=.
__isub__() — соответствует операции «Вычитание и присваивание» -=.

"""

import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector2D({}, {})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __neg__(self):
        return Vector2D(-self.x, -self.y)


x = Vector2D(3, 4)
print(x)
print(abs(x))
y = Vector2D(5, 6)
print(x + y)
print(x - y)
print(-x)
x += y
print(x)
print(bool(x))
z = Vector2D(0, 0)
print(bool(z))
print(-z)

class Word(str):
    '''Класс для слов, определяющий сравнение по длине слов.'''

    def __new__(cls, word):
        # Мы должны использовать __new__, так как тип str неизменяемый
        # и мы должны инициализировать его раньше (при создании)
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)

first_world = Word("Привет")
second_world = Word("Пока")

print(first_world <= second_world)