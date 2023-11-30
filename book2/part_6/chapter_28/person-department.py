# -*- coding: utf-8 -*-

from person import Person, Manager


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def add_member(self, person):
        self.members.append(person)

    def give_raises(self, percent):
        for person in self.members:
            person.give_raise(percent)

    def show_all(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Jones', pay=50000)

    development = Department(bob, sue)
    development.show_all()

    development.add_member(tom)
    development.show_all()

    development.give_raises(.10)
    development.show_all()
