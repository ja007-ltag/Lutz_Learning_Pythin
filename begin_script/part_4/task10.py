# -*- coding: utf-8 -*-

"""
Измерение времени выполнения инструментов.
Какой из способов вычисления квадратного корня быстрее:
math.sqrt(X), X ** .5 или pow(X, .5)
"""

import sys
import chapter_21.timer as timer
import math

reps = 10000
reps_list = list(range(reps))


def sgrt_list_comp():
    return [math.sqrt(x) for x in reps_list]


def multi_list_comp():
    return [x ** .5 for x in reps_list]


def pow_list_comp():
    return [pow(x, .5) for x in reps_list]


def sgrt_for_loop():
    res = []
    for x in reps_list:
        res.append(math.sqrt(x))
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
    return list(map(math.sqrt, reps_list))


def multi_map_call():
    return list(map(lambda x: x ** .5, reps_list))


def pow_map_call():
    return list(map(lambda x: pow(x, .5), reps_list))


if __name__ == '__main__':
    print(sys.version)
    test_func = (sgrt_list_comp, multi_list_comp, pow_list_comp,
                 sgrt_for_loop, multi_for_loop, pow_for_loop,
                 sgrt_map_call, multi_map_call, pow_map_call,)
    for test in test_func:
        (bestof, (total, result)) = timer.bestof_total(5, 1000, test)
        print('%-15s: %.5f => [%s...%s]' %
              (test.__name__, bestof, result[0], result[-1]))
