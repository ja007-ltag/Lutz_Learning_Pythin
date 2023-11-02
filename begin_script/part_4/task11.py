def countdown(n):
    if n == 0:
        print('stop')
    else:
        print(n, end=' ')
        countdown(n-1)


def countdown2(n):
    while n >= 0:
        yield n if n > 0 else 'stop'
        n -= 1


# for x in countdown2(5):
#     print(x)

countdown(5)
print(*countdown2(5))

res = ' '.join([str(x) if x > 0 else 'stop' for x in range(5, -1, -1)])
print(res)

gen_res = (x if x > 0 else 'stop' for x in range(5, -1, -1))
print(*gen_res)
