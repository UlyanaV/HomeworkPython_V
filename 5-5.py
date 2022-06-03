# 5

with open('text_5.txt', 'w', encoding='utf-8') as f_obj:
    user_str = input('Введите цифры через пробел ')
    f_obj.write(user_str)
    my_numb = user_str.split()
    print(sum(map(int, my_numb)))
