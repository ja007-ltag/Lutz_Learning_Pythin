# -*- coding: utf-8 -*-

"""
Homegrown timing tools for function calls.
Does total time, best-of time, and best-of-totals time

Любительские инструменты для измерения времени выполнения вызовов функций.
Определяют суммарное время, лучшее время и лучшее суммарное время

!!! Для версий Python 2.X не работает из-за русских символов.
Пока не знаю как это решить, кроме как удалением русским комментов.

timer_eng.py - копия данного модуля без кириллицы!!!
"""

from __future__ import print_function
import sys
import time

# timer = time.clock if sys.platform[:3] == 'win' else time.time
# timer = time.perf_counter

# if sys.platform[:3] != 'win':
#     timer = time.time
# elif sys.version_info.major == 3 and sys.version_info.minor > 3:
#     timer = time.perf_counter
# else:
#     timer = time.time

# if sys.version_info[0] >= 3 and sys.version_info[1] >= 3:
#     timer = time.perf_counter  # or process_time
# else:
#     timer = time.clock if sys.platform[:3] == 'win' else time.time

try:
    timer = time.perf_counter
except AttributeError:
    timer = time.clock if sys.platform[:3] == 'win' else time.time

print('Platform: {0}, python: {1}'.format(sys.platform, sys.version.split()[0]))
print('Select function: {0}'.format(timer.__name__))


def total(reps, func, *args, **kwargs):
    """
    Total time to run func() reps times.
    Returns (total time, last result)

    Суммарное время выполнения функции func() reps раз
    Возвращает (суммарное время, последний результат)

    :param reps: кол-во запусков функции func()
    :param func: вызываемая функция
    :param args: позиционные аргументы вызываемой функции
    :param kwargs: ключевые аргументы вызываемой функции
    :return: (суммарное время, последний результат)
    """
    reps_list = list(range(reps))  # вынести за пределы и уравнять Python 2.x, 3.x
    start = timer()
    ret = None
    for _ in reps_list:
        ret = func(*args, **kwargs)
    elapsed = timer() - start
    return elapsed, ret


def bestof(reps, func, *args, **kwargs):
    """
    Quickest func() among reps runs.
    Return (best time, last result)

    Самая быстрая функция func() среди reps запусков
    Возвращает (лучшее время, последний результат)

    :param reps: кол-во запусков функции func()
    :param func: вызываемая функция
    :param args: позиционные аргументы вызываемой функции
    :param kwargs: ключевые аргументы вызываемой функции
    :return:
    """
    best = 2 ** 32  # 136 лет представляется достаточным (время предыдущего запуска)
    ret = None
    for i in range(reps):
        start = timer()
        ret = func(*args, **kwargs)
        elapsed = timer() - start  # Или вызвать total() с reps=1
        if elapsed < best:
            best = elapsed  # Или добавить в список и найти min()
    return best, ret


def bestof_total(reps1, reps2, func, *args, **kwargs):
    """
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))

    Лучшее суммарное время:
    (лучшее время из resp1 запусков (суммарное время resp2 запусков func))

    :param reps1:
    :param reps2:
    :param func:
    :param args:
    :param kwargs:
    :return:
    """
    return bestof(reps1, total, reps2, func, *args, **kwargs)
