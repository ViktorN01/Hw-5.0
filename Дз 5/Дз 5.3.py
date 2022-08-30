with open('5.3', 'r', encoding='utf-8') as f:
    employees = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f' средний показатель = {round(sum(employees.values()) / len(employees), 3)}\n'
          f' показатель 20тыс {[n[0] for n in employees.items() if n[1 < 20000]]}')
