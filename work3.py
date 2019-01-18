import math
print ('Решим с вами корень квадратного уровнения вида - ax**2 + bx + c = 0')
a = int(input('Введите а - '))
b = int(input('Введите b - '))
c = int(input('Введите с - '))
if a == 0:
    print(' a - не должен быть равен 0')
    a = int(input('Введите а - '))
else :
    pass
D = (b**2-(4*a*c))
if D > 0:
    x1 = float((-b - math.sqrt(D))/2*a)
    print('x1 равно:',x1)
    x2 = float((-b + math.sqrt(D))/2*a)
    print('x2 равно:',x2)
elif D == 0:
    x = (-b /(2*a))
    print('x равно:',x)
else :
    print('Корней нет')