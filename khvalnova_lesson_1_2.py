# my_list = list(range(1, 1001)) - список от 1 до 1000
cubes = [i**3 for i in list(range(1, 1001)) if i % 2 != 0] #список кубов нечетных чисел

final_sum = 0
for num in cubes:                          # для каждого числа в списке,сотоящим из кубов
    sum_dig = 0                            # назначаем счетчик для суммы цифр числа (0+28)
    for digit in str(num):                 # для каждой цифры в строке числа:
        sum_dig += int(digit)              # прибавляем в счетчик СУММУ ЦИФР (напр: 6+8+5+9 = 28)
        if sum_dig % 7 == 0:               # и если сумма в счетчике делится на 7 то (28/7)
            final_sum += num               # прибавляем к финальной сумме. (0 + 6859)
print(final_sum)

final_sum = 0
for num in cubes:
    num += 17
    sum_dig = 0
    for digit in str(num):
        sum_dig += int(digit)
        if sum_dig % 7 == 0:
            final_sum += num
print(final_sum)

# Итого получились два числа;  144843716016 ;  147316505772 ;
