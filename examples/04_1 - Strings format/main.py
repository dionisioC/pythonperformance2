import timeit
import itertools

NUMBER_OF_LOOPS = 3


def c_style(a, b, c, d):
    return "Ms. %s! My %s crawled in my %s and then I %s it. Can I have another one?" % (a, b, c, d)


def format_string(a, b, c, d):
    return "Ms. {}! My {} crawled in my {} and then I {} it. Can I have another one?".format(a, b, c, d)


def format_string_position(a, b, c, d):
    return "Ms. {0}! My {2} crawled in my {1} and then I {3} it. Can I have another one?".format(a, b, c, d)


def f_string(a, b, c, d):
    return f"Ms. {a}! My {b} crawled in my {c} and then I {d} it. Can I have another one?"


if __name__ == "__main__":
    for _ in itertools.repeat(None, NUMBER_OF_LOOPS):
        print(f"C-style : {timeit.timeit(lambda: c_style('Hoover', 'worm', 'mouth', 'ate'), number=1000000):.5f}")
        print(f"Format : {timeit.timeit(lambda: format_string('Hoover', 'worm', 'mouth', 'ate'), number=1000000):.5f}")
        print(f"Format position : {timeit.timeit(lambda: format_string_position('Hoover', 'worm', 'mouth', 'ate'), number=1000000):.5f}")
        print(f"F-string : {timeit.timeit(lambda: f_string('Hoover', 'worm', 'mouth', 'ate'), number=1000000):.5f}")
