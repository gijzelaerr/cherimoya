"""
random data generators. Not real python generators by the way.
"""
import random



def float_generator(start, end):
    """
    returns a function that generates random float in the range start - end.
    """
    return lambda: start + random.random()*(end-start)


def int_generator(start, end):
    """
    returns a function that generates random ints in the range start - end.
    """
    return lambda: int(start + random.random()*(end-start))


def str_generator(choices):
    """
    returns a function that generates random choices from `choices`.
    """
    return lambda: random.choice(choices)


def complex_generator(start, end):
    """
    returns a function that generates random complex numbers in the range
    start - end. complex numers are formatted like: (0.1,0.2)
    """
    ran = lambda: start + random.random()*(end-start)
    return lambda: "(%s,%s)" % (ran(), ran())