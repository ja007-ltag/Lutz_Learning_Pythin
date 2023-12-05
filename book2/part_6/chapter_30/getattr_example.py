# -*- coding: utf-8 -*-

class Empty:
    def __getattr__(self, attr_name):  # вызывается для неопределённого атрибута в self
        if attr_name == 'age':
            return 40
        else:
            raise AttributeError(attr_name)


X = Empty()
print(X.age)
# print(X.name)
