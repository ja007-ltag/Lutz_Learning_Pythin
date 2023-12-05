class Squares:  # генератор на основе __iter__ + yield
    def __init__(self, start, stop):  # Метод __next__ является автоматическим/подразумеваемым
        self.start = start
        self.stop = stop

    def gen(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2
