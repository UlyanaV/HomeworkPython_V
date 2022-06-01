# 7 Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24


def fact(num_user):
    x = 1
    for i in range(1, num_user + 1):
        yield f'{i}!={x}'
        x = x * (i + 1)


for el in fact(int(input('Введите чилсо для расчета факториала: '))):
    print(el)
