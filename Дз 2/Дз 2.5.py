my_list = [5, 4, 3, 2, 1]
while True:

    unput_num = (input('Введите цифру:\n'))
    if unput_num.isdigit():
        my_list.append(int(unput_num))
        my_list.sort(reverse=True)
        print(my_list)
    elif unput_num == 'q':
        break
