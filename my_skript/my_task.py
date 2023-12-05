class Num:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(self, Num):
            other = other.value
        return Num(self.value + other)

    def __radd__(self, other):
        return Num(self.value + other)

    def __str__(self):
        return f'Num({self.value})'


if __name__ == '__main__':
    x = Num(0)
    for i in range(1000):
        x += Num(1)
        print(x)
