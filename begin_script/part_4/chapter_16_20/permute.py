"""Перестановки: все возможные комбинации"""


def permute1(seq):
    if not seq:  # Тасование любой последовательности: список
        return [seq]  # Пустая последовательность: [[]]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i + 1:]  # Удаление текущего узла
            for x in permute1(rest):  # Рекурсивная перетасовка остальных
                res.append(seq[i:i + 1] + x)  # Добавление узла спереди
        return res


def permute2(seq):
    if not seq:  # Тасование любой последовательности: генератор
        yield seq  # Пустая последовательность: []
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i + 1:]  # Удаление текущего узла
            for x in permute2(rest):  # Рекурсивная перетасовка остальных
                yield seq[i:i + 1] + x  # Добавление узла спереди


if __name__ == '__main__':

    # sequence = list(range(1, 11+1))
    # all_permute = permute1(sequence)
    #
    # print(*all_permute, sep='\n')
    # print(len(all_permute))

    # count = 0
    # for cur in permute2(sequence):
    #     # print(cur)
    #     count += 1
    #     if not count % 1000000:
    #         print(f'{count:10,}: {cur}')
    #
    # print(f'{count:10,}')
    # print(sequence)

    count = 0
    sequence = 'ABCDEFGH'
    for cur in permute2(sequence):
        count += 1
        if count % len(sequence) != 0:
            print(cur, end=' ')
        else:
            print(cur)
