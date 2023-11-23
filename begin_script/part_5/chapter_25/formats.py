#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Файл: formats.py (Python 2.X и 3.X)
Разнообразные специализированные функции для форматирования строк
с целью отображения.
Тестирование можно проводить с помощью заготовленного теста
или аргументов командной строки.
Что сделать: добавить круглые скобки для отрицательных денежных сумм,
реализовать больше возможностей.
"""


def commas(n):
    """
    Форматирует положительное целое число N для отображения
    с запятыми, разделяющие группы цифр: "xxx,yyy,zzz".
    """
    digits = str(n)
    assert digits.isdigit()
    result = ''
    while digits:
        digits, last3 = digits[:-3], digits[-3:]
        result = (last3 + ',' + result) if result else last3
    return result


def money(n, num_width=0, currency='$'):
    """
    Форматирует число n для отображения с запятыми, 2 десятичными цифрами,
    ведущим символом $ и знаком, а также необязательным дополнением:
    "$ -xxx,yyy.zz"
    num_width=0 - отсутствие дополнения пробелами,
    currency='' - опустить символ $
    или символ не ASCII для других валют (например, фунт - u'\xA3' или u'\u00A3').
    """
    sign = '-' if n < 0 else ''
    n = abs(n)
    whole = commas(int(n))
    fract = ('%.2f' % n)[-2:]  # 2 символа после запятой
    number = '%s%s.%s' % (sign, whole, fract)
    return '%s%*s' % (currency, num_width, number)


if __name__ == '__main__':
    def selftest():
        tests = 0, 1  # не проходит: -1, 1.23
        tests += 12, 123, 1234, 12345, 123456, 1234567
        tests += 2 ** 32, 2 ** 100
        for test in tests:
            print(commas(test))
        print('')

        tests = 0, 1, -1, 1.23, 1., 1.2, 3.14159
        tests += 12.34, 12.344, 12.345, 12.346
        tests += 2 ** 32, (2 ** 32 + .2345)
        tests += 1.2345, 1.2, 0.2345
        tests += -1.2345, -1.2, -0.2345
        tests += -(2 ** 32), -(2 ** 32 + .2345)
        tests += (2 ** 100), -(2 ** 100)
        for test in tests:
            print('%s [%s]' % (money(test, 17), test))

    import sys
    if len(sys.argv) == 1:
        selftest()
    else:
        print(money(float(sys.argv[1]), int(sys.argv[2])))
