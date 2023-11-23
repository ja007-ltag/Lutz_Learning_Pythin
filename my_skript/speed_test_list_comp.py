"""
Испытание скорости list comp, с различными входными данными
"""
import random
import timeit

n = 1_000
s1 = {x for x in range(0, n + 1, 2)}  # множество
s2 = [x for x in range(0, n + 1, 2)]  # список упорядоченный по возрастанию
s3 = tuple(s2)  # кортеж упорядоченный по возрастанию

s4 = list(reversed(s2))  # список упорядоченный по убыванию
s5 = tuple(s4)  # кортеж упорядоченный по убыванию

s6 = [x for x in range(0, n + 1, 2)]
random.shuffle(s6)  # перемешанный список
s7 = tuple(s6)  # перемешанный кортеж

s8 = set(s6)  # множество из перемешанного списка

stmts = [
    ('[x for x in range(n+1) if x in s1]', 'множество'),
    ('[x for x in range(n+1) if x in s2]', 'список упорядоченный по возрастанию'),
    ('[x for x in range(n+1) if x in set(s2)]', ''),
    ('[x for x in range(n+1) if x in s3]', 'кортеж упорядоченный по возрастанию'),
    ('[x for x in range(n+1) if x in set(s3)]', ''),
    ('[x for x in range(n+1) if x in s4]', 'список упорядоченный по убыванию'),
    ('[x for x in range(n+1) if x in set(s4)]', ''),
    ('[x for x in range(n+1) if x in s5]', 'кортеж упорядоченный по убыванию'),
    ('[x for x in range(n+1) if x in set(s5)]', ''),
    ('[x for x in range(n+1) if x in s6]', 'перемешанный список'),
    ('[x for x in range(n+1) if x in set(s6)]', ''),
    ('[x for x in range(n+1) if x in s7]', 'перемешанный кортеж'),
    ('[x for x in range(n+1) if x in set(s7)]', ''),
    ('[x for x in range(n+1) if x in s8]', 'множество из перемешанного списка'),
]

param = dict(globals=globals(), number=100, repeat=5)

if __name__ == '__main__':
    max_stmt = max(len(x[0]) for x in stmts)
    max_description = max(len(x[0]) for x in stmts)
    for num, (stmt, description) in enumerate(stmts):
        if num % 2 != 0:
            print()

        print(f'{stmt:>{max_stmt}} {description:>{max_description}}', end=' ... ')
        print(min(timeit.repeat(stmt=stmt, **param)))
