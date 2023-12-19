# -*- coding: utf-8 -*-

from listinstance import ListInstance  # Получить класс инструмента для вывода списка атрибутов


class Super:
    def __init__(self):
        self.data1 = 'spam'

    def ham(self):
        pass


class Sub(Super, ListInstance):  # Подмешивание ham и __str__
    def __init__(self):          # Классы, выводящие списки атрибутов, имеют доступ к self
        Super.__init__(self)
        self.data2 = 'eggs'
        self.data3 = 42

    def spam(self):
        pass


if __name__ == '__main__':
    X = Sub()
    print(X)
    print(repr(X))
