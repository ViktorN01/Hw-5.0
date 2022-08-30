dict = {}
numbers = "1234567890"
with open("lessons", "r", encoding='utf-8') as lessons:
    for line in lessons:
        head, hours = line.split(":")
        dict[head] = sum(map(int, "".join([num for num in hours if num in numbers]).split()))
print(dict)
