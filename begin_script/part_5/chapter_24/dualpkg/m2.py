import dualpkg.m1 as m1


def some_func():
    m1.some_func()
    print('m2.some_func')


if __name__ == '__main__':
    some_func()
