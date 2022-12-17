import random

themes = {
    'фрукты': ['яблоко', 'абрикос', 'авокадо', 'ананас', 'банан', 'бергамот', 'дыня', 'грейпфрут', 'киви', 'лайм'],
    'овощи': ['морковь', 'лук', 'перец', 'чеснок', 'картофель', 'фенхель', 'латук', 'капуста', 'свекла', 'батат',
              'кукуруза'],
    'одежда': ['кроссовки', 'ботинки', 'пальто', 'платье', 'пиджак', 'джинсы', 'рубашка', 'туфли', 'юбка', 'костюм'],
    'кухня': ['нож', 'вилка', 'ложка', 'сотейник', 'сковорода', 'кастрюля', 'венчик', 'половник', 'тёрка',
              'ступа'],
    'пк': ['озу', 'видеокарта', 'процессор', 'куллер', 'ссд', 'монитор', 'колонки', 'мышь', 'клавиатура',
           'камера'
           ]}

line_sep = '\n*_*_*_*_*_*_*_*_*_*_*_*\n'
print(line_sep)
print('Приветствую в игре "Виселица"')
print('Выбери тему, на которую будет загадано слово!')
print('Темы: Фрукты, Овощи, Одежда, Кухня, ПК')
print(line_sep)


# Выбор темы для слова и вывод рандомного слова
def choose_theme(user_input):
    for key, value in themes.items():
        if key == user_input:
            sec = get_random_word(value)
            print(line_sep, 'Длинна слова', len(sec), 'букв')
            print(f' у вас {len(sec * 2)} попыток', line_sep)
            return sec


# Выбираем рандом слово из выбраной темы
def get_random_word(word_list):
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]


# Проверяем ввод на соответствие условию
def check_latter(sec):
    while True:
        print('Введите букву', end=' ')
        gus = str(input().lower())
        if len(gus) != 1:
            print('Вы ввели больше одной буквы')
        elif gus in '1234567890!@#$%^&*(),."[]{}|/ ':
            print('Введите букву кирилицы')
        elif gus not in 'ёйцукенгшщзхъфывапролджэячсмитьбю':
            print('Введите букву кириллицы')
        elif gus in sec:
            print('Вы уже пробовали эту букву!')
        else:
            return gus


# Проверка ввода на соответствие заданым темам
def check_user_input():
    while True:
        print('Введите тему:', end=' ')
        ui = str(input().lower())
        if ui in '1234567890!@#$%^&*(),."[]{}|/ ':
            print('Введите слово на кириллице')
        elif ui not in themes.keys():
            print('Таких тем у нас нет!')
        else:
            return ui


secret = choose_theme(user_input=check_user_input())
attempt = len(secret * 2)
star = '_' * len(secret)
miss_letter = ''
correct_letter = ''

while True:
    # производим замену символов на угаданые буквы
    for k in range(len(secret)):
        if secret[k] in correct_letter:
            star = star[:k] + secret[k] + star[k + 1:]

    for letter in star:
        print(letter, end='')
    print()

    # инициализируем проверку ввода букв
    guess = check_latter(miss_letter + correct_letter)

    # Проверка на условие победы, если нет, отнимаем попытку
    if guess in secret:
        correct_letter = correct_letter + guess
    else:
        attempt -= 1
    found_all_letters = True

    for i in range(len(secret)):
        if secret[i] not in correct_letter:
            print(f'осталось {attempt} попыток!')
            found_all_letters = False
            break

    # Условие победы
    if found_all_letters:
        print(line_sep)
        print(f'Превосходно! загаданое слово "{secret}" Вы победили!')
        print(line_sep)
        break
    else:
        miss_letter = miss_letter + guess

    # Условие поражения
    if len(miss_letter) == len(secret * 2):
        print(line_sep)
        print(f'У вас не осталось попыток после {str(len(miss_letter))} ошибок!\n '
              f'и {str(len(correct_letter))} угаданых букв. Загадное слово:'
              f' {secret}')
        print(line_sep)
        break