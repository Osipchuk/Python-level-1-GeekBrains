# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


def read_f(file_name, col):
    d = dict()
    with open('data\\{}'.format(file_name), 'r', encoding='UTF-8') as f:
        for line in f:
            line = line.split(' ')
            line = list(filter(len, line))
            line[-1] = line[-1].replace('\n', '')
            if line[col].isdigit() or line[col].find('.') != -1:
                d[line[0] + ' ' + line[1]] = float(line[col])
    return d


salary = read_f('workers', 2)
standard_hours = read_f('workers', 4)
fact_hours = read_f('hours_of', 2)
fact_salary = dict()
for key, value in fact_hours.items():
    if value <= standard_hours[key]:
        fact_salary[key] = round(value * salary[key] / standard_hours[key], 2)
    else:
        fact_salary[key] = round(2 * int(value - standard_hours[key]) * salary[key] / \
                                 standard_hours[key] + salary[key], 2)
with open('data\\salary.txt', 'w', encoding='UTF-8') as f:
    f.write('Имя Фамилия   Фактическая_зарплата\n')
    for key, value in fact_salary.items():
        f.write('{}\t{}\n'.format(key, str(value)))


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


def write_in_file(line):
    with open(('data\\fruits_{}.txt'.format(str(line[0]))), 'a', encoding='utf-8') as f:
        f.write(line + '\n')


def read_file(file_name):
    with open('data\\{}'.format(file_name), 'r', encoding='utf-8') as f:
        for line in f:
            if not line.isspace():  # проверка на наличие отображаемых символов
                line = line.capitalize()
                write_in_file(line)


read_file('fruits.txt')
