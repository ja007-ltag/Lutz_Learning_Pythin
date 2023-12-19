#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Файл listinstance.py (Python 2.X + 3.X)


class ListInstance:
    """
    Подмешиваемый класс, который предоставляет форматированную функцию
    print() или str() для экземпляров через наследование реализованного
    в нем метода __str__;
    отображает только атрибуты экземпляра;
    self является экземпляром самого нижнего класса;
    имена __X предотвращают конфликты с атрибутами клиента
    """

    def __attr_names(self):
        # result = ''
        # for attr in sorted(self.__dict__):
        #     result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        # return result
        return ''.join('\t%s=%s\n' % (attr, self.__dict__[attr])  # Этот вариант сложно читаемый
                       for attr in sorted(self.__dict__))

    def __str__(self):
        return '<Instance of %s, address 0x%016X:\n%s>' % (
                    self.__class__.__name__,  # Имя класса
                    id(self),                 # Адрес экземпляра
                    self.__attr_names())      # Список имя=значение


if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInstance)
