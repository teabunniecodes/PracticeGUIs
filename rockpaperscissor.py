import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import random

moves = ['r', 'p', 's']
x = 0

class GameLayout(Widget):
    def setRock(self):
        self.user = "r"
        print(self.user)

    def setPaper(self):
        self.user = "p"
        print(self.user)

    def setScissor(self):
        self.user = "s"
        print(self.user)
        
    def getMove(self):
        while True:
            if self.user in moves:
                computer = random.choice(moves)
                print(f"The computer played {computer}")
                self.is_win(self.user, computer)
                break
            else:
                print("Thats not a valid choice!!!! >:O Stop trying to cheat!!!")

    def is_win(player, opponent):
        if player == opponent:
            print("You tied!")
        elif (player == moves[x] and opponent == moves[x-1]):
            print("You won!")
        else:
            print("You lost :(")


class RockPaperScissors(App):
    def build(self):
        return GameLayout()

if __name__ == "__main__":
    RockPaperScissors().run()