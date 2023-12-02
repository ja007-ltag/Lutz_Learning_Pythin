class NextClass:
    def printer(self, text):
        self.message = text
        print(self.message)


if __name__ == '__main__':
    x = NextClass()
    x.printer('instance call')
    print(repr(x.message))
