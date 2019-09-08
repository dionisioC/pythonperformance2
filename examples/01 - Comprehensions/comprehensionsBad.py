import config
import time

my_config = config.get_config()
number_of_loops = my_config.getint("Global", "number_of_loops")


def bad_list():
    my_list = []
    for value in range(number_of_loops):
        my_list.append(value)


start = time.time()
bad_list()
end = time.time()
print(end - start)
