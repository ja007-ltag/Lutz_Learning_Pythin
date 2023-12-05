#! /usr/bin/python3
# -*- coding: utf-8 -*-

# """Ага, скажете что это я занимаюсь спамом.
# А я просто хотел посмотреть какие коды используются у символов"""
#
# s = """ФА𐌡ЬШИВЫЕ РУБ𐌡И, БЕЗ 𐌏Т𐌡ИԿИЙ 𐌏Т 𐋏А𑀝Т𐌏ЯЩИ𐌗, КУПЮРЫ ПРИ𐋏И𐌑АЕТ ЛЮБОЙ БА𐋏𐌺𐌏𐌑АТ.
#
# ԿТ𐌏БЫ 𐋏АЙТИ 𐋏АШ 𐌑А𐌲АЗИ𐋏: 𐋏АПИШИТЕ В П𐌏И𑀝КЕ ТЕ𐌡𐌲РА𐌑A : GFDK50"""
#
# for word in s.split():
#     code = ' '.join([str(ord(car)) for car in word])
#     print(f"{word} = {code}")

class Cats:
    __set_attr = {
        'id': 0,
        'name': 'Biggie',
        'spec': 'swing'
    }

    def __init__(self):
        self.__dict__ = self.__set_attr
        if self.__dict__['id'] == self.__dict__['id']:
            self.__dict__['id'] += 1


cat1 = Cats()
cat2 = Cats()

print(cat1.id)
print(cat2.id)
