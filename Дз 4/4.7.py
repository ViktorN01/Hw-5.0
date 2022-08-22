def factorial(num):
    f_num = 1
    for n in range(num + 1):
        yield f'{n}! = {f_num}'
        f_num *= n + 1


for i in factorial(int(input('Целое число: '))):
    print(i)
