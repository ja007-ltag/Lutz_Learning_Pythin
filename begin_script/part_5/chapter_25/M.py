import sys
import M
name = "Hello"

if __name__ == '__main__':
    print(M.name)
    print(sys.modules['M'].name)
    print(M.__dict__['name'])
    print(getattr(M, 'name'))
