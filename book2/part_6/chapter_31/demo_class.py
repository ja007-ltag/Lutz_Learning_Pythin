class Spam:
    def doit(self, message):
        print(message)


object1 = Spam()
object1.doit('Hello world')

x = object1.doit
x('Hello world')

t = Spam.doit
t(object1, 'howdy')


class Eggs:
    def m1(self, n):
        print(n)

    def m2(self):
        x = self.m1
        x(42)
    

Eggs().m2()
