# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

a = input('Введите значения - ')
b = input('На что проверить - ')

def fil(funct, name) :
    for i in funct :
        if str(i) == str(name) :
            print(i)
        else :
            pass
fil(a,b)
    