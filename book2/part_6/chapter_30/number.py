class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return Number(self.data - other)

    def __rsub__(self, other):
        return Number(other - self.data)

    def __repr__(self):
        return f'Num: {self.data}'


if __name__ == '__main__':
    X = Number(7)
    print(X)
    print(X - 2)
    print(17 - X)
    X -= 3
    print(X)

