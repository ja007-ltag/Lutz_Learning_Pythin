def count_lines(name):
    name.seek(0)
    count = 0
    for _ in name:
        count += 1
    return count


def count_chars(name):
    name.seek(0)
    return sum(len(line) for line in name)


def count_lines_chars(name):
    name.seek(0)
    lines = 0
    chars = 0
    for line in name:
        lines += 1
        chars += len(line)
    return lines, chars


def test(name):
    file = open(name, encoding='utf-8')

    print(f'Тестируемый файл: {name}')
    print(f'Количество строк: {count_lines(file):,}')
    print(f'Количество символов: {count_chars(file):,}')
    cnt_line, cnt_count = count_lines_chars(file)
    print(f'Итого в файле: строк = {cnt_line:,}, символов = {cnt_count:,}.')

    file.close()


if __name__ == '__main__':
    test("test2.txt")
    test("test_file.txt")
    test("scenario_0055_0001_0001_0001.log")
    test("mymod.py")
