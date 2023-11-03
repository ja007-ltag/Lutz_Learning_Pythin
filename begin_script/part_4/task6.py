"""
Словарные инструменты. Напишите функцию по имени addDict (dictl, dict2), которая вычисляет объединение двух словарей.
Она должна возвращать новый словарь, содержащий все элементы из своих двух аргументов
(по предположению являющиеся словарями). Если в обоих аргументах встречается один и тот же ключ,
выбирайте значение из любого по своему усмотрению.
Протестируйте написанную функцию, запустив файл как сценарий. Что произойдет, если передать списки вместо словарей?
Как можно было бы обобщить функцию для обработки такого случая?
(Подсказка: примените упомянутую ранее встроенную функцию type.)
Имеет ли значение порядок, в котором передаются аргументы?
"""


def add_dict(dict1, dict2):
    if not (isinstance(dict1, dict) and isinstance(dict2, dict)):
        return "Принимаем только словари"

    # res = dict1.copy()
    # for key in dict2:
    #     res[key] = dict2[key]
    # return res

    res = dict1.copy()
    res.update(dict2)
    return res


if __name__ == '__main__':
    d1 = dict(a=1, b=2)
    d2 = dict(a=3, d=4)

    d_all = add_dict(d1, d2)
    print(d_all)
    print(f"{d_all is d1 = }")
    print(f'{d_all is d2 = }')

    print(f'{d1 = }')
    d1.update(d2)
    print(f'{d1 = }')

    

    # for cur in dict_list:
    #     out = copy_dict(cur)
    #     print(f"Test: {cur}")
    #     assert cur is not out

    # print("All test complete")
