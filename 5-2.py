# 2

count = 0
words = 0
str_list = ['stroka_1 \n', 'stroka2 sdfs \n', 'stroka 3 sdfs \n']
with open('text_2.txt', 'w+', encoding='utf-8') as f_obj:
    f_obj.writelines(str_list)
with open('text_2.txt') as f_obj:
    for line in f_obj:
        print(f"{len(line.split())} слов в каждой строке")
        count = count + 1

print(f"Количство строк {count}")
