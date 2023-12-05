from tkinter import Button


class Callback:
    def __init__(self, color):
        self.color = color

    def __call__(self):
        print('turn', self.color)


# Обработчики
cb1 = Callback('blue')
cb2 = Callback('green')

B1 = Button(command=cb1)
B2 = Button(command=cb2)

cb1()
cb2()


def callback(color):
    def oncall():
        print('turn', color)
    return oncall


cb3 = callback('yellow')
cb3()

cb4 = (lambda color='red': 'turn ' + color)
print(cb4())


class Callback:
    def __init__(self, color):
        self.color = color

    def change_color(self):
        print('turn', self.color)


cb1 = Callback('blue')
cb2 = Callback('yellow')

B3 = Button(command=cb1.change_color)
B4 = Button(command=cb2.change_color)

cb1 = Callback('blue')
obj = cb1.change_color
obj()
