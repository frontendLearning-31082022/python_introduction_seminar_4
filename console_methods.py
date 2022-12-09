import multiprocessing
import re
import sys
from threading import Thread
import time
import select

def input_strings_while_q(msg):
    print_console(msg + " <<<<To_STOP_-_enter_'q'>>>>")
    result = []
    inputed = ""
    while not inputed.__eq__("q"):
        inputed = input()
        if inputed.__eq__("q"): break
        result.append(inputed)

    return result


def input_one_string(msg):
    print_console(msg)
    inputed = input()
    return inputed


def input_dig_in_range(msg, from_dig, to_dig):
    if msg != None:
        print_console(msg)
    inputed = input_digit(True)
    while inputed <= from_dig >= to_dig:
        inputed = input_digit(True)
        print_console(f"in range {from_dig} to {to_dig} pls")
    return inputed


def input_digit(positive_only):
    while True:
        inputed = input()
        check_digit=is_it_digit(inputed)
        if (positive_only and check_digit):
            corrected_input = float(inputed) > -1
        if check_digit:
            break
        print_console("Input integer again")

    inputed = float(inputed)
    return inputed

def is_it_digit(inputed):
    result = re.findall(r'\D', inputed)
    result = list(filter(lambda x: not (str(x).__eq__("-")), result))
    result = list(filter(lambda x: not (str(x).__eq__(",")), result))
    result = list(filter(lambda x: not (str(x).__eq__(".")), result))

    corrected_input = len(result) == 0
    return corrected_input

def print_console(textt='', *new_line):
    if new_line != None:
        sys.stdout.write(textt)
        return

    print(textt)


def input_int(negotive):
    inputed = input_digit(False)
    is_it_integer = inputed.is_integer()

    while (inputed >= 0 or not is_it_integer):
        print_console(f"It's negotive digit {negotive}."
                      f"It's integer digit {inputed.is_integer()}.  Try again")
        inputed = int(input_digit(False))

    return int(inputed)




