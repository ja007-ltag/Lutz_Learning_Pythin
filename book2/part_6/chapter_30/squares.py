class Squares:
    def __init__(self, start, stop):  # Сохранить состояние при создании
        self.value = start - 1
        self.stop = stop

    def __iter__(self):  # Получить объект итератора при вызове iter
        print('Call __iter__')
        return self

    def __next__(self):  # Возвратить квадрат на каждой итерации
        print('Call __next__')
        if self.value == self.stop:  # Также вызывается встроенной функцией next
            raise StopIteration
        self.value += 1
        return self.value ** 2
