# 2
# левая принимающая, правая отдающая

number = int(input('Сколько будет элементов списка? '))
my_list = []
a = 0
ind = 0
while a < number:
    my_list.append(input('Введите значение списка '))
    a = a + 1

for i in range(1, len(my_list)-1, 2):
    my_list[ind], my_list[ind + 1] = my_list[ind + 1], my_list[ind]
    ind = ind + 2
print(my_list)
