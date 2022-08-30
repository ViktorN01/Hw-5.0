with open('counts', 'w', encoding='utf-8') as name:
    while True:
        line = input('Введите ваши данные ')
        if not line:
            break

        print(line, file=name)
