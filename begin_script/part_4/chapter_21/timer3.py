"""
Используется в точности как timer2.py, но для получения более простого кода
применяет аргументы с передачей только по ключевым словам и стандартным
значениям Python-3.x.
Выносить вызов range() за пределы тестов в Python 3.x нет нужды, т.к. он
всегда дает генератор; данная версия не будет работать в Python 2.x
"""

import sys
import time

# if sys.version_info[0] >= 3 and sys.version_info[1] >= 3:
#     timer = time.perf_counter  # or process_time
# else:
#     timer = time.clock if sys.platform[:3] == 'win' else time.time

try:
    timer = time.perf_counter
except AttributeError:
    timer = time.clock if sys.platform[:3] == 'win' else time.time

print('Platform: {0}, python: {1}'.format(sys.platform, sys.version.split()[0]))
print('Select function: time.{0}'.format(timer.__name__))


def total(func, *args, _reps=1000, **kwargs):
    start = timer()
    ret = None
    for _ in range(_reps):
        ret = func(*args, **kwargs)
    elapsed = timer() - start
    return elapsed, ret


def bestof(func, *args, _reps=5, **kwargs):
    best = 2 ** 32
    ret = None
    for i in range(_reps):
        start = timer()
        ret = func(*args, **kwargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return best, ret


def bestof_total(func, *args, _reps1=5, **kwargs):
    return min(total(func, *args, **kwargs) for _ in range(_reps1))
