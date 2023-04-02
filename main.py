import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line

class DrawWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 1, 0)
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=5)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class Shamsiyat(App):

    def build(self):
        return DrawWidget()


if __name__ == '__main__':
    Shamsiyat().run()
