from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.metrics import dp
import string, random

class WordleLayout(BoxLayout):
    turns = 0
    alphabet = list(string.ascii_uppercase)
    is_playing = True
    play_answer = True
    won_or_lost = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_word(self):
        # gets a random word from a text document
        with open("wordle\words.txt") as words:
            self.words = words.read()
            # create a list of the words
            self.words = self.words.strip().split("\n")
            # randomly chooses a word from the list
            self.chosen_word = random.choice(self.words).upper()
    
    def check_dictionary(self):
        with open("wordle\dictionary.txt") as dictionary:
            self.dictionary = dictionary.read()
            #create a list of words from the dictionary
            self.dictionary = self.dictionary.strip().split("\n")
    
    def user_guess(self, widget):
        self.guess = (self.ids["text_input_guess"].text).upper()
        self.get_word()
        self.check_dictionary()
        self.check_guess()
        self.input_guess()

    def input_guess(self):
        # this will place the letters in the boxes
        if self.turns < 6:
            for x in range(len(self.guess)):
                self.ids[f"Guess{self.turns}Letter{x+1}"].text = self.guess[x]
            self.ids["text_input_guess"].text = ""
    
    def check_guess(self):
        if self.guess.lower() in self.dictionary or self.guess.lower() in self.words:
                # self.is_win()
                # self.color_guess()
                # self.display_alphabet()
                self.turns += 1
        elif self.guess.isalpha():
            if len(self.guess) < 5:
                self.ids["label"].text = "The word is to short!"
                self.ids["text_input_guess"].text = ""
            elif len(self.guess) > 5:
                self.ids["label"].text = "The word is to long!"
                self.ids["text_input_guess"].text = ""
            elif len(self.guess) == 5:
                self.ids["label"].text = "Stop making up words >:O"
                self.ids["text_input_guess"].text = ""
        else:
            print("Not a valid word -_-")

class WordleApp(App):
    def build(self):
        return WordleLayout()

if __name__ == "__main__":
    WordleApp().run()