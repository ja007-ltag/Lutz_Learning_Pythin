class C1:
    def meth1(self):
        self.X = 88

    def meth2(self):
        print(self.X)


class C2:
    def metha(self):
        self.X = 99

    def methb(self):
        print(self.X)


class C3(C1, C2):
    pass


if __name__ == '__main__':
    I = C3()

    I.meth1()
    I.metha()
    print(I.__dict__)
    I.meth2()
    I.methb()
