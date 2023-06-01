#! /usr/bin/python2
"""
Emulates most of the print function from Python 3.X for use in Python 2.X (and Python 3.x).
Call signature: print3(*args, sep=' ', end='\n', file=sys.stdout)
"""
import sys


def print3(*args, **kwargs):
    sep = kwargs.get('sep', ' ')  # Keyword arg default
    end = kwargs.get('end', '\n')
    file = kwargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)
