dict = {'Зима': (1, 2, 12),
       'Весна': (3, 4, 5),
       'Лето': (6, 7, 8),
       'Осень': (9, 10, 11)}

month = int(input('Выберите месяц: '))
for key in dict.keys():
   if month in dict[key]:
       print(key)
