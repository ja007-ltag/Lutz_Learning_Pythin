"""
Тут функции пересечения и объединения.
А так же функция тестирования, с перестановкой аргументов:
[4, 1, 2, 3]
[3, 4, 1, 2]
[2, 3, 4, 1]
[1, 2, 3, 4]
"""


def intersect(*args):
    """Функция пересечения"""
    res = []
    for x in args[0]:
        if x in res:
            continue
        for other in args[1:]:
            if x not in other:
                break
        else:
            res.append(x)
    return res


def union(*args):
    """Функция объединения"""
    res = []
    for seq in args:
        for x in seq:
            if x not in res:
                res.append(x)
    return res


def tester(func, items, trace=True):
    """Функция тестирования с перестановкой items-ов"""
    for i in range(len(items)):
        items = items[:1] + items[1:]
        if trace:
            print(items)
        print(sorted(func(*items)))
    print('---/END/---')


if __name__ == '__main__':
    tester(intersect, ('a', 'abcdefg', 'abdst', 'albmcnd'))
    tester(union, ('a', 'abcdefg', 'abdst', 'albmcnd'), False)
    tester(intersect, ('ba', 'abcdefg', 'abdst', 'albmcnd'), False)

    print('Дубликаты не появляются, жрёт разнородные итерируемые объекты:')
    print(intersect([1, 2, 1, 3], (1, 1, 4)))
    print(union([1, 2, 1, 3], (1, 1, 4)))

    tester(intersect, ('ababa', 'abcdefga', 'aaaabbbbbb'), False)
    tester(union, ('ababa', 'abcdefga', 'aaaabbbbbb'), False)
