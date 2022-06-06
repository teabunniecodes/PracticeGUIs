from kivy.app import App
from kivy.graphics import BorderImage, Color, Line
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex

spacing = 10

def all_cells():
    for x in range(5):
        for y in range(6):
            yield (x, y)

class Board(Widget):
    b = None

    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)
        self.resize()

    def reset(self):
        self.b = [[None for i in range(5)] 
            for j in range(6)]

    def resize(self, *args):
        self.cell_size = (.2 * (self.height - 6 * spacing), ) * 2
        self.canvas.before.clear()
        with self.canvas.before:
            BorderImage(pos = self.pos, 
                size = self.size, 
                source = 'board.png')
            Color(*get_color_from_hex('#262626'))
            for pos_x, pos_y in all_cells():
                BorderImage(pos = self.cell_pos(pos_x, pos_y), 
                    size = self.cell_size, 
                    source = 'cell.png')

    on_pos = resize
    on_size = resize

    def cell_pos(self, pos_x, pos_y):
        return (self.x + pos_x * 
            (self.cell_size[0] + spacing) + spacing, 
            self.y + pos_y * 
            (self.cell_size[1] + spacing) + spacing)

class WordleApp(App):
    def on_start(self):
        # board = self.root.ids.board
        # board.reset()
        return Board()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = get_color_from_hex('#FFFFFF')

    WordleApp().run()