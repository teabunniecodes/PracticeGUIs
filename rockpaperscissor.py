import random

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

moves = ['r', 'p', 's']
x = 0

class GameLayout(Widget):
    text = StringProperty("Rock Paper Scissors")
    text2 = StringProperty("Choose a move")
    text3 = StringProperty("")

    def setRock(self):
        self.user = 'r'
        self.getMove()
        self.text = "You chose Rock"

    def setPaper(self):
        self.user = 'p'
        self.getMove()
        self.text = "You chose Paper"

    def setScissor(self):
        self.user = 's'
        self.getMove()
        self.text = "You chose Scissor"

    def getMove(self):
        while True:
            if self.user in moves:
                self.computer = random.choice(moves)
                self.text2 = f"The computer played {self.computer}"
                self.isWin(self.computer)
                break

    def isWin(self, opponent):
        if self.user == opponent:
            self.text3 = "You tied!"
        elif (self.user == moves[0] and opponent == moves[2]) or (self.user == moves[1] and opponent == moves[0]) or (self.user == moves[2] and opponent == moves[1]):
            self.text3 = "You won!"
        else:
            self.text3 = "You lost :("

class RockPaperScissors(App):
    def build(self):
        # self.game = GameMethods()
        return GameLayout()

if __name__ == "__main__":
    RockPaperScissors().run()
