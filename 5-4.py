# 4

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('text_4.txt', 'r', encoding='utf-8') as f_obj:
    with open('my_file_4.txt', 'w', encoding='utf-8') as new_obj:
        for i in f_obj:
            res = i.replace(i.split()[0], rus.get(i.split()[0]))
            new_obj.writelines(res)
            print(res, end='')
