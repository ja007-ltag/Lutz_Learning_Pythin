"""
"Обратный отсчёт" при помощи генераторных функций
"""


def countdown2(n):
    if n == 0:
        yield 'stop'
    else:
        yield n
        # for x in countdown2(n - 1):
        #     yield x
        yield from countdown2(n - 1)  # такая запись появилась в Python 3.3+


def countdown3(n):
    yield from range(n, 0, -1)
    yield 'stop'


def countdown4(n):
    for x in range(n, 0, -1):
        yield x
    else:
        yield 'stop'


countdown5 = (x if x > 0 else 'stop' for x in range(25, -1, -1))


if __name__ == '__main__':
    print(*countdown2(25))
    print(*countdown3(25))
    print(*countdown4(25))
    print(*countdown5)
