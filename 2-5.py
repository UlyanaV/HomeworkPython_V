# 5.

user_num = int(input('Введите новый элемент рейтинга: '))
my_list = [7, 5, 3, 3, 2]
n = 0
for i in my_list:
    if user_num <= i:
        n = n + 1
    else:
        break
my_list.insert(n, user_num)
print(my_list)
