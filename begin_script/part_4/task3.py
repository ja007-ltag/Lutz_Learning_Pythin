def adder(*args):
    print('adder', end=' ')
    res = args[0]
    for item in args[1:]:
        res += item
    return res


def adder1(*args):
    print('adder1', end=' ')
    if type(args[0]) == type(0) or type(args[0]) == type(.0):  # Целое число? Инициализировать нулем
        res = 0
    else:                          # Иначе последовательность: использовать пустой срез arg1
        res = args[0][:0]
    for arg in args:
        res = res + arg
    return res


def adder2(*args):
    print('adder2', end=' ')
    res = args[0]
    for arg in args[1:]:
        res += arg
    return res


if __name__ == '__main__':
    for func in adder, adder1:

        print(func('Hello', 'world'))
        print(func('Hello'))
        print(func(0.1, 0.2, 3, 123))
        print(func([1, 2, 3], [10, 12], [4, 5, 6]))
        print(func((1, 2), (3, 4)))
        print(func((1, 2), (3, 4), (5, 7)))
        print(func((1, 2), (3,)))

        # print(func({1, 2, 3}, {4, 5, 7}))
        print('-' * 20)

print('END')
