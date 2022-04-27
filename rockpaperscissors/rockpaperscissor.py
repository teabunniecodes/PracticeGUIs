from rps_layout import GameLayout

from kivy.app import App

class RockPaperScissors(App):
    def build(self):
        return GameLayout()

if __name__ == "__main__":
    RockPaperScissors().run()
