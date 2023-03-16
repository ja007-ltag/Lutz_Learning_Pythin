S = "stroka, spam"

summa = 0
l = []
for char in S:
    print(f'{char} = {ord(char)}')
    summa += ord(char)
    l.append(ord(char))

print('---')
print(f'{summa = }')
print(f'{l = }')

print(list(map(ord, S)))
print([ord(c) for c in S])
