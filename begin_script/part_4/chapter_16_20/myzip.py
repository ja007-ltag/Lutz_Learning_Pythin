"""
Emulating the zip function from sidebar
"What will require attention: one-time iterations"
Chapter 20, page 638. (Before "Summary of Inclusion Syntax")
"""

from __future__ import print_function
import sys


def myzip_2x(*args):
    """For version 2.X"""
    iters = map(iter, args)
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)


def myzip_36(*args):
    """For version <= 3.6"""
    iters = list(map(iter, args))
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)


def myzip_37(*args):
    """For version >= 3.7"""
    iters = list(map(iter, args))
    while iters:
        try:
            res = [next(i) for i in iters]
        except StopIteration:
            break
        yield tuple(res)


if sys.version_info.major == 2:
    myzip = myzip_2x
elif sys.version_info.minor <= 6:
    myzip = myzip_36
else:
    myzip = myzip_37


S1 = "abc"
S2 = "123456"
print('Version: ' + sys.version.split()[0])
print(list(myzip(S1, S2)))
# for out in myzip(S1, S2):
#     print(out)

print('Universal')
print(list(myzip_37(S1, S2)))
