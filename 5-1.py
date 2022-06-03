# 1
# программно значит файла нет в системе

while True:
    user_str = input('Введите данные для добавления в файл. '
                     'Об окончании ввода данных будет свидетельствовать пустая строка ')
    if user_str == '':
        exit()
    else:
        with open('text_1.txt', 'a', encoding='utf-8') as f_obj:
            f_obj.write(f'{user_str}\n')

