from rps_methods import GameMethods

from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class GameLayout(Widget):
    text = StringProperty("Rock Paper Scissors")
    text2 = StringProperty("Choose a move")
    text3 = StringProperty("")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.methods = GameMethods()

    def setRock(self):
        user = 'Rock'
        self.text2, self.text3 = self.methods.getMove(user)
        self.text = "You chose Rock"

    def setPaper(self):
        user = 'Paper'
        self.text2, self.text3 = self.methods.getMove(user)
        self.text = "You chose Paper"

    def setScissor(self):
        user = 'Scissor'
        self.text2, self.text3 = self.methods.getMove(user)
        self.text = "You chose Scissor"