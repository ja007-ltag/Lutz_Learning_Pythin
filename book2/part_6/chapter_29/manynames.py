X = 11                # Глобальное имя/атрибут модуля (X или manynames.X)


def f():
    print(X)          # Доступ к глобальному имени X (11)


def g():
    X = 22            # Локальная переменная в функции (X, скрывает X в модуле)
    print(X)


class C:
    X = 33            # Атрибут класса (C.X)

    def m(self):
        X = 44        # Локальная переменная в методе (X)
        self.X = 55   # Атрибут экземпляра (экземпляр.X)


if __name__ == '__main__':
    print(X)

    f()
    g()
    print(X)

    obj = C()
    print(obj.X)
    print(C.X)

    obj.m()
    print(obj.X)
    print(C.X)
