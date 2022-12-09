# 1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника.
# В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений
# необходимо запускать скрипт с параметрами.

from sys import argv

import console_methods

if __name__ == '__main__':
    if len(argv) < 4:
        print(
            "Error. It's need 3 args - hours_count, one_hour_cost and premium. App stoping")

    for iter in range(1, 3):
        if not console_methods.is_it_digit(argv[iter]):
            print(f"Error. {argv[iter]} not digit")
            exit(1)

    hours_count = float(argv[1])
    one_hour_cost = float(argv[2])
    premium = float(argv[3])

    result_salary = hours_count * one_hour_cost + premium
    print(f"Salary result - {result_salary} conv. un.")
