# -*- coding: utf-8 -*-

"""
pybench.py: тестирует скорость одной и более версий Python
на наборе простых эталонных тестов в виде строк кода.
Функция runner допускает разнообразные операторы в stmts.
Сама система выполняется в Python 2.x и 3.x и может
порождать вывод в обеих линейках.

Использует модуль timeit для тестирования либо версии Python,
выполняющей этот сценарий, через вызовы API-интерфейса, либо
набора версий Python за счёт чтения порождённого вывода командной
строки (os.popen) посредством флага -m интерпретатора Python,
позволяющего находить timeit в пути поиска модулей.

Заменяют $listif3 на list в генераторах для Python 3.X и на пустую строку
для Python 2.X, заставляя Python 3.X делать ту же самую работу, что и Python 2.X.
В режиме командной строки многострочные операторы должны разделяться на отдельные
аргументы в кавычках для каждой строки и все символы \t в отступах должны
заменяться четырьмя пробелами ради единообразия.

Предостережения:
режим командной строки (только) может потерпеть неудачу, если
внутри оператора содержатся двойные кавычки, строка оператора в кавычках вообще
несовместима с командной оболочкой или командная строка превышает предел длины
в командной оболочке платформы -- применяйте режим вызова API-интерфейса
или любительский таймер;

Реализация оператора настройки.
"""

import os
import sys
import timeit

def_num, def_rep = 1000, 5  # Может варьироваться от оператора к оператору


def runner(stmts, pythons=None, tracecmd=False):
    """
    Основная логика: запускать тесты на входных списках,
    режимами использования управляет вызывающий код.
    :param stmts: [(количество?, повторений?, строка-оператора)] заменяет $listif3 в строке оператора
    :param pythons: None = только эта версия Python или
    [(версия-Python-3?, путь-к-исполняемому-файлу-Python)]
    :param tracecmd:
    :return:
    """
    print(sys.version)
    for number, repeat, setup, stmt in stmts:
        number = number or def_num
        repeat = repeat or def_rep  # 0 = стандартное значение

        if not pythons:
            # Запустить оператор stmt в этой версии Python: вызов API-интерфейса.
            # Нет необходимости разделять строки или помещать в кавычки
            ispy3 = sys.version[0] == '3'
            stmt = stmt.replace('$listif3', 'list' if ispy3 else '')
            best = min(timeit.repeat(setup=setup, stmt=stmt, number=number, repeat=repeat))
            print('%.4f [%r]' % (best, stmt[:70]))
        else:
            # Запустить оператор stmt во всех версиях Python: командная строка.
            # Разделить строки на аргументы в кавычках
            setup = setup.replace('\t', ' ' * 4)
            setup = ' '.join('-s "%s"' % line for line in setup.split('\n'))
            print('-' * 80)
            print('[%r]' % stmt)
            for ispy3, python in pythons:
                stmt1 = stmt.replace('$listif3', 'list' if ispy3 else '')
                stmt1 = stmt1.replace('\t', ' ' * 4)
                lines = stmt1.split('\n')
                args = ' '.join('"%s"' % line for line in lines)
                cmd = '"%s" -m timeit -n %s -r %s %s %s' % (python, number, repeat, setup, args)
                print(python)
                if tracecmd:
                    print(cmd)
                print('\t' + os.popen(cmd).read().rstrip())
