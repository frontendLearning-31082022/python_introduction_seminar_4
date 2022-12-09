import signal

TIMEOUT = 5  # number of seconds your want for timeout


def interrupted(signum, frame):
    # "called when read times out"
    print('interrupted!')
    signal.signal(signal.SIGALRM, interrupted)


def input():
    try:
        print('You have 5 seconds to type in your stuff...')
        foo = input()
        return foo
    except:
        # timeout
        return


if __name__ == '__main__':
    # set alarm
    signal.alarm(2)
    # signal.alarm(TIMEOUT)
    s = input()
    # disable the alarm after success
    signal.alarm(0)
    print('You typed', s)
