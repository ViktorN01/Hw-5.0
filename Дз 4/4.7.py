def factor(numb):
    num = 1
    for n in range(numb + 1):
        yield f'{n}! = {num}'
        num *= n + 1


for el in factor(int(input('целое число: '))):
    print(el)
