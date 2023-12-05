class C:
    data = 'spam'

    def __gt__(self, other):
        print('Run gt ">"', end=' ')
        return self.data > other

    def __lt__(self, other):
        print('Run lt "<"', end=' ')
        return self.data < other


X = C()
print(X > 'ham')
print(X < 'ham')

print('ham' < X)
print('ham' > X)
