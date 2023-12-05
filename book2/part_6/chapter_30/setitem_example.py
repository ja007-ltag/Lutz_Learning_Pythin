"""
Смотрим как работает __setitem__
"""


class IndexSetter:
    def __init__(self, data):
        self.data = data

    def __setitem__(self, index, value):
        self.data[index] = value

    def __repr__(self):
        return f"Data: {self.data}"


X = IndexSetter(list(range(5)))
print(X)
X[3] = 6
print(X)
X[1:2] = 'spam'
print(X)
