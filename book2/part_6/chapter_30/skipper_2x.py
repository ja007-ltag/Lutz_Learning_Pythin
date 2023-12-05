# -*- coding: utf-8 -*-

from __future__ import print_function  # Совместимость с Python 2.X/3.X


class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)


class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item

    next = __next__  # Совместимость с Python 2.X/3.X


if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I), next(I), next(I))
    print(*skipper)

    for x in skipper:
        for y in skipper:
            print(x + y, end=' ')
    print()
