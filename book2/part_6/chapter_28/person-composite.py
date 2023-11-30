# -*- coding: utf-8 -*-
# Альтернативная версия Manager, основанная на внедрении

from person import Person


class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)  # Внедрить объект Person

    def give_raise(self, percent, bonus=.10):
        self.person.give_raise(percent + bonus)  # Перехватить и делегировать

    def __getattr__(self, attr):
        return getattr(self.person, attr)  # Делегировать все остальные атрибуты

    def __repr__(self):
        return str(self.person)  # снова должен быть перегружен (в Python 3.X)


if __name__ == '__main__':
    # Код самотестирования
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    # Для совместимости с Python 2.X
    # print('{0} {1}'.format(bob.name, bob.pay))
    # print('%s %s' % (bob.name, bob.pay))
    print(bob)
    print(sue)
    print(bob.last_name(), sue.last_name())
    sue.give_raise(.10)
    print(sue)

    tom = Manager('Tom Jones', pay=50000)
    tom.give_raise(.10)
    print(tom.last_name())
    print(tom)

    # print('--All there--')
    # for obj in bob, sue, tom:
    #     obj.give_raise(.10)
    #     print(obj)
