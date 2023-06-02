"""
Homegrown timing tools for function calls.
Does total time, best-of time, and best-of-totals time
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

print('Platform: {}, python: {}'.format(sys.platform, sys.version.split()[0]))
print('Select function: {}'.format(timer.__name__))


def total(reps, func, *args, **kwargs):
    """
    Total time to run func() reps times.
    Returns (total time, last result)
    """
    reps_list = list(range(reps))
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
    """
    best = 2 ** 32
    ret = None
    for i in range(reps):
        start = timer()
        ret = func(*args, **kwargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return best, ret


def bestof_total(reps1, reps2, func, *args, **kwargs):
    """
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    """
    return bestof(reps1, total, reps2, func, *args, **kwargs)
