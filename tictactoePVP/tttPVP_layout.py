from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class GameLayout(Widget):
    text1 = StringProperty("Tic Tac Toe!")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = ""
        
    def random(self):
        user = 'X'
        self.text1 = user