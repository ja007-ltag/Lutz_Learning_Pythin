def f1(a, b): print(a, b)  # Нормальные аргументы


def f2(a, *b): print(a, b)  # Переменное количество позиционных аргументов


def f3(a, **b): print(a, b)  # Переменное количество ключевых аргументов


def f4(a, *b, **c): print(a, b, c)  # Смешанные режимы


def f5(a, b=2, c=3): print(a, b, c)  # Стандартные значения


def f6(a, b=2, *c): print(a, b, c)  # Стандартные значения и переменное количество позиционных аргументов
