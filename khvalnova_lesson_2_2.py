my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+05', 'градусов']
new_list = []

for i in my_list:
    if i.isdigit():
        new_list.append('"{:02d}"'.format(int(i)))
    elif i.startswith('+'):
        new_list.append('"{}{:02d}"'.format(i[0], int(i)))
    elif i.startswith('-'):
        new_list.append('"{}{:02d}"'.format(i[0], int(i[1])))
    else: new_list.append(i)

print(' '.join(new_list))
