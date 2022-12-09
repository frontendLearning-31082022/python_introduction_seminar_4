# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
#  Во втором также необходимо предусмотреть условие,
#  при котором повторение элементов списка будет прекращено.

import itertools
import os
import sys
import time
from threading import Thread

import window


def generator_thread():
    some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    generator_cycle = itertools.cycle(some_list)
    while True:
        print(generator_cycle.__next__())
        time.sleep(2)


if __name__ == '__main__':
    thread = Thread(target=generator_thread)
    thread.start()

    window.show_first_window()
