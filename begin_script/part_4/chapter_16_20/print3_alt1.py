#! /usr/bin/pithon3
"""Использование аргументов с передачей только по ключевым словам Python 3.X"""
import sys


def print3(*args, sep='', end='\n', file=sys.stdout):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)
