# -*- coding: utf-8 -*-

class PrivateExc(Exception):  # Исключения подробно рассматриваются в части VII
    pass


class Privacy:
    def __setattr__(self, attr_name, value):  # Вызывается для self.attr_name = value
        if attr_name in self.privates:
            raise PrivateExc(attr_name, self)  # Сгенерировать определяемое пользователем исключение
        else:
            self.__dict__[attr_name] = value  # Избежать зацикливания, используя ключ словаря


class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__dict__['name'] = 'Tom'  # Чтобы сделать лучше, обратитесь в главу 39!


if __name__ == '__main__':
    x = Test1()
    y = Test2()

    x.name = 'Bob'    # Работает
    # y.name = 'Sue'  # Терпит неудачу
    print(x.name)

    y.age = 30        # Работает
    # x.age = 40      # Терпит неудачу
    print(y.age)
