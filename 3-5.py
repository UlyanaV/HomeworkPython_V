# 5

def sum_num():
    sum_res = 0
    ex = False
    while not ex:
        number = input('Введите строку чисел, разделённых пробелом или q для выхода: ').split()
        res = 0
        for i in range(len(number)):
            if number[i] == 'q':
                ex = True
                break
            else:
                res = res + int(number[i])
        sum_res = sum_res + res
        print(f'Сумма: {sum_res}')
    print(f'Финальная сумма: {sum_res}')


sum_num()
