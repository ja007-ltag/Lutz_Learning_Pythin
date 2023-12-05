class Commuter1:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        print('radd', other, self.val)
        return other + self.val


class Commuter2:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        return self.__add__(other)  # Явно вызвать __add__


class Commuter3:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        return self + other  # Поменять местами и снова сложить


class Commuter4:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    __radd__ = __add__  # Псевдоним: исключить посредника


class Commuter5:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        # if isinstance(other, Commuter5):  # Проверка типа во избежание вложенности объектов
        #     other = other.val
        return Commuter5(self.val + other)  # Иначе результатом операции + является ещё один Commuter5

    # def __radd__(self, other):
    #     return Commuter5(other + self.val)
    __radd__ = __add__

    def __str__(self):
        return '<Commuter5: %s>' % self.val


if __name__ == '__main__':
    # for klass in Commuter1, Commuter2, Commuter3, Commuter4, Commuter5:
    #     print(f'\n{klass.__name__}')
    #     x = klass(88)
    #     y = klass(99)
    #     print(x + 1)
    #     print(1 + y)
    #     print(x + y)

    x = Commuter5(88)
    y = Commuter5(99)
    z = x + y
    print(z + z)
    z += z
    print(z)
