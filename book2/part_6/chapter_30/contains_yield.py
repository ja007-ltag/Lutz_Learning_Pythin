# -*- coding: utf-8 -*-
from __future__ import print_function


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):          # Запасной вариант для итерации
        print('get[%s]:' % i, end='')  # Также для индексирования, нарезания
        return self.data[i]

    def __iter__(self):                # Предпочтительнее для итерации
        print('iter=> next:', end='')  # Разрешает множество активный итераторов
        for x in self.data:            # __next__ для создания псевдонима next отсутствует
            yield x
            print('next:', end='')

    def __contains__(self, x):         # Предпочтительнее для операции in
        print('contains: ', end='')
        return x in self.data

    def __len__(self):
        return len(self.data)


if __name__ == '__main__':
    X = Iters([1, 2, 3, 4, 5])
    print()
    print('Членство')
    print(3 in X)

    print()
    print('Циклы for')
    for i in X:
        print(i, end=' | ')
    print()

    print()
    print('Другие итерационные контексты')
    print([i ** 2 for i in X])
    print(list(map(bin, X)))

    print()
    print('Итерация вручную')
    I = iter(X)
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            print()
            break

    print()
    print('Индексация и срезы')
    print(X[3])
    print(X[1:3])
    print(X[1:-1])
    print(X[:-1])
    print(X[1:-1:2])
    print(X[::-1])
    print(X[-2::-1])
