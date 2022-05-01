from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty

class GameMethods(BoxLayout):
    buttons = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player = "X"
    winner = False
    text = StringProperty("Tic Tac Toe!")
    bEnabled = True
    theWins = [
        # horizantal win conditions
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        # vertical win conditions
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        
        # diagonal win conditions
        [0, 4, 8],
        [2, 4, 6]
    ]

    # gives the parameters of a turn
    def onPress(self, widget):
        # places an X in the space during X's turn
        if self.player == "X":
            self.wins()
            x = int(widget.text) - 1
            widget.text = self.player
            self.buttons[x] = self.player
            self.wins()
            self.player = "O"
            widget.disabled = True

        # places an O in the space if it is a valid input when it is O's turn
        else:
            x = int(widget.text) - 1
            widget.text = self.player
            self.buttons[x] = self.player
            self.wins()
            self.player = "X"
            widget.disabled = True

    # defines how to win the game and checks if met
    def wins(self):
        if any(self.buttons[win[0]] == self.buttons[win[1]] == self.buttons[win[2]] for win in self.theWins):
            self.text = f"Congrats {self.player} has won!"
            self.winner = True

class TicTacToe(App):
    def build(self):
        return GameMethods()

if __name__ == "__main__":
    TicTacToe().run()
