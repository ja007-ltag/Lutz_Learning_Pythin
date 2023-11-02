import math
from functools import reduce

import timeit


def fact_recurs(n):
    return n if n == 1 else n * fact_recurs(n-1)


def fact_reduce(n):
    return reduce(lambda x, y: x*y, range(1, n+1))


def fact_for(n):
    res = 1
    for x in range(1, n+1):
        res *= x
    return res


def fact_match(n):
    return math.factorial(n)


if __name__ == '__main__':
    tuple_func = (fact_recurs, fact_reduce, fact_for, fact_match)
    num = 6
    total_dict = {}

    for func in tuple_func:
        print(f'{func.__name__:11}: {func(num)}')

    for func in tuple_func:
        func_name = func.__name__
        stmt = f'{func_name}({num})'
        total_time1 = timeit.timeit(stmt=stmt, setup=f'from __main__ import {func_name}')
        total_time2 = timeit.timeit(stmt=stmt, globals=globals())

        total_dict[func_name] = min(total_time1, total_time2)

        run_func = f'{func_name}({num})'
        print(f'{run_func:15}: {total_time1:.3f} {total_time2:.3f}')

    print()
    print(timeit.timeit(stmt=f'[func({num}) for func in tuple_func]', globals=globals()))
    print()

    print(total_dict)

    print(f'Вывод: самая быстрая функция: {min(total_dict, key=lambda key: total_dict[key])}')

    # print(timeit.timeit(stmt=f'fact_recurs({num})', globals=globals()))
    # print(timeit.timeit(stmt=f'fact_reduce({num})', globals=globals()))
    # print(timeit.timeit(stmt=f'fact_for({num})', globals=globals()))
    # print(timeit.timeit(stmt=f'fact_match({num})', globals=globals()))
