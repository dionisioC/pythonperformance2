import timeit
import itertools

NUMBER_OF_ELEMENTS = 100000
NUMBER_OF_LOOPS = 3


def range_function(number_of_loops):
    for i in range(number_of_loops):
        pass


def itertools_function(number_of_loops):
    for _ in itertools.repeat(None, number_of_loops):
        pass


if __name__ == "__main__":
    for _ in itertools.repeat(None, NUMBER_OF_LOOPS):
        print(f"Itertools : {timeit.timeit(lambda: itertools_function(NUMBER_OF_ELEMENTS), number=100):.20f}")
        print(f"Range : {timeit.timeit(lambda: range_function(NUMBER_OF_ELEMENTS), number=100):.20f}")
