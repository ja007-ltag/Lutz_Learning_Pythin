# -*- coding: utf-8 -*-

class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj                      # Сохранить объект

    def __getattr__(self, attrname):
        print('Trase: ' + attrname)             # Трассировать извлечение
        return getattr(self.wrapped, attrname)  # Делегировать извлечение


if __name__ == '__main__':
    x = Wrapper([1, 2, 3])
    x.append(4)
    print(x.wrapped)

    x = Wrapper({'a': 1, 'b': 2})
    print(list(x.keys()))
