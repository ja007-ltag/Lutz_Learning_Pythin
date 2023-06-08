"""Draft"""


# import sys
# from tkinter import Button, mainloop
# x = Button(
#     text='Press me',
#     command=lambda: sys.stdout.write('Spam\n')
# )
# x.pack()
# mainloop()
def can_get(n):
    run = 0

    def func():
        nonlocal run
        if run < n:
            run += 1
            return True
        else:
            return False
    return func


can_get_two = can_get(2)
# assert can_get_two() is True
# assert can_get_two() is True
# assert can_get_two() is False
# assert can_get_two() is False
for _ in range(5):
    print(can_get_two())
