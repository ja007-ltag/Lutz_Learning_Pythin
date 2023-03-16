L = [1, 2, 4, 8, 16, 32, 64]
X = 5
found = False
i = 0

while not found and i < len(L):
    if 2 ** X == L[i]:
        found = True
    else:
        i = i + 1

if found:
    print('at index', i)
else:
    print(X, 'not found')

# а
L = [1, 2, 4, 8, 16, 32, 64]
X = 5
i = 0

while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    i = i + 1
else:
    print(X, 'not found')

# б
L = [1, 2, 4, 8, 16, 32, 64]
X = 5

for val in L:
    if 2 ** X == val:
        print('at index', L.index(val))
        break
else:
    print(X, 'not found')

# в
L = [1, 2, 4, 8, 16, 32, 64]
X = 5

if 2 ** X in L:
    print(2 ** X, 'at index', L.index(2 ** X))
else:
    print(X, 'not found')

# г
X = 5
L = []
for i in range(7):
    L.append(2 ** i)

if 2 ** X in L:
    print(2 ** X, 'at index', L.index(2 ** X))
else:
    print(X, 'not found')

# д
X = 5
L = []
for i in range(7):
    L.append(2 ** i)

find = 2 ** X

if find in L:
    print('at index', L.index(find))
else:
    print(X, 'not found')

# е
X = 5

# L = list(map(lambda x: 2 ** x, range(7)))
L = [2 ** x for x in range(7)]

find = 2 ** X

if find in L:
    print('at index', L.index(find))
else:
    print(X, 'not found')
