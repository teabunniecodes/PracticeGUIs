from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class WordleLayout(BoxLayout):
    pass

class WordleMethods():
    turns = 6

class WordleApp(App):
    # def build(self):
    #     return WordleLayout()
    pass

if __name__ == "__main__":
    WordleApp().run()