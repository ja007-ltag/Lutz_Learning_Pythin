def sumtree1(L):  # Явная очередь с обходом в ширину
    tot = 0
    items = list(L)  # Начать с копии верхнего уровня
    while items:
        front = items.pop(0)  # Извлечь и удалить элемент в начале
        if not isinstance(front, list):
            print(front, end=', ')
            tot += front  # Напрямую суммировать числа
        else:
            items.extend(front)  # <== Добавить все из вложенного подсписка
    return tot


def sumtree2(L):  # Явный стек с обходом в глубину
    tot = 0
    items = list(L)  # Начать с копии верхнего уровня
    while items:
        front = items.pop(0)  # Извлечь и удалить элемент в начале
        if not isinstance(front, list):
            print(front, end=', ')
            tot += front  # Напрямую суммировать числа
        else:
            items[:0] = front  # <== Присоединить спереди все из вложенного подсписка
    return tot


L = [1, [2, [3, 4], 5], 6, [7, 8], [[[[[[[[[[[[[[[[9]]]]]]]], 10]]]]]]]]]
print(sumtree1(L))
print(sumtree1([1, [2, [3, [4, [5]]]]]))
print(sumtree1([[[[[1], 2], 3], 4], 5]))
print('-' * 50)

print(sumtree2(L))
print(sumtree2([1, [2, [3, [4, [5]]]]]))
print(sumtree2([[[[[1], 2], 3], 4], 5]))
print('-' * 50)