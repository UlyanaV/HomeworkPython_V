# 3

with open('text_3.txt', 'r', encoding='utf-8') as f_obj:
    workers = {}
    sum_s = 0
    for i in f_obj:
        key, value = i.split()
        sum_s += int(float(value))
        workers[key] = value
        if int(float(value)) < 20000:
            print(key)
print(f'Cредней величины дохода сотрудников: {sum_s/len(workers)}')
