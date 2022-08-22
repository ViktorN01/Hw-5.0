from sys import argv


def salary():
    try:
        time, rateph, bonus = map(float, argv[1:])
        print(f'salary - {time * rateph + bonus}')
    except ValueError:
        print("Введите ваши данные ")


salary()
