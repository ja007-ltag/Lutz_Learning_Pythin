"""
Checking the relative speed of iterative alternatives.
User timer2_eng.py - description in timer2.py
"""

import sys
import timer2_eng as timer2

reps = 10000
reps_list = list(range(reps))


def for_loop():
    res = []
    for x in reps_list:
        res.append(x + 10)
    return res


def list_comp():
    return [x + 10 for x in reps_list]


def map_call_2x():
    return map(lambda x: x + 10, reps_list)


def map_call_3x():
    return list(map(lambda x: x + 10, reps_list))  # Only use list() in Python 3.X!
    # return map(abs, reps_list)


def gen_expr():
    return list(x + 10 for x in reps_list)  # list() is required to initialize the output


def gen_func():
    def gen():
        for x in reps_list:
            yield x + 10
    return list(gen())  # list() is required to initialize the output


def set_for():
    res = set()
    for x in reps_list:
        res.add(x + 10)
    return res


def set_comp():
    return {x + 10 for x in reps_list}


def dict_for():
    res = {}
    for x in reps_list:
        res[x] = x + 10
    return res


def dict_comp():
    return {x: x + 10 for x in reps_list}


map_call = map_call_2x if sys.version_info.major == 2 else map_call_3x
map_call.__name__ = 'map_call'

print(sys.version)
for test in (for_loop, list_comp, map_call, gen_expr, gen_func,
             set_for, set_comp, dict_for, dict_comp):
    # (bestof, (total, result)) = timer.bestof_total(5, 1000, test)  # old

    total, result = timer2.bestof_total(test, _reps1=5, _reps=1000)
    # Or:
    # total, result = timer2.bestof(test, _reps=5)
    # total, result = timer2.total(test, _reps=1000)
    # bestof, (total, result) = timer2.bestof(timer2.total, test, _reps=5)

    if isinstance(result, (set, dict)):
        # print(type(result))
        result = list(result)
    print('%-10s: %.5f => [%s...%s]' % (test.__name__, total, result[0], result[-1]))
