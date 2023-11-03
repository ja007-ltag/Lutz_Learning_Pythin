# -*- coding: utf-8 -*-

"""
Измерение времени выполнения инструментов.
Какой из способов вычисления квадратного корня быстрее:
math.sqrt(X), X ** .5 или pow(X, .5)


"Как бы вы измеряли скорость выполнения включений словарей
по сравнению с циклами for в интерактивной подсказке?"

import timeit

d1 = "{k: 2 ** k for k in range(10000)}"

d2 = "d = {}\nfor k in range(10000):\n\td[k] = 2 ** k"

d3 = '''d = {}
for k in range(10000):
    d[k] = 2 ** k'''

timeit.timeit(stmt=d1, number=100)
timeit.timeit(stmt=d2, number=100)
timeit.timeit(stmt=d3, number=100)

timeit.repeat(setup='', stmt=d1, number=20, repeat=5)
timeit.repeat(setup='', stmt=d2, number=20, repeat=5)
timeit.repeat(setup='', stmt=d3, number=20, repeat=5)

min(timeit.repeat(setup='', stmt=d1, number=20, repeat=5))
min(timeit.repeat(setup='', stmt=d2, number=20, repeat=5))
min(timeit.repeat(setup='', stmt=d3, number=20, repeat=5))

Так в командной строке:
py -3.11 -m timeit -n 50 "{k: 2 ** k for k in range(10000)}"
py -3.11 -m timeit -n 50 "d = {}" "for k in range(10000):" "    d[k] = 2 ** k"
"""

import sys
import chapter_21.timer as timer
from math import sqrt

reps = 10000
reps_list = list(range(reps))


def sgrt_list_comp():
    return [sqrt(x) for x in reps_list]


def multi_list_comp():
    return [x ** .5 for x in reps_list]


def pow_list_comp():
    return [pow(x, .5) for x in reps_list]


def sgrt_for_loop():
    res = []
    for x in reps_list:
        res.append(sqrt(x))
    return res


def multi_for_loop():
    res = []
    for x in reps_list:
        res.append(x ** .5)
    return res


def pow_for_loop():
    res = []
    for x in reps_list:
        res.append(pow(x, .5))
    return res


def sgrt_map_call():
    return list(map(sqrt, reps_list))


def multi_map_call():
    return list(map(lambda x: x ** .5, reps_list))


def pow_map_call():
    return list(map(lambda x: pow(x, .5), reps_list))


if __name__ == '__main__':
    print(sys.version)
    test_func = (sgrt_list_comp, multi_list_comp, pow_list_comp,
                 sgrt_for_loop, multi_for_loop, pow_for_loop,
                 sgrt_map_call, multi_map_call, pow_map_call,)
    for num, test in enumerate(test_func):
        if num > 0 and num % 3 == 0:
            print('-' * 53)

        (bestof, (total, result)) = timer.bestof_total(5, 1000, test)
        print('%-15s: %.5f => [%s...%s]' %
              (test.__name__, bestof, result[0], result[-1]))
