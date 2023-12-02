# -*- coding: utf-8 -*-
class Super:
    def method(self):
        print('in Super.method')     # Стандартное поведение

    def delegate(self):
        self.action()                # Ожидается определение метода

    def action(self):
        # assert False, 'action must be defined!'
        raise NotImplementedError('action must be defined!')


class Inheritor(Super):              # Буквальное наследование метода
    pass


class Replacer(Super):               # Полное замещение метода
    def method(self):
        print('in Replacer.method')  # в Replacer.method


class Extender(Super):
    def method(self):
        print('staring Extender.method')  # начало Extender.method
        Super.method(self)
        print('ending Extender.method')   # конец Extender.method


class Provider(Super):               # заполнение обязательного метода
    def action(self):
        print('in Provider.action')  # в Provider.method


if __name__ == '__main__':
    for klass in Inheritor, Replacer, Extender:
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()
