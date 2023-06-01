#! /usr/bin/python3 -i

def tester(start):
    def nester(label):
        print(label, nester.state)
        nester.state += 1
    nester.state = start
    return nester


F = tester(0)
F('spam')
F('ham')

G = tester(42)
G('eggs')
print(F.state)
print(G.state)
