import config
import time

my_config = config.get_config()
number_of_loops = my_config.getint("Global", "number_of_loops")

start = time.time()
for i in range(number_of_loops):
    pass
end = time.time()
print(end - start)
