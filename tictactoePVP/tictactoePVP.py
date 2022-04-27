from tttPVP_layout import GameLayout

from kivy.app import App

class TicTacToePVP(App):
    def build(self):
        return GameLayout()

if __name__ == "__main__":
    TicTacToePVP().run()
