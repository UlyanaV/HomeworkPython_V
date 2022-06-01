# 6 - 2 Реализовать два небольших скрипта: 2 - повторяющий элементы некоторого списка, определённого заранее.

from sys import argv
from itertools import cycle

file, user_str = argv
c = 1

for el in cycle(user_str):
    if c > len(user_str):
        break
    print(el)
    c += 1

