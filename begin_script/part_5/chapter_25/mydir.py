#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
mydir.py: модуль, который выводит листинг пространства имен другого модуля
"""

from __future__ import print_function

sep_len = 60
sep_chr = '-'


def listing(module, verbose=True):
    """
    Выводит листинг пространства имен другого модуля

    :param module: передаваемый модуль
    :param verbose: (подробно) = False - выведет чуть меньше информации
    """
    sep_line = sep_chr * sep_len
    if verbose:
        print(sep_line)
        print('name:', module.__name__, 'file:', module.__file__)
        print(sep_line)

    count = 0
    for attr in sorted(module.__dict__):
        count += 1
        print('%02d) %s' % (count, attr), end=' ')
        if attr.startswith('__'):
            print('<built-in name>')
        else:
            print(getattr(module, attr))

    if verbose:
        print(sep_line)
        print(module.__name__, 'has %d names' % count)
        print(sep_line)


if __name__ == '__main__':
    import mydir
    listing(mydir)
