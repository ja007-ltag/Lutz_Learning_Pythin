# -*- coding: utf-8 -*-

"""
pybench_cases.py: запускает pybench на наборе версий Python и операторов.
Выбирайте режимы путем редактирования этого сценария либо использования
аргументов командной строки (в sys.argv): например, запускайте

"C:\\Program Files\\Python38\\python" pybench_cases.py,
чтобы протестировать только одну версию Python из перечисленных в stmts,

pybench_cases.py -a для тестирования всех версий Python
py -3 pybench_cases.py -a -t для трассировки командных строк.
"""

import sys
import pybench

pythons = [  # (Python3?, путь)
    (1, r"C:\Program Files\Python311\python"),
    (1, r"C:\Program Files\Python310\python"),
    (1, r"C:\Program Files\Python39\python"),
    (1, r"C:\Program Files\Python38\python"),
    # (1, r"C:\Program Files\Python37\python"),
    # (1, r"C:\Program Files\Python36\python"),
    # (1, r"C:\Program Files\Python35\python"),
    # (1, r"C:\Program Files\Python34\python"),
    # (1, r"C:\Program Files\Python33\python"),
    # (1, r"C:\Program Files\Python32\python"),
    # (1, r"C:\Program Files\Python31\python"),
    (0, r"C:\Program Files\Python27\python"),
    # (0, r"C:\Program Files\Python26\python"),
    # (0, r"C:\Program Files\Python25\python"),
]

stmts = [  # (количество, повторения, оператор)
    (0, 0, "[x ** 2 for x in range(1000)]"),
    (0, 0, "res = []\nfor x in range(1000): res.append(x ** 2)"),
    (0, 0, "res = []\nfor x in range(1000):\n\tres.append(x ** 2)"),
    (0, 0, "$listif3(map(lambda x: x ** 2, range(1000)))"),
    (0, 0, "list(x ** 2 for x in range(1000))"),
    (0, 0, "s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"),
    (0, 0, "s = 'spam' * 2500\nx = [s[i] for i in range(len(s))]"),
    (0, 0, "s = '?'\nfor i in range(10000): s += '?'"),
    (0, 0, "s = '?'\nfor i in range(10000):\n\ts += '?'"),
]

tracecmd = '-t' in sys.argv  # -t: трассировать командные строки?
pythons = pythons if '-a' in sys.argv else None  # -a: все версии или одну

pybench.runner(stmts, pythons, tracecmd)
