# 7
import json

subj = {}
sum_s = 0
with open('text_7.txt', 'r', encoding='utf-8') as f_obj:
    for i in f_obj:
        name, sobstvennosti, vyruchka, izderzhki = i.split()
        res = int(vyruchka) - int(izderzhki)
        sum_s += res
        subj[name] = res
    print(f'Прибыль каждой компании\n {subj}')
    print(f'Средняя прибыль: {sum_s/len(subj)}')
    subj['Average profit'] = sum_s / len(subj)

with open('text_7.json', 'w', encoding='utf-8') as f_js:
    json.dump(subj, f_js)
    my_js_str = json.dumps(subj)
    print(f'Файл json:\n{my_js_str}')
