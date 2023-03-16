D = {'b': 2, 'c': 3, 'a': 1, 'd': 4}

for key in sorted(D, reverse=True):
    print(key, '=>', D[key])
