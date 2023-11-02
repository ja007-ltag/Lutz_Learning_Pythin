def adder(*args):
    res = args[0]
    for item in args[1:]:
        res += item
    return res


print(adder('Hello', 'world'))
print(adder('Hello'))
print(adder(0.1, 0.2, 3, 123))
print(adder([1, 2, 3], [10, 12], [4, 5, 6]))
print(adder((1, 2), (3, 4)))
print(adder((1, 2), (3, 4), (5, 7)))
print(adder((1, 2), (3,)))

print(adder({1, 2, 3}, {4, 5, 7}))

