my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']
for position in my_list:
    name = position.split()
    print('Привет,{}!'.format(name[-1].lower().title()))