
__author__ = 'Осипчук Евгений Александрович'

import random
from math import sqrt

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

s = []
for i in range(10):
    s.append(random.randint(-100, 100))
print('Задача-1: \n', s)
new_list = []
for i in s:
    if i >= 0 and sqrt(i) % 1 == 0:
        new_list.append(int(sqrt(i)))
print(new_list, end='\n\n')

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

date = input('Задача-2: \nВведите дату в формате: dd.mm.yyyy:\n')
try:
    dd = int(date[0:2])
    mm = int(date[3:5])
    yy = int(date[6:])
    if 0 > dd or dd > 31 or 0 > mm or mm > 12 or yy < 0 or \
            dd == 31 and mm != (1, 3, 5, 7, 8, 10, 12) or \
            dd == 29 and mm == 2 and yy % 4 != 0:
        print('Вы ввели несуществующую дату\n\n')
    else:
        days = {1: 'первое', 2: 'второе', 3: 'третье', 4: 'четвертое', 5: 'пятое', 6: 'шестое', 7: 'седьмое',
                8: 'восьмое', 9: 'девятое', 10: 'десятое', 11: 'одиннадцатое', 12: 'двенадцатое', 13: 'тринадцатое',
                14: 'четырнадцатое', 15: 'пятнадцатое', 16: 'шестнадцатое', 17: 'семнадцатое', 18: 'восемнадцатое',
                19: 'девятнадцатое', 20: 'двадцатое', 21: 'двадцать первое', 22: 'двадцать второе',
                23: 'двадцать третье', 24: 'двадцать четвертое', 25: 'двадцать пятое', 26: 'двадцать шестое',
                27: 'двадцать седьмое', 28: 'двадцать восьмое', 29: 'двадцать девятое', 30: 'тридцатое',
                31: 'тридцать первое'}
        month = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня',
                 7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}
        print('Вы ввели: {0} {1} {2} года\n'.format(days[dd], month[mm], yy))
except ValueError:
    print('Вы ввели дату в неверном формате\n')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

try:
    lenght = int(input('Задача-3: \nВведите количество элементов списка:\n'))
    s = []
    for i in range(lenght):
        s.append(random.randint(-100, 100))
    print(s, end='\n\n')
except:
    print('Вы ввели не число\n')


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

s = []
new_list1 = []
new_list2 = []
for i in range(10):
    s.append(random.randint(0, 10))
for i in s:
    if new_list1.count(i) == 0:
        new_list1.append(i)
    if s.count(i) == 1:
        new_list2.append(i)
print('Задача-4: \nНачальный список:\n{0}\nПервый список:\n{1}\nВторой список:\n{2}'.format(s, new_list1, new_list2))
