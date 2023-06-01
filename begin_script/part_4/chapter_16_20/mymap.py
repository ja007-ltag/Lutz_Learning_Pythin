"""Эмуляция функции map"""


def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res


def mymap2(func, *seqs):
    return [func(*args) for args in zip(*seqs)]


def mymap3(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)


def mymap4(func, *seqs):
    return (func(*args) for args in zip(*seqs))


print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))

print(mymap2(abs, [-2, -1, 0, 1, 2]))
print(mymap2(pow, [1, 2, 3], [2, 3, 4, 5]))

print(list(mymap3(abs, [-2, -1, 0, 1, 2])))
print(list(mymap3(pow, [1, 2, 3], [2, 3, 4, 5])))

print(list(mymap4(abs, [-2, -1, 0, 1, 2])))
print(list(mymap4(pow, [1, 2, 3], [2, 3, 4, 5])))
