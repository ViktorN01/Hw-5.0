dict = {"one": "один", "two": "два", "three": "три", "four": "четыре"}

with open('5.4.txt', 'w', encoding='utf-8') as new:
    with open('5.4.txt', encoding='utf-8') as my:
        new.writelines([line.replace(line.split()[0], dict.get(line.split()[0])) for line in my])
