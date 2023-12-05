# -*- coding: utf-8 -*-

class Accesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'age':
            # self.age = value + 10             # рекурсивное зацикливание
            # setattr(self, attr, value + 10)   # рекурсивное зацикливание
            # self.__dict__[attr] = value + 10  # нормально: зацикливания нет
            object.__setattr__(self, attr, value + 10)  # нормально: зацикливания нет (только классы нового стиля)
        else:
            raise AttributeError(attr + ' not allowed')


X = Accesscontrol()
X.age = 40
print(X.age)

Y = Accesscontrol()
Y.age = 25
print(Y.age)

# X.name = 'Bob'
