import random

class GameMethods:
    moves = ['Rock', 'Paper', 'Scissor']

    def getMove(self, button):
        self.computer = random.choice(self.moves)
        return (f"The computer played {self.computer}", self.isWin(button, self.computer))

    def isWin(self, button, opponent):
        if button == opponent:
            return "You tied!"
        elif (button == self.moves[0] and opponent == self.moves[2]) or (button == self.moves[1] and opponent == self.moves[0]) or (button == self.moves[2] and opponent == self.moves[1]):
            return "You won!"
        else:
            return "You lost :("