def tracer(func, *args, **kwargs):
    print('calling:', func.__name__)
    return func(*args, **kwargs)


def function_main(a, b, c, d):
    return a + b + c + d


print(tracer(function_main, *(1, 2), d=4, c=3))
