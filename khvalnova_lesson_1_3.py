for number in range(100):
    my_list = list(str(number + 1))
    if int(my_list[-1]) % 10 == 1 and number + 1 != 11:
        print(str(number + 1) + ' процент')
    elif int(my_list[-1]) >1 and int(my_list[-1]) <= 4:
        if number + 1 > 10 and number + 1 <= 14:
            print(str(number + 1) + ' процентов')
        else:
            print(str(number + 1) + ' процента')
    else:
        print(str(number + 1) + ' процентов')