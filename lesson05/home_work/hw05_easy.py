import os
import shutil


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def create_dir(dir_name='new_dir', num=1, path=os.getcwd()):
    for i in range(num):
        dir_path = os.path.join(path, f'{dir_name}_{i+1}')
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print('This dir already exist')
        except ValueError:
            print('Impossible to create dir')


def remove_dir_tree(path=os.getcwd()):
    for root, dirs, files in os.walk(path, topdown=False):
        for f in files:
            if path != os.getcwd():
                os.remove(os.path.join(root, f))
        for d in dirs:
            os.rmdir(os.path.join(root, d))


def remove_dir(path=os.getcwd(), dir_name='new_dir_1'):
    path = os.path.join(path, dir_name)
    try:
        os.rmdir(path)
    except OSError as e:
        print(e)


# create_dir()
# create_dir('Dir', 4)
# input("press enter to remove one dir")
# remove_dir()
# input("press enter to remove dirs")
# remove_dir_tree()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def exist_dirs(path=os.getcwd()):
    print('По указанному пути находятся следующие директории:')
    for _, dirs, _ in os.walk(path, topdown=False):
        for d in dirs:
            print(d)


# exist_dirs()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
filename = os.path.basename(__file__)
path = os.path.abspath(filename)


def copy_file(file=path, copy=f'{path[:-3]}_copy.py'):
    shutil.copy2(file, copy)


# copy_file()


# Функции для задачи нормал


def go_to_dir(dir_name, path=os.getcwd()):
    path = os.path.join(path, dir_name)
    if os.path.isdir(path):
        os.chdir(path)
    else:
        print('There`s no dir')





def what_in_dir(path=os.getcwd()):
    print('Dir includes:')
    files = os.listdir(path=os.getcwd())
    for file in files:
        print(file)


def help_func():
    print('1. Go to dir')
    print('2. Show files and dirs in current dir')
    print('3. Delete dir')
    print('4. Create dir')
    print('q - quit')
