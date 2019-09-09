from memory_profiler import profile
import config
import time
from random import random
from string import ascii_lowercase

lis = list(ascii_lowercase)
my_config = config.get_config()
number_of_loops = my_config.getint("Global", "number_of_loops")
examples = [lis[int(random() * 26)] for _ in range(number_of_loops)]


@profile
def string_joiner():
    final_string = ''
    for c in examples:
        final_string += c


start = time.time()
string_joiner()
end = time.time()
print(end - start)
