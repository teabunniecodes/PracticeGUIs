import string, random
from kivy.app import App
from kivy.graphics import BorderImage, Color, Line
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.core.window import Keyboard
from kivy.properties import NumericProperty, ListProperty, StringProperty

spacing = 10
alphabet = list(string.ascii_uppercase)
guess = ''
BOARD_WIDTH = 5
BOARD_HEIGHT = 6

# TODO replace magic numbers (AKA 5, 6 with constant variables (Board Height, Width, turns))

def all_cells():
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            yield (x, y)

# upload dictionary and list of words one time in beginning on start
# gets a random word from a text document
with open("wordle\words.txt") as words:
    words = words.read()
    # create a list of the words
    words = words.strip().split("\n")
    chosen_word = ''

with open("wordle\dictionary.txt") as dictionary:
    dictionary = dictionary.read()
    #create a list of words from the dictionary
    dictionary = dictionary.strip().split("\n")

class Tile(Widget):
    font_size = NumericProperty(24)
    color = ListProperty(get_color_from_hex('#ffffff'))
    letter_guess = StringProperty('')

    def __init__(self, letter_guess = '', **kwargs):
        super().__init__(**kwargs)
        self.font_size = 0.5 * self.width

class GameLogic:
    def __init__(self):
        self.chosen_word = self.choose_word()
        print(self.chosen_word)
    # chooses the word for the 
    def choose_word(self):
        # randomly chooses a word from the list
        return random.choice(words).upper()

    # set up win and lose parameters
    def is_win(self, guess):
        if guess == self.chosen_word:
            print("You Won!")
            # self.won_or_lost = True
            # self.is_playing = False
    def is_lose(self):
        if self.row == 0: #and not self.won_or_lost:
            print("You Lost :(")
            print(f"The word was {self.chosen_word.upper()}")
            # self.won_or_lost = True
            # self.is_playing = False
    # set up play again function


class GameText(Label):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    game_text = StringProperty('')

class Board(Widget):
    b = None
    logic = GameLogic()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.row = 5
        self.col = 0
        self.user_guess = []
        self.resize()

    def reset(self):
        self.b = [[None for i in range(5)] 
            for j in range(6)]

    def resize(self, *args):
        self.cell_size = (.167 * (self.height - 7 * spacing), ) * 2
        self.canvas.before.clear()
        with self.canvas.before:
            BorderImage(pos = self.pos, 
                size = self.size, 
                source = 'board.png')
            Color(*get_color_from_hex('#262626'))
            for pos_x, pos_y in all_cells():
                BorderImage(pos = self.cell_pos(pos_x, pos_y), 
                    size = self.cell_size, 
                    source = 'cell.png')

    on_pos = resize
    on_size = resize

    def cell_pos(self, pos_x, pos_y):
        return (self.x + pos_x * 
            (self.cell_size[0] + spacing) + spacing, 
            self.y + pos_y * 
            (self.cell_size[1] + spacing) + spacing)

    def letter_input(self, key_input, *args):
        letter_tile = Tile(pos = self.cell_pos(self.col, self.row),
            size = self.cell_size)
        letter_tile.letter_guess = key_input
        if self.col < 5:
            self.user_guess.append(letter_tile.letter_guess)
            self.b[self.row][self.col] = letter_tile
            self.col += 1
            self.add_widget(letter_tile)
        else:
            pass

    def color_guess(self, guess):
        guess_letter = list(guess)
        chosen_letters = list(self.logic.chosen_word)
        # first loops through to check the letters in the correct spot
        for x, letter in enumerate(guess):
            if guess_letter[x] == chosen_letters[x]:
                chosen_letters[x] = "*"
                color_tile = Tile(pos = self.cell_pos(x, self.row),
                                    size = self.cell_size, 
                                    color = get_color_from_hex('#50C878'))
                color_tile.letter_guess = guess_letter[x]
                self.b[self.row][x] = color_tile
                self.add_widget(color_tile)

        # then loops through to check if remaining letters are in the word
        for x, letter in enumerate(guess):
            if letter in chosen_letters:
                # need to replace at the index of the letter
                chosen_letters[chosen_letters.index(letter)] = "*"
                color_tile = Tile(pos = self.cell_pos(x, self.row),
                                    size = self.cell_size, 
                                    color = get_color_from_hex('#FFC300'))
                color_tile.letter_guess = guess_letter[x]
                self.b[self.row][x] = color_tile
                self.add_widget(color_tile)

    def letter_del(self, *args):
        # if I delete a letter I nee to self.col -= 1 and remove the cell
        self.user_guess.pop()
        self.col -= 1
        self.remove_widget(self.b[self.row][self.col])

    def word_submit(self):
        guess = "".join(self.user_guess)
        # when I hit enter to submit a word (only when at the end of a column) set self.col = 0 and self.row -= 1
        if self.col == 5 and (guess.lower() in dictionary or guess.lower() in words):
            self.color_guess(guess)
            self.row -= 1
            self.col = 0
            self.logic.is_win(guess)
            self.user_guess.clear()
        elif self.col == 5 and (guess.lower() not in dictionary or guess.lower() in words):
            self.parent.ids.game_text.game_text = 'Not A Word >:O'
            self.user_guess.clear()
            # need to figure out how to delete all the widgets in the row
            for x in range(self.col):
                self.remove_widget(self.b[self.row][x])
                self.col = 0 
        else:
            # if enter hit before 5 letters submitted then yells at the player :D
            self.parent.ids.game_text.game_text = 'Word not long enough'
            pass
    
    def on_key_down(self, window, key, *args):
        if chr(key).upper() in alphabet:
            self.letter_input(chr(key).upper())
        elif key == 8 and self.col != 0:
            self.letter_del()
        if key == 13:
            self.word_submit()
    # tip: do one thing per function: ie: on key down you switch between your actions, the letter concatenate leave for other part of code (aka leave logic for another method)

            # as letters are inputted they are added to a list to become a string to check against the dictionary and chosen word

# TODO
# set colors in a list to change the color of the labels (green, yellow)
# decide if I want to display alphabet with letters chosen colored

class WordleApp(App):
    def on_start(self):
        board = self.root.ids.board
        board.reset()
        Window.bind(on_key_down = board.on_key_down)


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = get_color_from_hex('#262626')

    WordleApp().run()
    # App.get_running_app()