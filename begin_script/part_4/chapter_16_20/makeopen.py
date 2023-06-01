import builtins


def makeopen_def(id):
    original = builtins.open

    def custom(*pargs, **kargs):
        print('Custom open call %r:' % id, pargs, kargs)
        return original(*pargs, **kargs)

    builtins.open = custom


class makeopen:
    def __init__(self, id):
        self.id = id
        self.original = builtins.open
        builtins.open = self

    def __call__(self, *args, **kwargs):
        print('Custom open call %r:', args, kwargs)
        return self.original(*args, **kwargs)
