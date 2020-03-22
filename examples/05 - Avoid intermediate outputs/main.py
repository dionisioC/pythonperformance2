import timeit
import itertools

NUMBER_OF_ELEMENTS = 1000
NUMBER_OF_LOOPS = 3


def good_intermediate_testing(number_of_loops):
    for _ in itertools.repeat(None, number_of_loops):
        print('Hi how are you')


def good_intermediate_no_print_testing(number_of_loops):
    for _ in itertools.repeat(None, number_of_loops):
        foo = 20 + 20 + 20 + 20


def bad_intermediate_testing(number_of_loops):
    for _ in itertools.repeat(None, number_of_loops):
        print('Hi')
        print('How')
        print('Are')
        print('You')


def bad_intermediate_no_print_testing(number_of_loops):
    for _ in itertools.repeat(None, number_of_loops):
        foo = 20
        foo += 20
        foo += 20
        foo += 20


if __name__ == "__main__":
    results = []
    for _ in itertools.repeat(None, NUMBER_OF_LOOPS):
        good_print = timeit.timeit(lambda: good_intermediate_testing(NUMBER_OF_ELEMENTS), number=100)
        bad_print = timeit.timeit(lambda: bad_intermediate_testing(NUMBER_OF_ELEMENTS), number=100)
        good_no_print = timeit.timeit(lambda: good_intermediate_no_print_testing(NUMBER_OF_ELEMENTS), number=100)
        bad_no_print = timeit.timeit(lambda: bad_intermediate_no_print_testing(NUMBER_OF_ELEMENTS), number=100)
        results.append((good_print, bad_print, good_no_print, bad_no_print))

    for good_print, bad_print, good_no_print, bad_no_print in results:
        print(f"Good print: {good_print:.20f}")
        print(f"Bad print: {bad_print:.20f}")
        print(f"Good no print: {good_no_print:.20f}")
        print(f"Bad no print: {bad_no_print:.20f}")
