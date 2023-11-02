def is_prime(y):
    x = y // 2

    if y <= 1:
        print(y, 'is отрицательное')
    else:
        while x > 1:
            if y % x == 0:
                print(y, 'has factor', x)
                break
            x -= 1
        else:
            print(y, 'is prime')


is_prime(13)
is_prime(13.0)
is_prime(15)
is_prime(15.0)
is_prime(0)
is_prime(1)