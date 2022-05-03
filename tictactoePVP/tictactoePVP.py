from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, BooleanProperty

class GameMethods(BoxLayout):
    buttons = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player = "X"
    turns = 0
    text = StringProperty("Tic Tac Toe!")
    bEnabled = BooleanProperty(False)
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
    def getMove(self, widget):
        x = int(widget.text) - 1
        self.turns += 1
        widget.text = self.player
        self.buttons[x] = self.player
        widget.disabled = True
        self.wins()
        
    def onPress(self, widget):
        # places an X in the space during X's turn
        if self.player == "X":
            self.getMove(widget)
            self.player = "O"
        # places an O in the space if it is a valid input when it is O's turn
        else:
            self.getMove(widget)
            self.player = "X"
 
    # defines how to win the game and checks if met
    def wins(self):
        if any(self.buttons[win[0]] == self.buttons[win[1]] == self.buttons[win[2]] for win in self.theWins):
            self.text = f"Congrats {self.player} has won!"
            self.bEnabled = True

        elif self.turns == 9:
            self.text = f"Cat's Game!"
            self.bEnabled = True

    def onReset(self):
        if self.bEnabled == True:
            self.text = "Tic Tac Toe!"
            self.bEnabled = False
            self.player = "X"
            self.turns = 0
            for i in range(1, 10):
                self.buttons[i - 1] = i
                self.ids[f"button_{i}"].text = str(i)

class TicTacToe(App):
    def build(self):
        return GameMethods()

if __name__ == "__main__":
    TicTacToe().run()
