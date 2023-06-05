"""
Checking the relative speed of iterative alternatives.
"""

import sys
import timer_eng as timer

reps = 10000
reps_list = list(range(reps))


def for_loop():
    res = []
    for x in reps_list:
        res.append(abs(x))
    return res


def list_comp():
    return [abs(x) for x in reps_list]


def map_call_2x():
    return map(abs, reps_list)


def map_call_3x():
    return list(map(abs, reps_list))  # Only use list() in Python 3.X!
    # return map(abs, reps_list)


def gen_expr():
    return list(abs(x) for x in reps_list)  # list() is required to initialize the output


def gen_func():
    def gen():
        for x in reps_list:
            yield abs(x)
    return list(gen())  # list() is required to initialize the output


map_call = map_call_2x if sys.version_info.major == 2 else map_call_3x
map_call.__name__ = 'map_call'

print(sys.version)
for test in (for_loop, list_comp, map_call, gen_expr, gen_func):
    (bestof, (total, result)) = timer.bestof_total(5, 1000, test)
    print('%-10s: %.5f => [%s...%s]' %
          (test.__name__, bestof, result[0], result[-1]))
