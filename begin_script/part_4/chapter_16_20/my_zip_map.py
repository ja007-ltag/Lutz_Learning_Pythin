"""
Эмуляция функций zip(seqs...) и map(None, seqs...) из Python 2.X
"""


def my_zip(*seqs):
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res


def my_map_pad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    res = []
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res


# Применение генераторов: yield
def my_zip_gen(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)


def my_map_pad_gen(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)


# Альтернативная реализация с использованием длин
def my_zip_len(*seqs):
    min_len = min(len(S) for S in seqs)
    return [tuple(S[i] for S in seqs) for i in range(min_len)]


def my_map_pad_len(*seqs, pad=None):
    max_len = max(len(S) for S in seqs)
    index = range(max_len)
    return [tuple((S[i] if len(S) > i else pad) for S in seqs) for i in index]


# Применение генераторов: (...)
def my_zip_len_gen(*seqs):
    min_len = min(len(S) for S in seqs)
    return (tuple(S[i] for S in seqs) for i in range(min_len))


def my_map_pad_len_gen(*seqs, pad=None):
    max_len = max(len(S) for S in seqs)
    index = range(max_len)
    return (tuple((S[i] if len(S) > i else pad) for S in seqs) for i in index)


S1, S2, S3 = (1, 2, 3), 'abcdef', '123'

print(list(zip(S1, S2, S3)))
print(my_zip(S1, S2, S3))
print(my_map_pad(S1, S2, S3))

print('-' * 80)
print(my_map_pad(S1, S2, S3, pad=99))

print()
print('# Применение генераторов: yield')

print(list(my_zip_gen(S1, S2, S3)))
print(list(my_map_pad_gen(S1, S2, S3)))

print()
print('# Альтернативная реализация с использованием длин')
print(my_zip_len(S1, S2, S3))
print(my_map_pad_len(S1, S2, S3))

print()
print('# Применение генераторов: (...)')
print(list(my_zip_len_gen(S1, S2, S3)))
print(list(my_map_pad_len_gen(S1, S2, S3)))

