from functools import reduce


def fact(x, y):
    return x*y


print(reduce(fact, range(1, 5)))
