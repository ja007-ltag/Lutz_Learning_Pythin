x = -100


def f1():
    x = 11

    def f2():
        x = 22

        def f3():
            x = 33
            print(x)

        print(x)
        f3()

    print(x)
    f2()


print(x)
f1()
