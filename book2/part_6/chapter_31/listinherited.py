#! /usr/bin/env python
# -*- coding: utf-8 -*-

class ListInherited:
    """
    Применяет dir() для сбора атрибутов экземпляра и имен, унаследованных
    из его классов;
    в Python 3.X отображает больше имен, чем в Python 2.X из-за наличия
    подразумеваемого суперкласса object в модели классов нового стиля;
    getattr() извлекает унаследованные имена не в self.__dict__;
    используйте __str__, а не __repr__, иначе произойдёт зацикливание при
    вызове связанных методов!
    """

    def __attr_names(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                result += '\t%s\n' % attr
            else:
                result += '\t%s=%s\n' % (attr, getattr(self, attr))
        return result

    def __str__(self):
        return '<Instance of %s, address 0x%016X:\n%s' % (
                    self.__class__.__name__,
                    id(self),
                    self.__attr_names())


if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInherited)
