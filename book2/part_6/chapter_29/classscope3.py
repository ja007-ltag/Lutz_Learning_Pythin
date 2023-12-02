X = 1


def nester():
    X = 2
    print(X, 1)

    class C:
        X = 3
        print(X, 2)

        def method1(self):
            print(X, 4)  # !!! = 2
            print(self.X, 5) # 3

        def method2(self):
            X = 4
            print(X, 6)  # 4
            self.X = 5
            print(self.X, 7) # 5

        print(X, 3)

    I = C()
    I.method1()
    I.method2()
    print(X, 8)     # 2
    print(C.X, 9)   # 3
    print(I.X, 10)  # 5


# print(X)
nester()
