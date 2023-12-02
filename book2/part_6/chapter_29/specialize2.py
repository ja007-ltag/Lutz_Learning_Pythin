# -*- coding: utf-8 -*-
import sys
from abc import ABCMeta, abstractmethod


# class Super3(metaclass=ABCMeta):  # in Python 3.X
#     @abstractmethod
#     def method(self, ...):
#         pass
#
#
# class Super2:   # in Python 2.6+
#     __metaclass__ == ABCMeta
#     @abstractmethod
#     def method(self, ...):
#         pass


# # For Python 2.6+
# class Super:
#     __metaclass__ = ABCMeta
#
#     def method(self):
#         print('in Super.method')     # Стандартное поведение
#
#     def delegate(self):
#         self.action()                # Ожидается определение метода
#
#     @abstractmethod
#     def action(self):
#         pass


# From Python 3.X
class Super(metaclass=ABCMeta):
    def method(self):
        print('in Super.method')     # Стандартное поведение

    def delegate(self):
        self.action()                # Ожидается определение метода

    @abstractmethod
    def action(self):
        pass
