month_list = [['Зима', 12, 1, 2], ['Весна', 3, 4, 5], ['Лето', 6, 7, 8], ['Осень', 9, 10, 11]]

month_num = int(input('Введите порядковый номер месяца в году: '))
if month_num in range(1, 13):
    for i, el in enumerate(month_list):
        if month_num in el[1:4]:
            print(f'Введенный номер месяца относится к сезону {el[0]}')
            break

