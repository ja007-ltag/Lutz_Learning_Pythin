class Class:
    X = 2

    def method(self):
        print(X)
        print(self.X)
        self.X = 3
        print(self.X)

X = 1
obj = Class()
obj.method()
