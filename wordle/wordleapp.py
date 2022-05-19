from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty

class WordleLayout(BoxLayout):
    pass

class WordleApp(App):
    def build(self):
        return WordleLayout()

if __name__ == "__main__":
    WordleApp().run()