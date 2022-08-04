list = input('Введите строку из слов, разделённых пробелами: ').split()
for i, v in enumerate(list, 1):
    print(f'{i}) {v:10}')
