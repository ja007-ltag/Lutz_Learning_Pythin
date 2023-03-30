"""Это черновик и не более"""


def changer(a, b):
    b = b[:]
    a = 2
    b[0] = 'spam'


X = 1
L = [1, 2]

changer(X, tuple(L))
print(X, L)

