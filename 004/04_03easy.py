# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
list_new = []
list = []
for i in range(50):
    list.append(random.randint(-25,25))
print(list)
print()
for a in list :
    if (a % 3) == 0 :
        list_new.append(a)
print(list_new)
print()
for b in list_new[:] :
    if b < 0 :
        list_new.remove(b)
print(list_new)
for c in list_new[:] :
    if (c % 4) == 0 :
        list_new.remove(c)
print()
print(list_new)