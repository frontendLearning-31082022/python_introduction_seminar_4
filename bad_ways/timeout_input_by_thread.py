import multiprocessing
import time
from threading import Thread


def __get_input():
    while True:
        try:
            print(input('> '))
        except EOFError as e:
            fsd=0


def __start_thread():
    t1 = Thread(target=__get_input)
    t1.daemon = True
    t1.start()

def input_by_timeout(secs_timeout,msg):
    print(msg)

    proc = multiprocessing.Process(target=__start_thread)
    proc.start()

    time.sleep(secs_timeout)
    # proc.terminate()