from threading import Thread
import time


def get_input():
    while True:
        print(input('> '))


def input_it(secs):
    t1 = Thread(target=get_input)
    t1.daemon=True
    t1.start()
    time.sleep(secs)
    print('program exceeds')