import hw05_easy
import os

print(os.getcwd())

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

print('Hello. I can do this:')

commands = {
    '1': hw05_easy.go_to_dir,
    '2': hw05_easy.what_in_dir,
    '3': hw05_easy.remove_dir,
    '4': hw05_easy.create_dir,
    'help': hw05_easy.help_func
}

hw05_easy.help_func()

while True:
    com = input('Number of command, help or q for exit:\n')
    if com in ['1', '3', '4']:
        try:
            commands[com](path=os.getcwd(), dir_name=(input('Enter directory name\n')))
        except OSError as e:
            print(e)
    elif com == '2' or com == 'help':
        commands[com]()
    elif com == 'q':
        break
    else:
        print('Sorry, I don`t know this command')
print('Good bye!')
# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
