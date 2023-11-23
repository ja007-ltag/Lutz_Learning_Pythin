#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
reloadall3.py: транзитивная перезагрузка встроенных модулей (явный стек)
"""

import types
# from imp import reload  # from требуется в Python 3.X
from reloadall import status, tryreload, tester


def transitive_reload(modules, visited):
    # while modules:
    #     _next = modules.pop()  # удалить элемент next в конце
    #     if _next not in visited:
    #         status(_next)
    #         tryreload(_next)
    #         visited.add(_next)
    #         modules.extend(x for x in _next.__dict__.values()
    #                        if type(x) is types.ModuleType and x not in visited)

    while modules:
        _next = modules.pop()  # удалить элемент next в конце
        status(_next)
        tryreload(_next)
        visited.add(_next)
        modules.extend(x for x in _next.__dict__.values()
                       if type(x) is types.ModuleType and x not in visited and x not in modules)


def reload_all(*modules):
    """
    Функция транзитивная перезагрузка встроенных модулей (явный стек).
    Перезагружает все модули импортированные с помощью оператора import,
    с from не работает

    :param modules: передайте модуль, который желаете перезагрузить
    """
    transitive_reload(list(modules), set())


if __name__ == '__main__':
    tester(reload_all, 'reloadall3')
    # tester(reload_all, 'tkinter')
