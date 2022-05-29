# 6 - 1  Реализовать два небольших скрипта: 1 - генерирующий целые числа, начиная с указанного;
from sys import argv
from itertools import count

file, num_start, num_finish = argv

for i in count(int(num_start)):
    if i > int(num_finish):
        break
    else:
        print(i)
