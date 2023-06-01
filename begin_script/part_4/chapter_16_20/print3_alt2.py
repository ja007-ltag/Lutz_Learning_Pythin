#! /usr/bin/pithon3
"""Использование удаления ключевых аргументов Python 2.X/3.X со стандартными значениями"""

import sys


def print3(*args, **kwargs):
    sep = kwargs.pop('sep', ' ')
    end = kwargs.pop('end', '\n')
    file = kwargs.pop('file', sys.stdout)
    if kwargs:
        raise TypeError('extra keyword: %s' % kwargs)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)
