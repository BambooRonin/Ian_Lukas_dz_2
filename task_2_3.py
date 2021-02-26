raw_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for ind, item in enumerate(raw_list):  # идем по списку
    if item.isdigit() and int(item) < 10:  # преобразовываем элемент, состоящий из цифры < 10
        raw_list.pop(ind)
        raw_list.insert(ind, '"' + '0' + item + '"')
    elif item.isdigit():  # то же но с числами > 10
        raw_list.pop(ind)
        raw_list.insert(ind, '"' + item + '"')
    elif item.startswith('+') and int(item) < 10:  # то же но с элементом, сожержащим "+"
        raw_list.insert(ind + 1, int(item))
        raw_list.insert(ind, '"' + '+0' + str(raw_list[ind + 1]) + '"')
        raw_list.pop(ind + 1)
        raw_list.pop(ind + 1)
print(" ".join(map(str, raw_list)))  # сливаем в единую строку
