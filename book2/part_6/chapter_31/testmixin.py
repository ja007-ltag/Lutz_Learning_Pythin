#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Обобщенный инструмент тестирования подмешиваемых классов вывода списков:
он похож на средство транзитивной перезагрузки модулей из главы 25 первого
тома, но ему передается объект класса (не функции), а в test_by_names
добавлена загрузка модуля и класса по строковым именам в соответствии с
паттерном проектирования "фабрика".
"""

import importlib


def tester(lister_class, sept=False):
    class Super:
        def __init__(self):
            self.data1 = 'spam'

        def ham(self):
            pass

    class Sub(Super, lister_class):
        def __init__(self):
            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 42

        def spam(self):
            pass

    instance = Sub()  # Возвратить экземпляр с помощью __str__ класса, выводящего список

    print(instance)   # Выполняется подмешанный метод __str__ (или через str(x))

    if sept:
        print('-' * 80)


def test_by_names(mod_name, class_name, sept=False):
    mod_object = importlib.import_module(mod_name)  # Импортировать по строковым именам

    lister_class = getattr(mod_object, class_name)  # Извлечь атрибуты по строковым именам

    tester(lister_class, sept)


if __name__ == '__main__':
    test_by_names('listinstance', 'ListInstance', True)

    # test_by_names('listinherited', 'ListInherited', True)
    # test_by_names('listtree', 'ListTree', False)
