# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

"""
class Figure():

    def __init__(self, dots):
"""


def lenght(dot1, dot2):
    return math.sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)


class Triangle():

    def __init__(self, type, *args):
        self.type = type
        self.a = args[0]
        self.b = args[1]
        self.c = args[2]
        self.ab = lenght(self.a, self.b)
        self.bc = lenght(self.b, self.c)
        self.ac = lenght(self.a, self.c)

    def perimeter(self):
        P = self.ab + self.bc + self.ac
        print(f'Периметр треугольника: {P}')

    def area(self):
        p = (self.ab + self.bc + self.ac) / 2
        S = (p * (p - self.ac) * (p - self.ab) * (p - self.bc)) ** 0.5
        print(f'Площадь треугольника: {S}')

    def heights(self, dot):
        p = (self.ab + self.bc + self.ac) / 2
        if dot.upper() == 'A':
            h = 2 * ((p * (p - self.ac) * (p - self.ab) * (p - self.bc)) ** 0.5) / self.bc
        elif dot.upper() == 'B':
            h = 2 * ((p * (p - self.ac) * (p - self.ab) * (p - self.bc)) ** 0.5) / self.ac
        elif dot.upper() == 'C':
            h = 2 * ((p * (p - self.ac) * (p - self.ab) * (p - self.bc)) ** 0.5) / self.ab
        else:
            print(f'Вершины {dot} не существет')
            h = 0
        print(f'Высота треугольника из точки {dot} равна: {h}')


Equilateral_tri = Triangle('Равносторонний', (0, 0), (1 / 2, math.sqrt(3) / 2), (1, 0))
Isosceles_tri = Triangle('Равнобедренный', (3, 3), (-1, 1), (7, 1))
Scalene_tri = Triangle('Скошенный', (-3, 4), (-1, -1), (1, 1))

print('Для равностороннего треугольника:')
Equilateral_tri.perimeter()
Equilateral_tri.area()
Equilateral_tri.heights('a')
Equilateral_tri.heights('b')
Equilateral_tri.heights('c')
print()
print('Для равнобедренного треугольника:')
Isosceles_tri.perimeter()
Isosceles_tri.area()
Isosceles_tri.heights('a')
Isosceles_tri.heights('b')
Isosceles_tri.heights('c')
print()
print('Для скошенного треугольника:')
Scalene_tri.perimeter()
Scalene_tri.area()
Scalene_tri.heights('a')
Scalene_tri.heights('b')
Scalene_tri.heights('c')
print()


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezoid:
    def __init__(self, *args):
        self.a = args[0]
        self.b = args[1]
        self.c = args[2]
        self.d = args[3]
        self.ab = lenght(self.a, self.b)
        self.bc = lenght(self.b, self.c)
        self.cd = lenght(self.c, self.d)
        self.da = lenght(self.d, self.a)

    def check(self):
        return lenght(self.c, self.a) == lenght(self.b, self.d)

    def perimeter(self):
        return self.ab + self.bc + self.cd + self.da

    def area(self):
        return ((self.da + self.bc) / 4) * math.sqrt((4 * (self.ab ** 2)) - ((self.da - self.bc) ** 2))


trapezoid = Trapezoid((0, 0), (2, 4), (6, 4), (8, 0))
print(f'{trapezoid.check()}')
print(f'Трапеция имеет следующие параметры: \n'
      f'Длины сторон: \n'
      f'ab = {trapezoid.ab}\n'
      f'bc = {trapezoid.bc}\n'
      f'cd = {trapezoid.cd}\n'
      f'da = {trapezoid.da}\n'
      f'Периметр = {trapezoid.perimeter()}\n'
      f'Площадь = {trapezoid.area()}\n')
