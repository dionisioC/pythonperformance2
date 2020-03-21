from memory_profiler import profile
import timeit
import itertools

NUMBER_OF_ELEMENTS = 100000
NUMBER_OF_LOOPS = 3


def good_generator():
    return (x * 2 for x in range(NUMBER_OF_ELEMENTS))


@profile
def good_generator_memory():
    for loop_count in good_generator():
        foo = loop_count + 3


def bad_generator():
    return [x * 2 for x in range(NUMBER_OF_ELEMENTS)]


@profile
def bad_generator_memory():
    for loop_count in bad_generator():
        foo = loop_count + 3


def my_generator(start_value):
    while start_value < NUMBER_OF_ELEMENTS:
        yield start_value
        start_value += 1


@profile
def my_generator_memory():
    for loop_count in my_generator(0):
        foo = loop_count + 3


if __name__ == "__main__":
    for _ in itertools.repeat(None, NUMBER_OF_LOOPS):
        print(f"Good : {timeit.timeit(lambda: good_generator(), number=100):.20f}")
        print(f"Bad : {timeit.timeit(lambda: bad_generator(), number=100):.20f}")
        print(f"Own : {timeit.timeit(lambda: my_generator(0), number=100):.20f}")
        print(f"Good memory : {timeit.timeit(lambda: good_generator_memory(), number=1)}")
        print(f"Bad memory : {timeit.timeit(lambda: bad_generator_memory(), number=1)}")
        print(f"Own memory : {timeit.timeit(lambda: my_generator_memory(), number=1)}")
