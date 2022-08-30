from random import randint

with open("counts.txt", "w", encoding="utf-8") as file:
    list = [randint(1, 100) for _ in range(100)]
    file.write("".join(map(str, list)))

print(f'Сумма элементов списка - {sum(list)}')
