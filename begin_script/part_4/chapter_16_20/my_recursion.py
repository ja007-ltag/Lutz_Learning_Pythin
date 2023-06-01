def mysum(L):
    # print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])


def mysum1(L):
    return 0 if not L else L[0] + mysum1(L[1:])


def mysum2(L):
    return L[0] if len(L) == 1 else L[0] + mysum2(L[1:])


def mysum3(L):
    first, *rest = L
    return first if not rest else first + mysum3(rest)


if __name__ == '__main__':
    print(mysum([1, 2, 3, 4, 5]))
    print(mysum1([1, 2, 3, 4, 5]))
    print()
    print(mysum2.__name__)
    print(mysum2([1, 2, 3, 4, 5]))
    print(mysum2(['a', 'b', 'c', 'd', 'e']))
    print(mysum2(['sp', 'am']))
    print()
    print(mysum3.__name__)
    print(mysum3([1, 2, 3, 4, 5]))
    print(mysum3(['a', 'b', 'c', 'd', 'e']))
    print(mysum3(['sp', 'am']))
    print()
    # print(mysum1(['s', 'p', 'a', 'm']))
    print(mysum2(['s', 'p', 'a', 'm']))
    print(mysum3(['s', 'p', 'a', 'm']))
    print('-----spam-------')
    # print(mysum1(['spam']))
    print(mysum2(['spam']))
    print(mysum3(['spam']))
    print('-------')
    print(mysum3(open('script2.py')))
