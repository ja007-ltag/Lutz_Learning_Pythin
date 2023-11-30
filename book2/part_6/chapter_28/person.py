# -*- coding: utf-8 -*-
"""
Регистрирует и обрабатывает сведения о людях.
Для тестирования классов из этого файла запустите его напрямую
"""

from class_tools import AttrDisplay


class Person(AttrDisplay):
    """
    Создает и обрабатывает записи о людях
    """
    def __init__(cur, name, job=None, pay=0):
        cur.name = name
        cur.job = job
        cur.pay = pay  # оплата

    def last_name(mine):  # Предполагается, что фамилия указана последней
        return mine.name.split()[-1]

    def give_raise(her, percent):  # Процент должен находиться между 0 и 1
        her.pay = int(her.pay * (1 + percent))


class Manager(Person):
    """
    Настроенная версия Person со специальными требованиями
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)  # Название должности подразумевается

    def give_raise(self, percent, bonus=.10):
        # self.pay = int(self.pay * (1 + percent + bonus))  # Плохой способ: копирование кода и изменение
        Person.give_raise(self, percent + bonus)  # хороший способ: расширение исходной версии

    def something_else(self, ):
        pass


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.last_name(), sue.last_name())
    sue.give_raise(.10)
    print(sue)

    tom = Manager('Tom Jones', pay=50000)
    tom.give_raise(.10)
    print(tom.last_name())
    print(tom)

