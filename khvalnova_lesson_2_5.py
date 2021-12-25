my_price = [57.8, 46.51, 97, 0.99, 14.99, 15.00, 115, 1148, 0.01]
# A) вывести на экран цены через запятую в виде __ руб __ коп.
def my_func():
    for i in my_price:
        r = int(i)
        kk = round((i - r)*100)
        a = '{} руб. {:02} коп.'.format(r, kk)
        print(a, end=', ')
my_func()

# B) вывести цены, отсортированные по возрастанию
print(id(my_price))
my_price.sort()
my_func()
print(id(my_price))

# C) создание нового списка по убыванию
new_list = [my_price.sort(reverse=True)]
my_func()
print(id(new_list))

# D) Вывести пять дорогих товаров, написав минимум кода
print(*['{} руб. {:02} коп.'.format((int(i)), (round((i - int(i))*100))) for i in sorted(my_price)[::-1][:5]],sep=', ')






