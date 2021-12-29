import random
nouns =['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']
new_list_1 = []

def get_jokes(n, flag = False):
    for word in range(n):
        random_str_nouns = random.choice(nouns)
        random_str_adverbs = random.choice(adverbs)
        random_str_adjectives = random.choice(adjectives)
        joke = f'{random_str_nouns} {random_str_adverbs} {random_str_adjectives}'
        print(joke)
        if flag == True:
            new_list_1 = joke.split()
            for str_nouns in nouns:
                for str_fun in new_list_1:
                    if str_nouns == str_fun:
                        nouns.remove(str_nouns)
            for str_adverbs in adverbs:
                for str_fun in new_list_1:
                    if str_adverbs == str_fun:
                        adverbs.remove(str_adverbs)
            for str_adjectives in adjectives:
                for str_fun in new_list_1:
                    if str_adjectives == str_fun:
                        adjectives.remove(str_adjectives)

get_jokes(3, flag=True)

