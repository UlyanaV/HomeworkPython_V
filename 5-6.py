# 6
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

subj = {}
with open('text_6.txt', 'r', encoding='utf-8') as f_obj:
    for i in f_obj:
        name, stats = i.split(':')
        sum_s = sum(map(int, ''.join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        subj[name] = sum_s
    print(f'Общее количество часов по предмету - \n {subj}')
