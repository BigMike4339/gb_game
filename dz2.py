import random
import tkinter


class My_game():
    def __init__(self, max_errors=8, g_height=400, g_width=800):
        self.words_list = ['Автострада', 'Библиотека', 'Стадион', 'Консерва', \
                           'Параграф', 'Автомобиль', 'Переправа']
        self.errors_counter = 0
        self.used_letters = []
        self.secret_word = ''
        self.MAX_ERRORS = max_errors
        self.G_HEIGHT = g_height
        self.G_WIDTH = g_width

        self.need_new_game = True
        self.game_over = False

        root.title('игра')
        self.real_h, self.real_w = root.winfo_screenheight(), root.winfo_screenwidth()

        self.left_offset = (self.real_w - self.G_WIDTH) // 2
        self.top_offset = (self.real_h - self.G_HEIGHT) // 2

        root.geometry(f'{self.G_WIDTH}x{self.G_HEIGHT}+{self.left_offset}+{self.top_offset}')
        root.iconbitmap('game.ico')
        root.resizable(height=False, width=False)

        self.var_gamer_word = tkinter.StringVar()
        self.var_different_messages = tkinter.StringVar()

        # заголовок
        self.label_1 = tkinter.Label(root, text='Угадайте слово')
        self.label_1.config(font=("Courier", 16), )
        self.label_1.place(x=0, y=0)

        # отгадываемое слово
        self.label_2 = tkinter.Label(root, textvariable=self.var_gamer_word)
        self.label_2.config(font=("Courier", 28))
        self.label_2.place(x=0, y=self.G_HEIGHT // 3)

        # дополнительные сообщения
        self.label_3 = tkinter.Label(root, textvariable=self.var_different_messages)
        self.label_3.config(font=("Courier", 14))
        self.label_3.place(x=0, y=self.G_HEIGHT // 3 * 2)

        self.init_new_game()

        root.bind('<KeyPress>', self.key_press)

    def to_russian_letters2(self, char):
        # проверим введена ли русская буква и если нет, то преобразуем её в русскую
        if not 'а' <= chr(ord(char)) <= 'я':
            eng_chars = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
            rus_chars = "йцукенгшщзхъфывапролджэячсмитьбю"
            trans_table = dict(zip(eng_chars, rus_chars))
            char = trans_table.get(char)

        return char

    def make_user_word(self, arg):
        return ''.join(arg)

    def init_new_game(self):
        self.errors_counter = 0
        self.used_letters = []

        self.secret_word = random.sample(self.words_list, 1)[0].lower()
        self.user_word = ['*'] * len(self.secret_word)
        self.var_gamer_word.set(self.user_word)

        self.game_over = False

        print(self.secret_word)
        self.var_gamer_word.set(self.make_user_word(self.user_word))
        self.var_different_messages.set('Введите букву')

    def key_press(self, arg):

        letter = arg.char.lower()
        # print(ord(letter))

        if self.game_over:
            if ord(letter) == 13 or self.to_russian_letters2(letter) in ('д', 'y'):
                self.init_new_game()
                return
            elif self.to_russian_letters2(letter) in ('н', 'n'):
                root.destroy()
            else:
                different_messages = f'Не понял, уточните, играем снова? (Д/н)'
                self.var_different_messages.set(different_messages)
                return

        if len(letter) != 1 or not letter.isalpha() \
                or letter in self.used_letters:
            return

        letter = self.to_russian_letters2(letter)

        self.used_letters.append(letter)
        different_messages = f'Вы пробовали буквы: {self.used_letters}\n'
        # print(f'пробовали буквы: {self.used_letters}')

        addition_to_gamer_word = ''
        if letter in self.secret_word:
            for pos, char in enumerate(self.secret_word):
                if char == letter:
                    self.user_word[pos] = letter
            if '*' not in self.user_word:
                # self.var_gamer_word.set(self.make_user_word(self.user_word))
                addition_to_gamer_word = 'Вы выиграли!\n'
                different_messages = 'Сыграем ещё? (Д/н)'
                self.game_over = True
        else:
            self.errors_counter += 1
            different_messages += f'\nДопущено ошибок: {self.errors_counter}'
            # print(f'допущено ошибок: {self.errors_counter}')
            if self.errors_counter == self.MAX_ERRORS:
                addition_to_gamer_word = f'Допущено ошибок: {self.errors_counter}\nВы проиграли!\n'
                different_messages = 'Сыграем ещё? (Д/н)'
                self.game_over = True

        self.var_gamer_word.set(addition_to_gamer_word + self.make_user_word(self.user_word))
        self.var_different_messages.set(different_messages)


root = tkinter.Tk()
obj = My_game();
root.mainloop()
