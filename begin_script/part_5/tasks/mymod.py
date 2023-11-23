def count_lines(file):
    file.seek(0)
    return sum(+1 for _ in file)
    # count = 0
    # for _ in name:
    #     count += 1
    # return count


def count_chars(file):
    file.seek(0)
    return sum(len(line) for line in file)


def count_lines_chars(file):
    file.seek(0)
    lines = chars = 0
    for line in file:
        lines += 1
        chars += len(line)
    return lines, chars


def test(name):
    file = open(name, encoding='utf-8')
    # file = open(name, mode='rb')

    print(f'Тестируемый файл: {name}')
    print(f'Количество строк: {count_lines(file):,}')
    print(f'Количество символов: {count_chars(file):,}')
    cnt_line, cnt_count = count_lines_chars(file)
    print(f'Итого в файле: строк = {cnt_line:,}, символов = {cnt_count:,}.')

    file.close()


if __name__ == '__main__':
    import sys
    print(len(sys.argv))
    if len(sys.argv) == 1:
        test("test2.txt")
        test("test_file.txt")
        test("scenario_0055_0001_0001_0001.log")
        test("mymod.py")
    else:
        """
        для запуска из cmd использовать:
        py mymod.py "test2.txt"
        py mymod.py "scenario_0055_0001_0001_0001.log"
        py mymod.py "test2.txt" "test_file.txt" "scenario_0055_0001_0001_0001.log" "mymod.py"
        """
        for file in sys.argv[1:]:
            test(file)
