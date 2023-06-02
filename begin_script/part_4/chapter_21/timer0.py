"""
В новом Python нет time.clock().
Вместо него нужно использовать
time.process_time() или
time.perf_counter() - этот мне пока понравился больше
"""

import time


def timer(func, *args):
    # start = time.process_time()
    start = time.perf_counter()  # или это использовать
    for i in range(1000):
        func(*args)
    # return time.process_time() - start
    return time.perf_counter() - start

