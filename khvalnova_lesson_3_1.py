number = str(input('Введите числительное на английском: '))

def english_number():
    for key in my_dict.keys():
        if number == key:
            print(my_dict.get(key))

my_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

english_number()