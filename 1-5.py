# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника

income = int(input("Введите выручку фирмы "))
costs = int(input("Введите издержки фирмы "))

if income > costs:
    print(f'Фирма отработала с прибылью {income - costs})')
    print(f'Рентабельность выручки {((income - costs) / costs):.1f}')
    employees = int(input("Введите численность сотрудников фирмы "))
    print(f'Прибыль фирмы в расчёте на одного сотрудника {income - costs / employees:.2f}')
elif income == costs:
    print(f'Фирма отработала в ноль.')
else:
    not_profit = income - costs
    print(f'Фирма в убытке {not_profit}')
