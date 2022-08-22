from random import randint

list = [randint(-10, 10) for _ in range(20)]
list_new = [n for n in list if list.count(n) == 1]
print(f'исходный список\n{list}\n полученный список\n{list_new}')
