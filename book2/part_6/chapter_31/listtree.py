#! /usr/bin/env python
# -*- coding: utf-8 -*-

class ListTree:
    """
    Подмешиваемый класс, который возвращает в __str__ результат обхода целого
    дерева классов и атрибуты всех его объектов, начиная с self и выше;
    запускается print() и str() и возвращает сформированную строку;
    использует схему именования __X, чтобы избежать конфликтов
    имен в клиентах; явно рекурсивно обращается к суперклассам,
    для ясности применяется str.format().
    """

    def __attr_names(self, obj, indent):
        spaces = ' ' * (indent + 1)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result

    def __list_class(self, a_class, indent):
        dots = '.' * indent
        if a_class in self.__visited:
            return '\n{0}<Class {1}:, address 0x{2:016X}: (see above)>\n'.format(
                dots,
                a_class.__name__,
                id(a_class)
            )
        else:
            self.__visited[a_class] = True
            here = self.__attr_names(a_class, indent)
            above = ''
            for supers in a_class.__bases__:
                above += self.__list_class(supers, indent+4)
        return '\n{0}<Class {1}, address 0x{2:016X}:\n{3}{4}{0}>\n'.format(
            dots,
            a_class.__name__,
            id(a_class),
            here, above,
        )

    def __str__(self):
        self.__visited = {}
        here = self.__attr_names(self, 0)
        above = self.__list_class(self.__class__, 4)
        return '<Instance of {0}, address 0x{1:016X}:\n{2}{3}>'.format(
            self.__class__.__name__,
            id(self),
            here, above
        )


if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListTree)
