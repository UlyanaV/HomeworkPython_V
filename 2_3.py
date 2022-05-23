# 3

month_dict = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь',
              7: 'июль', 8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
season_list = ['зима', 'весна', 'лето', 'осень']
user_month = int(input('Введите месяц в виде целого числа от 1 до 12: '))

if user_month > 12 or user_month == 0:
    print('Необходимо ввести месяц от 1 до 12')
else:
    print(f'месяц: {month_dict[user_month]} ')
if user_month <= 2 or user_month == 12:
    print(f'время года: {season_list[0]}')

elif 2 < user_month <= 5:
    print(f'время года: {season_list[1]}')

elif 5 < user_month <= 8:
    print(f'время года: {season_list[2]}')

elif 8 < user_month <= 11:
    print(f'время года: {season_list[3]}')
else:
    print(f'Нет сезона для этого месяца')
