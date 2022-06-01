# 5

from functools import reduce

my_list = [i for i in range(100, 1001) if i % 2 == 0]


def my_func(prev_el, el):
    return prev_el * el


print(f'Чётные числа от 100 до 1000: {my_list}')
print(f'Результат вычисления произведения всех элементов списка {reduce(my_func, my_list)}')
