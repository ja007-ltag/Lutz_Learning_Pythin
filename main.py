#! /usr/bin/python3

s = """ФА𐌡ЬШИВЫЕ РУБ𐌡И, БЕЗ 𐌏Т𐌡ИԿИЙ 𐌏Т 𐋏А𑀝Т𐌏ЯЩИ𐌗, КУПЮРЫ ПРИ𐋏И𐌑АЕТ ЛЮБОЙ БА𐋏𐌺𐌏𐌑АТ.

ԿТ𐌏БЫ 𐋏АЙТИ 𐋏АШ 𐌑А𐌲АЗИ𐋏: 𐋏АПИШИТЕ В П𐌏И𑀝КЕ ТЕ𐌡𐌲РА𐌑A : GFDK50"""

for word in s.split():
    code = ' '.join([str(ord(car)) for car in word])
    print(f"{word} = {code}")