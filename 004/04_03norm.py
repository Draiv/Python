# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import re
import os
import random


a = open('file.txt', 'w', encoding = 'UTF-8')

for i in range(2500):
    a.write(str(random.randint(0 , 10)))
a.close()
f = open('file.txt', 'r', encoding = 'UTF-8')
for line in f:
    print(line)
    print()
    part1 = re.compile('[0]{1}|[1]{1}|[2]{1}|[3]{1}|[4]{1}|[5]{1}|[6]{1}|[7]{1}|[8]{1}|[9]{1}')
    part2 = re.compile('[0]{2}|[1]{2}|[2]{2}|[3]{2}|[4]{2}|[5]{2}|[6]{2}|[7]{2}|[8]{2}|[9]{2}')
    part3 = re.compile('[0]{3}|[1]{3}|[2]{3}|[3]{3}|[4]{3}|[5]{3}|[6]{3}|[7]{3}|[8]{3}|[9]{3}')
    part4 = re.compile('[0]{4}|[1]{4}|[2]{4}|[3]{4}|[4]{4}|[5]{4}|[6]{4}|[7]{4}|[8]{4}|[9]{4}')
    part5 = re.compile('[0]{5}|[1]{5}|[2]{5}|[3]{5}|[4]{5}|[5]{5}|[6]{5}|[7]{5}|[8]{5}|[9]{5}')
    part6 = re.compile('[0]{6}|[1]{6}|[2]{6}|[3]{6}|[4]{6}|[5]{6}|[6]{6}|[7]{6}|[8]{6}|[9]{6}')
    part7 = re.compile('[0]{7}|[1]{7}|[2]{7}|[3]{7}|[4]{7}|[5]{7}|[6]{7}|[7]{7}|[8]{7}|[9]{7}')
    result = part1.findall(line)
    if len(result) > 1:
        result = part2.findall(line)
        print(result)
        if len(result) > 1:
            result = part3.findall(line)
            print(result)
            if len(result) > 1:
                result = part4.findall(line)
                print(result)
                if len(result) > 1:
                    result = part5.findall(line)
                    print(result)
                    if len(result) > 1:
                        result = part6.findall(line)
                        print(result)
                        if len(result) > 1:
                            result = part7.findall(line)
                            print(result)