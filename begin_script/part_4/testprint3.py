#! /usr/bin/python3

# from print3 import print3
# from print3_alt1 import print3
from print3_alt2 import print3
import sys

print3('VERSION:', sys.version.split()[0])
print3(1, 2, 3)
print3(1, 2, 3, sep='')
print3(1, 2, 3, sep='...')
print3(1, [2], (3,), True, sep='...')
print3(4, 5, 6, sep='', end='')
print3(7, 8, 9)
print3()

print3(1, 2, 3, sep='??', end='.\n', file=sys.stderr)
