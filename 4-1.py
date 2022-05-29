# 1

from sys import argv

file, production_hours, hourly_rate, premium = argv
salary = (int(production_hours) * int(hourly_rate)) + int(premium)

print(f'Заработная плата сотрудника: {salary}')
