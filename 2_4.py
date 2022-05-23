# 4.

words = input('Введите строку из нескольких слов, разделённых пробелами: ').split()

for i, n in enumerate(words, 1):
    print(f'{i} {n:.10}')
