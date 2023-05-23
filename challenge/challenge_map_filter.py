"""
Переписать конструкцию ниже, в вид с использованием функций map и filter.
Лутц, том 1, часть 4, стр 602
Перед "Пример: списковые включения и матрицы"
"""


res = []
for x in range(5):
    if x % 2 == 0:
        for y in range(5):
            if y % 2 == 1:
                res.append((x, y))
print(res)


res = [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
print(res)


# Короче какая-то фигня выходит. Нужно больше времени и получится что-то не читаемое. Но я верю, что это можно сделать.
# res = map(lambda x, y: (x, y), filter(lambda x: x % 2 == 0, range(5)), filter(lambda y: y % 2 == 1, range(5)))
res = filter(lambda x: x % 2 == 0, range(5))
res2 = filter(lambda y: y % 2 == 1, range(5))


print(list(res))
print(list(res2))
