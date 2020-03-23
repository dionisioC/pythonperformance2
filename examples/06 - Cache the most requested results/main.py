import time
import timeit
import itertools
from functools import lru_cache

NUMBER_OF_ELEMENTS = 1000
NUMBER_OF_LOOPS = 3


def expensive_function(value):
    time.sleep(value / (NUMBER_OF_ELEMENTS * NUMBER_OF_ELEMENTS))


def non_expensive_function(value):
    return value + 1


def bad_cache_testing(number_of_loops):
    for loop_count in range(number_of_loops):
        expensive_function(loop_count % 2)


def bad_cache_testing_non_expensive(number_of_loops):
    for loop_count in range(number_of_loops):
        non_expensive_function(loop_count % 2)


@lru_cache(maxsize=8)
def cached_expensive_function(value):
    time.sleep(value / (NUMBER_OF_ELEMENTS * NUMBER_OF_ELEMENTS))


def good_cache_testing(number_of_loops):
    for loop_count in range(number_of_loops):
        cached_expensive_function(loop_count % 2)


@lru_cache(maxsize=8)
def cached_non_expensive_function(value):
    return value + 1


def good_cache_testing_non_expensive(number_of_loops):
    for loop_count in range(number_of_loops):
        cached_non_expensive_function(loop_count % 2)


if __name__ == "__main__":
    for _ in itertools.repeat(None, NUMBER_OF_LOOPS):
        print(f"Good : {timeit.timeit(lambda: good_cache_testing(NUMBER_OF_ELEMENTS), number=100):.20f}")
        print(f"Bad : {timeit.timeit(lambda: bad_cache_testing(NUMBER_OF_ELEMENTS), number=100):.20f}")
        print(f"Good non expensive: {timeit.timeit(lambda: good_cache_testing_non_expensive(NUMBER_OF_ELEMENTS), number=100):.20f}")
        print(f"Bad non expensive: {timeit.timeit(lambda: bad_cache_testing_non_expensive(NUMBER_OF_ELEMENTS), number=100):.20f}")
