from functools import reduce


def list(n_1, n2):
    return n_1 * n2


newlist = [n for n in range(100, 1001, 2)]
print(reduce(list, newlist))
