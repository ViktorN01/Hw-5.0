from functools import reduce

a = [n for n in list(range(100, 1001, 2))]
print(f'Произведение всех элементов списка\n', reduce(lambda x,y: x*y, a))
