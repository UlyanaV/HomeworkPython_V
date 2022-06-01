# 1

def del_f(a, b):
    try:
        res = int(a) / int(b)
        print(res)
    except ZeroDivisionError:
        print("You can't divide by zero")


del_f(input('Введите число a: '), input('Введите число b: '))
