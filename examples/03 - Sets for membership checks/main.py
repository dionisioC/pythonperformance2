from memory_profiler import profile
import timeit
import itertools

NUMBER_OF_ELEMENTS = 1000000
NUMBER_OF_LOOPS = 3


def check(iterable, item_to_check):
    return item_to_check in iterable


if __name__ == "__main__":
    my_set = {value for value in range(NUMBER_OF_ELEMENTS)}
    my_list = [value for value in range(NUMBER_OF_ELEMENTS)]
    for _ in itertools.repeat(None, NUMBER_OF_LOOPS):
        print(f"Good : {timeit.timeit(lambda: check(my_set, NUMBER_OF_ELEMENTS - 10), number=100):.20f}")
        print(f"Bad : {timeit.timeit(lambda: check(my_list, NUMBER_OF_ELEMENTS - 10), number=100):.20f}")
