"""
Измерение времени различных реализаций
функции реверса строки
"""

from string import ascii_uppercase
from timeit import repeat


def rev1(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + rev1(s[:-1])


def rev2(s):
    return ''.join(reversed(s))


def rev3(s):
    return s[::-1]


if __name__ == '__main__':
    s1 = ((ascii_uppercase + '-') * 3)[:-1]
    print(rev1(s1) == rev2(s1) == rev3(s1))
    print(s1)

    for func in rev1, rev2, rev3:
        print(func.__name__, min(repeat(stmt=lambda: func(s1), number=1000000, repeat=10)))
        print(func.__name__, min(repeat(stmt='func(s1)', number=1000000, repeat=10, globals=globals())))
        print(func(s1))
