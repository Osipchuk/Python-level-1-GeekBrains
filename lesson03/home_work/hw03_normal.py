from math import sqrt
import random


def my_round(number, ndigits=0):
    number *= 10 ** ndigits
    i = number - int(number)
    if i >= 0.5:
        number = int(number) + 1
    else:
        number = int(number)
    return number / 10 ** ndigits


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

print('\nЗадача 1:\n')


def fibonacci(n, m):
    """
    Функция возвращает числа фибоначи с n по m элементы. Первые элементы находятся с помощью формулы Бине
    """
    first_num = my_round(((((1 + sqrt(5)) / 2) ** (n - 1)) - (((1 - sqrt(5)) / 2) ** (n - 1))) / sqrt(5))
    second_num = my_round(((((1 + sqrt(5)) / 2) ** n) - (((1 - sqrt(5)) / 2) ** n)) / sqrt(5))
    fibonacci_num = [int(second_num)]
    while n < m:
        first_num, second_num = second_num, first_num + second_num
        fibonacci_num.append(int(second_num))
        n += 1
    return fibonacci_num


print(fibonacci(10, 16))
print(fibonacci(13, 21))
print(fibonacci(1, 14))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
print('\nЗадача 2:\n')


def sort_to_max(nums):
    """Функция, основанная на алгоритме быстрой сортировки"""
    if len(nums) <= 1:
        return nums
    else:
        num = random.choice(nums)
        left_nums = []
        right_nums = []
        m_nums = []
        for n in nums:
            if n < num:
                left_nums.append(n)
            elif n > num:
                right_nums.append(n)
            else:
                m_nums.append(n)
        return sort_to_max(left_nums) + m_nums + sort_to_max(right_nums)


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print('\nЗадача 3:\n')


def my_filter(condition, n):
    filter_iter = []
    for i in n:
        if condition(i):
            filter_iter.append(i)
    return filter_iter


test_list = [-5, -1, 0, 1, 2, 3, 4, 5, 10]
print('Список', test_list)
print('Отсортированный список:', my_filter(lambda x: x % 2 == 0, test_list))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
print('\nЗадача 4:\n')


def length(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def isParallelogramm(c):
    if len(c) == 8 and (length(c[0], c[1], c[2], c[3]) == length(c[4], c[5], c[6], c[7]) and (
            length(c[0], c[1], c[4], c[5]) == length(c[2], c[3], c[6], c[7]) or
            length(c[0], c[1], c[6], c[7]) == length(c[2], c[3], c[4], c[5]))):
        return True
    else:
        return False


coordinate = [-3, -1, -2, 2, 4, 2, 3, -1]
coordinate1 = [-3, -1, -2, 2, 3, -1, 4, 2]
coordinate2 = [-3, -1, -2, 2, 4, 2, 3, 1]
print(coordinate, isParallelogramm(coordinate))
print(coordinate1, isParallelogramm(coordinate1))
print(coordinate2, isParallelogramm(coordinate2))
