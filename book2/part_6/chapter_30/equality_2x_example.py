# -*- coding: utf-8 -*-
# Только в Python 2.X

class C:
    data = 'spam'

    def __cmp__(self, other):
        return cmp(self.data, other)


X = C()
print(X > 'ham')
print(X < 'ham')
