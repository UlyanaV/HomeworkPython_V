# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное число: '))
num_max = 0
while number > 10:
    n = number % 10
    number = number//10
    if n > num_max:
        num_max = n
print(f'Самая большая цифра в числе {num_max}')