from memory_profiler import profile
import config
import time

my_config = config.get_config()
number_of_loops = my_config.getint("Global", "number_of_loops")


class NoSlots:

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.x = self.y + self.z
        self.y = self.x + self.z
        self.z = self.y + self.x
        self.x = self.x + self.z

@profile
def instanitate_classes():
    objects = []
    for i in range(number_of_loops):
        x = NoSlots(i, i + 1, i + 2)
        objects.append(x)


start = time.time()
instanitate_classes()
end = time.time()
print(end - start)
