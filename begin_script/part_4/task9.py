import math

L = [2, 4, 9, 16, 25]

res = []
for i in L:
    res.append(math.sqrt(i))
print(*res)

res = map(math.sqrt, L)
print(*res)  # Это лучший способ для данной задачи

res = [math.sqrt(i) for i in L]
print(*res)

res = (math.sqrt(i) for i in L)
print(*res)

