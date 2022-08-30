with open('5.2.txt', encoding='utf-8') as file:
    crash = file.readlines()
    for index, value in enumerate(crash, 1):
        numbers_words = len(value.split())
        print(f"Строка {index} содержит {numbers_words} слов")
