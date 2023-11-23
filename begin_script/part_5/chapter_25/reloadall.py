#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
reloadall.py: транзитивная перезагрузка встроенных модулей (Python 2.X + 3.X).
Вызывайте reload_all с одним и более объектами импортированных модулей.
"""

import types
from imp import reload


def status(module):
    print('reloading ' + module.__name__)


def tryreload(module):
    try:
        reload(module)  # В Python 3.3 (только?) иногда терпело неудачу
    except:
        print('FAILED: %s' % module)


def transitive_reload(module, visited):
    if module not in visited:  # Отлавливать циклы, дубликаты
        status(module)         # Перезагрузить этот модуль
        tryreload(module)      # И посетить дочерние модули
        visited[module] = True
        for attrobj in module.__dict__.values():     # Для всех атрибутов
            if type(attrobj) is types.ModuleType:    # Рекурсивный вызов,
                transitive_reload(attrobj, visited)  # если это модуль


def reload_all(*args):
    visited = {}       # Главная точка входа
    for arg in args:  # Для всех переданных аргументов
        if type(arg) is types.ModuleType:
            transitive_reload(arg, visited)


def tester(reloader, modname):  # Код самотестирования
    import importlib            # импортировать только при тестировании
    import sys
    if len(sys.argv) > 1:
        modname = sys.argv[1]  # Командная строка (или переданный аргумент)
    module = importlib.import_module(modname)  # Импортировать по строке с именем
    reloader(module)


if __name__ == '__main__':
    tester(reload_all, 'reloadall')
