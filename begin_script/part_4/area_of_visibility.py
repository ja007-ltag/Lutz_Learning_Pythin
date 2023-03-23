"""Документация модуля"""

import builtins
import sys

x = 99
print(x)


def func():
    """Документация функции"""
    x = 88
    print(x)


func()
print(func.__doc__)
print(x)
print(__doc__)

L = [x for x in range(3)]
print(L)
print(x)

L = []
for x in range(3):
    L.append(x)
print(L)
print(x)

X = 99


def func(Y):
    Z = X + Y
    return Z


print(func(1))
