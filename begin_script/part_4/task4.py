def adder1(good=5, bad=3, ugly=1):
    return good + bad + ugly


def adder2(**kwargs):
    res = None
    # for value in kwargs.values():
    #     if res is None:
    #         res = value
    #     else:
    #         res += value

    for value in kwargs.values():
        res = value if res is None else res + value
    return res


print(adder2(s1='Hello ', s2='world'))
print(adder2(s='Hello'))
print(adder2(good=5, bad=3, ugly=1))
print(adder2(f1=0.1, f2=0.2, i1=3, i2=123))
print(adder2(l1=[1, 2, 3], l2=[10, 12], l3=[4, 5, 6]))
print(adder2(t1=(1, 2), t2=(3, 4)))
print(adder2(t1=(1, 2), t2=(3, 4), t3=(5, 7)))
print(adder2(t1=(1, 2), t2=(3,)))

print(adder2(**{'good': 5, 'bad': 3, 'ugly': 1}))
#
# print(adder2(set1={1, 2, 3}, set2={4, 5, 7}))

