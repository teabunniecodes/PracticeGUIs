from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class GameFunction(BoxLayout):
    space_1 = StringProperty("1")
    space_2 = StringProperty("2")
    space_3 = StringProperty("3")
    space_4 = StringProperty("4")
    space_5 = StringProperty("5")
    space_6 = StringProperty("6")
    space_7 = StringProperty("7")
    space_8 = StringProperty("8")
    space_9 = StringProperty("9")
    pass

class GameLayout(BoxLayout):
    pass

class TicTacToe(App):
    def build(self):
        return GameLayout()

if __name__ == "__main__":
    TicTacToe().run()
