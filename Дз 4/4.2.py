list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list = [j for i, j in zip(list, list[1:]) if j > i]
print(my_list)
