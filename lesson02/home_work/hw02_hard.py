
__author__ = 'Осипчук Евгений Александрович'

import random

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# вычислите и выведите y

equation = 'y = -12x + 11111140.2121'
x = 2.5
equal_pos = equation.index('=')                                         # Находим позиции ключевых точек в строке
x_pos = equation.index('x')
plus_pos = equation.index('+')
k = float(equation[equal_pos + 2: x_pos])                               # Делаем срезы по позициям и получаем k и b
b = float(equation[plus_pos + 2:])
y = k * x + b
print('При x = {0} \nk = {1} \nb = {2} \ny = {3}\n'.format(x, k, b, y))

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

date = input('Введите дату в формате: dd.mm.yyyy:\n')
try:
    dd = int(date[0:2])
    mm = int(date[3:5])
    yy = int(date[6:])
    if 0 > dd or dd > 31 or 0 > mm or mm > 12 or 0 > yy or yy > 9999 or \
            dd == 31 and mm != (1, 3, 5, 7, 8, 10, 12) or \
            dd == 29 and mm == 2 and yy % 4 != 0:
        print('Вы ввели несуществующую дату\n\n')
    else:

        print('Такая дата существует!\n')
except:
    print('Вы ввели дату в неверном формате\n')

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

room = random.randint(1, 2000000000)
try:
    room = int(input('Ваша комната - {}. \nЕсли хотите, можете выбрать другую. Введите номер комнаты: \n'.format(room)))
except ValueError:
    print('Как хотите')
last_room = 0                                       # Последняя комната в группе
group = 0                                           # Группа комнат, с искомой комнатой
last_floor = 0                                      # Последний этаж в группе.
while last_room < room:                             # Находим последний этаж и последнюю комнату в группе
    group += 1
    last_room += group**2
    last_floor += group
dist = last_room - room                             # Находим расстояние от последней комнаты, до нашей
floor = last_floor - dist // group                  # Находим этаж комнаты
count = group - dist % group                        # Находим положение комнаты на этаже
print('Чтобы попасть в комнату № {0} вам нужно подняться на {1}-й этаж.'
      ' Ваша комната {2}-я слева.'.format(room, floor, count))
