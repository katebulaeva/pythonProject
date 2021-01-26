from functools import reduce


def func(a, b):
    return a * b

print(reduce(func, [el for el in range(99, 1001) if el % 2 == 0]))

print([el for el in range(99, 1001) if el % 2 == 0])
