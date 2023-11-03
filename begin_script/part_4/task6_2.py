"""
Функция для объединения любого количества словарей
"""


def add_dicts(*dicts):
    new = {}
    for cur in dicts:
        for key in cur:
            new[key] = cur[key]
    return new


def add_dicts2(*dicts):
    return {key: cur[key] for cur in dicts for key in cur}


if __name__ == '__main__':
    d1 = dict(a=1, b=2)
    d2 = dict(a=3, d=4)
    d3 = dict(e=5, f=6)

    print(add_dicts(d1, d2))
    print(add_dicts(d1, d2, d3))

    print(add_dicts2(d1, d2))
    print(add_dicts2(d1, d2, d3))
