import timeit
import itertools
from random import random
from string import ascii_lowercase

NUMBER_OF_ELEMENTS = 1000000
NUMBER_OF_LOOPS = 3


def good_string_joiner(list_to_join):
    ''.join(list_to_join)


def bad_string_joiner(list_to_join):
    final_string = ''
    for c in list_to_join:
        final_string += c


if __name__ == "__main__":
    lis = list(ascii_lowercase)
    examples = [lis[int(random() * 26)] for _ in itertools.repeat(None, NUMBER_OF_ELEMENTS)]
    for _ in itertools.repeat(None, NUMBER_OF_LOOPS):
        print(f"Good : {timeit.timeit(lambda: good_string_joiner(examples), number=100):.20f}")
        print(f"Bad : {timeit.timeit(lambda: bad_string_joiner(examples), number=100):.20f}")
