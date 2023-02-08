# Пример использования форматирования, основанного на словаре.

reply = """
Greetings...
Hello %(name)s!
Your age in %(age)s
"""

values = {'name': 'Bob', 'age': 40}
print(reply % values)

print()
print(reply)
