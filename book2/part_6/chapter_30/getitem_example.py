"""
Смотрим как работает __getitem__
"""


class Indexer:
    def __getitem__(self, index):
        return index ** 2


X = Indexer()
print(X[2])

for i in range(5):
    print(X[i], end=' ')
print('\n' + '-' * 20)


class Indexer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]


X = Indexer()
print(X[0])
print(X[1])
print(X[2])
print('-' * 20)

print(X[2:4])
print(X[1:])
print(X[:-1])
print(X[::2])
print(X[:])
print('-' * 20)


class Indexer:
    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)


X = Indexer()
print(X[99])
print(X[1:99:2])
print(X[1:])
