# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input('Введите число (n): ')
sum_num = int(number) + int(number + number) + int(number + number + number)
print(f'Cумму чисел n + nn + nnn равна {sum_num}')