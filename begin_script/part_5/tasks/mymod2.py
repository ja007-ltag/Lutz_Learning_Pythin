def count_lines(name):
    # count = 0
    # for _ in open(name, encoding='utf-8'):
    #     count += 1
    # return count
    return sum(+1 for _ in open(name, encoding='utf-8'))
    # return len(open(name, encoding='utf-8').readlines())


def count_chars(name):
    # counts = 0
    # for line in open(name, encoding='utf-8'):
    #     counts += len(line)
    # return counts

    return sum(len(line) for line in open(name, encoding='utf-8'))
    # return len(open(name, encoding='utf-8').read())


def test(name):
    print(f'Тестируемый файл: {name}')
    print(f'Количество строк: {count_lines(name):,}')
    print(f'Количество символов: {count_chars(name):,}')


if __name__ == '__main__':
    test("test2.txt")
    test("test_file.txt")
    test("scenario_0055_0001_0001_0001.log")
