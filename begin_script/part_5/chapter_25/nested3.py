import nested1
from nested1 import printer
nested1.X = 88
nested1.printer()
printer()
print(nested1.printer is printer)
