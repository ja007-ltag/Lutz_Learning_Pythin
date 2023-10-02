# -*- coding: utf-8 -*-

"""
pybench_cases.py: запускает pybench на наборе версий Python и операторов.
Выбирайте режимы путем редактирования этого сценария либо использования
аргументов командной строки (в sys.argv): например, запускайте

"C:\\Program Files\\Python38\\python" pybench_cases2.py,
чтобы протестировать только одну версию Python из перечисленных в stmts,

py pybench_cases2.py -a для тестирования всех версий Python
py -3 pybench_cases2.py -a -t для трассировки командных строк.
"""

import sys
import pybench

if any([
    sys.version_info[:2] == (3, 10),
    sys.version_info[:2] == (3, 11)
]):
    sys.set_int_max_str_digits(400000)

pythons = [  # (Python3?, путь)
    (1, r"C:\Program Files\Python311\python"),
    (1, r"C:\Program Files\Python310\python"),
    (1, r"C:\Program Files\Python39\python"),
    (1, r"C:\Program Files\Python38\python"),
    # (1, r"C:\Program Files\Python37\python"),
    # (1, r"C:\Program Files\Python36\python"),
    (1, r"C:\Program Files\Python35\python"),
    # (1, r"C:\Program Files\Python34\python"),
    # (1, r"C:\Program Files\Python33\python"),
    # (1, r"C:\Program Files\Python32\python"),
    (1, r"C:\Program Files\Python31\python"),
    (0, r"C:\Program Files\Python27\python"),
    # (0, r"C:\Program Files\Python26\python"),
    (0, r"C:\Program Files\Python25\python"),
]

stmts = [  # (количество, повторения, оператор)
    # # Использовать вызовы функций: map выигрывает
    # (0, 0, "[ord(x) for x in 'spam' * 2500]"),
    # (0, 0, "res=[]\nfor x in 'spam' * 2500: res.append(ord(x))"),
    # (0, 0, "res=[]\nfor x in 'spam' * 2500:\n\tres.append(ord(x))"),
    # (0, 0, "$listif3(map(ord, 'spam' * 2500))"),
    # (0, 0, "list(ord(x) for x in 'spam' * 2500)"),
    #
    # # Множества и словари
    # (0, 0, "{x ** 2 for x in range(1000)}"),
    # (0, 0, "s = set()\nfor x in range(1000): s.add(x ** 2)"),
    # (0, 0, "s = set()\nfor x in range(1000):\n\ts.add(x ** 2)"),
    # (0, 0, "{x: x ** 2 for x in range(1000)}"),
    # (0, 0, "d={}\nfor x in range(1000): d[x] = x ** 2"),
    # (0, 0, "d={}\nfor x in range(1000):\n\td[x] = x ** 2"),
    #
    # # Патологический случай: 301030 цифр
    # (1, 1, "len(str(2 ** 1000000))"),
    # (0, 0, "len(str(2 ** 1000))")

    # # Чтение файлов
    # (0, 0, "f = open('C:/Program Files/Python311/Lib/pdb.py')\nfor line in f:  x = line\nf.close()"),

    (0, 0, "def f(x): return x\n[f(x) for x in 'spam' * 2500]"),
    (0, 0, "def f(x): return x\nres = []\nfor x in 'spam' * 2500: res.append(f(x))"),
    (0, 0, "def f(x): return x\n$listif3(map(f, 'spam' * 2500))"),
    (0, 0, "def f(x): return x\nlist(f(x) for x in 'spam' * 2500)")
]

tracecmd = '-t' in sys.argv  # -t: трассировать командные строки?
pythons = pythons if '-a' in sys.argv else None  # -a: все версии или одну

pybench.runner(stmts, pythons, tracecmd)
