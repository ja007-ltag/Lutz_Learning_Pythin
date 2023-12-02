X = 1


def nester():
    X = 2
    print(X, 1)

    class C:
        print(X, 2)

        def method1(self):
            print(X, 4)

        def method2(self):
            X = 3
            print(X, 5)

        print(X, 3)

    I = C()
    I.method1()
    I.method2()
    print(X, 6)


# print(X)
nester()
