def is_prime(y):
    if y <= 1:
        print(y, 'is отрицательное')
    else:
        x = y // 2
        while x > 1:
            if y % x == 0:
                print(y, 'has factor', x)
                break
            x -= 1
        else:
            print(y, 'is prime')


def prime(y):
    if y <= 1:
        return False
    else:
        for x in range(int(y // 2), 1, -1):
            if y % x == 0:
                return x
        else:
            return True


if __name__ == '__main__':
    nums = (13, 13.0, 15, 15.0, 0, 1, 3, 2, 1, -3)
    for num in nums:
        print(num, prime(num), end=' ')
        is_prime(num)