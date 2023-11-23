# -*- coding: utf-8 -*-

from __future__ import print_function
from formats import money
import sys
print(sys.version)
X = 54321.987

print(money(X), money(X, 0, ''))
print(money(X, currency=u'\xA3'), money(X, currency=u'\u00A5'))
print(money(X, currency=b'\xA3'.decode('latin-1')))
print(money(X, currency=u'\u20AC'), money(X, 0, b'\xA4'.decode('iso-8859-15')))
print(money(X, currency=b'\xA4'.decode('latin-1')))

"""
Если не работает, то нужна донастройка командной оболочки:

c:> chcp 65001                  # установить кодовую страницу консоли, по умолчанию используется 866 -я
c:> set PYTHONIOENCODING=utf-8  # сделать кодовую страницу питона в соответствие с консолью

После это заработали версии Python 2.6, 2.7, 3.3+
В Python 3.0-3.2 работает, если удалить Unicode-литерал u'...'
В Python 2.5 не работает - ну и хрен с ним
"""