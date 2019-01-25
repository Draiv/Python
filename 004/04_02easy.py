# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

a = ['banana','orange','melone','apple']
b = ['orange','guava','paneapple','banana','kiwi']
c = []
print(a)
print(b)
for i in a :
    if i in b :
        c.append(i)
    else : 
        pass
print(c)