# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    b = [1,1]
    for i in range(200):
        c = sum(b[0+i:2+i])
        b.append(c)
    print(b[n-1:m])
fibonacci(1,5)