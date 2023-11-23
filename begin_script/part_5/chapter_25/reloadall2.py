#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
reloadall2.py: транзитивная перезагрузка встроенных модулей
(альтернативная версия)
"""

import types
# from imp import reload  # from требуется в Python 3.X
from reloadall import status, tryreload, tester


def transitive_reload(objects, visited):
    for obj in objects:
        if type(obj) is types.ModuleType and obj not in visited:
            status(obj)
            tryreload(obj)  # Перезагрузить это, рекурсия по атрибутам
            visited.add(obj)
            transitive_reload(obj.__dict__.values(), visited)


def reload_all(*args):
    transitive_reload(args, set())


if __name__ == '__main__':
    tester(reload_all, 'reloadall2')
