from memory_profiler import profile
import timeit
import itertools

NUMBER_OF_ELEMENTS = 100000
NUMBER_OF_LOOPS = 3


class Slots:
    __slots__ = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.x = self.y + self.z
        self.y = self.x + self.z
        self.z = self.y + self.x
        self.x = self.x + self.z


class NoSlots:

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.x = self.y + self.z
        self.y = self.x + self.z
        self.z = self.y + self.x
        self.x = self.x + self.z


@profile
def instanitate_classes(number_of_loops, klass):
    objects = []
    for i in range(number_of_loops):
        x = klass(i, i + 1, i + 2)
        objects.append(x)


if __name__ == "__main__":
    for _ in itertools.repeat(None, NUMBER_OF_LOOPS):
        print(f"Slots : {timeit.timeit(lambda: instanitate_classes(NUMBER_OF_ELEMENTS, Slots), number=1):.20f}")
        print(f"No slots : {timeit.timeit(lambda: instanitate_classes(NUMBER_OF_ELEMENTS, NoSlots), number=1):.20f}")
