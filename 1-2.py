# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

import time

time_user = int(input("Введите время в секундах "))
time_format = time.strftime("%H:%M:%S", time.gmtime(time_user))
print(f'Время в формате чч:мм:сс {time_format}')