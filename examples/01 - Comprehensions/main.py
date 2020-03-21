import timeit
import itertools

NUMBER_OF_ELEMENTS = 1000000
NUMBER_OF_LOOPS = 3


def good_list():
    my_list = [value for value in range(NUMBER_OF_ELEMENTS)]


def bad_list():
    my_list = []
    for value in range(NUMBER_OF_ELEMENTS):
        my_list.append(value)


def good_list():
    my_list = [value for value in range(NUMBER_OF_ELEMENTS)]


def modulus_validation(value):
    return value % 2 == 0


def good_list_validation():
    my_list = [value for value in range(NUMBER_OF_ELEMENTS)
               if modulus_validation(value)]


def good_tuple():
    my_tuple = tuple(value for value in range(NUMBER_OF_ELEMENTS))


def good_set():
    my_set = {value for value in range(NUMBER_OF_ELEMENTS)}


def good_dict():
    my_dict = {value: value for value in range(NUMBER_OF_ELEMENTS)}


if __name__ == "__main__":
    for _ in itertools.repeat(None, NUMBER_OF_LOOPS):
        print(f"Good : {timeit.timeit(lambda: good_list(), number=100)}")
        print(f"Bad : {timeit.timeit(lambda: bad_list(), number=100)}")
