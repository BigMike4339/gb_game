import random

MAX_ERRORS = 8

words_list = ['Автострада', 'Библиотека', 'Стадион', 'Консерва', \
              'Параграф', 'Автомобиль', 'Переправа']

# === мои функции =========
def russian_letters(char):
    # проверим введена ли русская буква
    ret = False
    if 'а' <= chr(ord(char)) <= 'я':
        ret = True

    return ret


def to_russian_letters2(char):
    # проверим введена ли русская буква и если нет, то преобразуем её в русскую
    if not 'а' <= chr(ord(char)) <= 'я':
        eng_chars = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
        rus_chars = "йцукенгшщзхъфывапролджэячсмитьбю"
        trans_table = dict(zip(eng_chars, rus_chars))
        char = trans_table.get(char)

    return char

# === мои функции закончились =========


def show_user_word(arg):
    print(''.join(arg))


# добавил ещё один цикл для реализации повтора игры
while True:
    errors_counter = 0
    used_letters = []

    # добавил перевод в нижний регистр для списка слов: ошибаются все :)
    secret_word = random.sample(words_list, 1)[0].lower()
    user_word = ['*'] * len(secret_word)

    print(secret_word)

    show_user_word(user_word)

    while True:
        # добавил перевод в нижний регистр
        letter = input('введите букву: ').lower()

        # ВАРИАНТ 1: добавил проверку на русские символы
        # if len(letter) != 1 or not letter.isalpha()\
        #         or letter in used_letters or not russian_letters(letter):
        #     continue

        # ВАРИАНТ 2: изменяем латинский символ на русский
        if len(letter) != 1 or not letter.isalpha() \
                or letter in used_letters:
            continue
        letter = to_russian_letters2(letter)

        used_letters.append(letter)
        # print(ord(letter))
        print(f'пробовали буквы: {used_letters}')

        if letter in secret_word:
            for pos, char in enumerate(secret_word):
                if char == letter:
                    user_word[pos] = letter
            if '*' not in user_word:
                print('вы выиграли ;)')
                break
        else:
            errors_counter += 1
            # errors_counter = errors_counter + 1
            print(f'допущено ошибок: { errors_counter }')
            if errors_counter == MAX_ERRORS:
                print('вы проиграли')
                break
        show_user_word(user_word)

    ques = input('Играем ещё? (Д/н): ').lower()
    if len(ques) !=0 and to_russian_letters2(ques) in ('н', 'n'):
        break


print('пока пока')
