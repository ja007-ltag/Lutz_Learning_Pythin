# -*- coding: utf-8 -*-
"""
В этом файле импорты интересных и полезных инструментов,
загружаемых автоматически при запуске интерактивного сеанса


Путь к файлу прописан в переменной среды PYTHONSTARTUP,
но пока что-то идёт не так, не получается сделать универсальный импорт.

Пока сделал обходную заглушку. Вроде работает


функция listing(<module>) выводит листинг имен другого модуля
"""

# Заглушка импорта, добавил путь на время импорта, затем его удалил
_temp_names = set(dir())

import sys as _sys
_temp_path = _sys.path[:]
_sys.path.append(r'D:\Projects\PyCharm\Lutz_Learning_Python\begin_script\part_5\chapter_25')
_temp_version = _sys.version_info

if not (_temp_version[0] == 2 and _temp_version[1] <= 5):
    from mydir import listing
    from reloadall3 import reload_all

# удаляем, проверяем, подчищаем
_sys.path.pop()
assert _temp_path == _sys.path and _temp_path is not _sys.path

if _temp_version[0] == 3:
    print('\nДополнительные функции успешно загружены!')
    print('Проверьте переменную среды PYTHONSTARTUP! :-)')
elif _temp_version[0] == 2 and _temp_version[1] > 5:
    print('\nAdditional functions loaded successfully!')
    print('Check the PYTHONSTARTUP environment variable! :-)')
elif _temp_version[0] == 2 and _temp_version[1] <= 5:
    pass
else:
    raise SystemError

del _sys, _temp_path


if _temp_version[0] == 3 or (_temp_version[0] == 2 and _temp_version[1] > 5):
    _temp_names = set(dir()) - _temp_names
    _temp_names.discard('_temp_names')
    _temp_names.discard('_temp_version')
    _temp_names = ', '.join(_temp_names)
    print('-> New objects: {0}\n'.format(_temp_names))
elif _temp_version[0] == 2 and _temp_version[1] <= 5:
    pass
else:
    raise SystemError


del _temp_names, _temp_version
