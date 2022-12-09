# 6) Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
import itertools
import time
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.

# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл.

from itertools import cycle
from sys import argv
from threading import Thread

import console_methods
import window


def generator_thread(first, second):
    generator_integer = itertools.count(int(first))
    if len(argv) > 2:
        generator_integer = itertools.count(int(first))
    # generator_integer = itertools.count(int(argv[1]))
    # if len(argv) > 2:
    #     generator_integer = itertools.count(int(argv[1]), int(argv[2]))

    while True:
        dig = generator_integer.__next__()
        print(dig)
        if second != None:
            if int(second) == dig:
                exit(0)
        time.sleep(2)


if __name__ == '__main__':
    if len(argv) < 2:
        print("Error. It's need 1 args at least. First number of cycle")
        exit(1)

    if not argv[1].isdigit():
        print("Error. First arg need digit")
        exit(1)

    if len(argv) < 3:
        print("No end number inputed")
    else:
        if not argv[2].isdigit():
            print("Error. Second arg need digit")
            exit(1)

    first = 0
    second = 0
    try:
        first = argv[1]
    except:
        asd = 0

    try:
        second = argv[2]
    except:
        asd = 0

    thread = Thread(target=generator_thread(first, second))
    thread.start()

    window.show_first_window()
