# 3

def my_func(a, b, c):
    my_list = [a, b, c]
    min_list = min(my_list)
    my_list.remove(min_list)
    print(sum(my_list))


my_func(12, 0, -3)
