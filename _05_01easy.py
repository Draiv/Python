# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def newdir():
    name = input(print('Введите название папки - '))
    dir_path1 = os.path.join(os.getcwd(), name)
    #dir_path2 = os.path.join(os.getcwd(), 'dir_9')
    try:
        os.mkdir(dir_path1)
        print('Дериктории созданы')
        #os.mkdir(dir_path2)
    except FileExistsError:
        print ( 'Такая директория уже существует')
    
def deldir():
    print(os.listdir())
    name = input(print('Введите название папки - '))
    try :
        os.rmdir(name)
        #os.rmdir(r'dir_9')
        print('Директории удалены')
    except FileExistsError:
        print ( 'Такая не найдена')
