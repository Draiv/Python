# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.


import shutil
import os
import sys
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp - создаёт копию указанного файла")
    print("rm - удаляет указанный файл с запросом подтверждения")
    print("cd - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def cp():
    if not file_name:
        print("Необходимо указать имя файла копирования")
        return
    else:
        try:
            shutil.copy(file_name, 'copy' + file_name)
            print('Файл скопирован в той же директории')
        except FileNotFoundError:
            print('Такого файла {}  не существует'.format(file_name))


def cd():
    if not full_path:
        print("Необходимо полный путь директории")
        return
    else:
        try:
            os.chdir(full_path)
            print('Успешно перешли')
        except FileNotFoundError:
            print('Такого пути {} не существует'.format(full_path))
# Что бы избежать ошибки, когда в пути встречаются пробелы, лучше сделать вводом переменной
# a = input('Введите путь - ')


def ls():
    print(os.getcwd())
    
def rm():
    if not file_name:
        print("Необходимо указать имя файла удаления")
        return
    else:
        try:
            open(file_name, 'r', encoding = 'UTF-8')
            print("Файл найден")
            q = input(r'Действительно удалить файл ? Y\N - ')
            if q == 'Y' :
                os.remove(file_name)
                print('Файл удалён')
            else:
                pass
        except FileNotFoundError:
            print('Такого файла {}  не существует'.format(file_name))
            

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "cd": cd,
    "ls": ls,
    "rm": rm
    }


try:
    full_path = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    dir_name = None
    
try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None
   

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")