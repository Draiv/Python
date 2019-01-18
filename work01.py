a = int(input('Введите 3-x значное число - '))
i = 0
while a >= 100:
    a = a - 100
    i += 1
print ( i )
b = 0
while a >= 10:
    a = a - 10
    b += 1
print ( b )
c = -1
while a >= 0:
    a = a - 1
    c += 1
print ( c )

if i >= b >= c :
    print('Наибольшее число - ',i)
elif c >= b >= i :
    print('Наибольшее число - ',c)
elif b >= c >= i :
    print('Наибольшее число - ',b)