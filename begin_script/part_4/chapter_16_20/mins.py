def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res


def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first


def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]


def min4(*args):
    return sorted(args)[0]


def max1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg > res:
            res = arg
    return res


def max2(first, *rest):
    for arg in rest:
        if arg > first:
            first = arg
    return first


def max3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[-1]


def max4(*args):
    return sorted(args)[-1]


if __name__ == '__main__':
    funcs = [min1, min2, min3, min4, max1, max2, max3, max4]
    tests = [[3, 4, 1, 2],
             ['bb', 'aa', 'cc'],
             [[2, 2], [1, 2], [1, 1], [3, 3]]]

    for f in funcs:
        for test in tests:
            # print(f.__name__, test, f(*test))
            print(f'{f.__name__}({str(test)[1:-1]}) = {f.__name__[:3]}: {f(*test)}')
        print('---')
