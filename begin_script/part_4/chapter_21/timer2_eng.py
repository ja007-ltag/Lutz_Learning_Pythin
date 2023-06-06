"""
total(spam, 1, 2, a=3, b=4, _reps=1000) calls and times spam(1, 2, a=3, b=4)
_reps times and returns the total time for all runs with the final result.

bestof(spam, 1, 2, a=3, b=4, _reps=5) runs a best-of-N test in an attempt
get rid of the influence of system load fluctuations and returns the best time
among _reps tests.

bestof_total(spam, 1, 2, a=3, b=4, _reps1=5, _reps=1000) runs the test
the best total time that takes the best of _reps1 runs
(total time _reps runs);
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


def total(func, *args, **kwargs):
    _reps = kwargs.pop('_reps', 1000)
    reps_list = list(range(_reps))
    start = timer()
    ret = None
    for _ in reps_list:
        ret = func(*args, **kwargs)
    elapsed = timer() - start
    return elapsed, ret


def bestof(func, *args, **kwargs):
    _reps = kwargs.pop('_reps', 5)
    best = 2 ** 32
    ret = None
    for i in range(_reps):
        start = timer()
        ret = func(*args, **kwargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return best, ret


def bestof_total(func, *args, **kwargs):
    _reps1 = kwargs.pop('_reps1', 5)
    return min(total(func, *args, **kwargs) for i in range(_reps1))
