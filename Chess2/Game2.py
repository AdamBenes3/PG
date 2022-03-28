from cProfile import label
from curses import panel
from sqlite3 import Row
from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout

class TicTacToe(App):
    def build(self):
        gr = RelativeLayout(size = (200,200))
        test = Button(text='', size_hint=(None, None), font_size=40)
        test.top = 100
        test.x=0
        test.background_color=(200,200,200,1)
        test.size = [100,100]
        gr.cols = 8
        gr.rows = 8
        gr.spacing = 10
        gr.size_hint = (1, 1)
        btns = []
        #gr.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        #gr.bind(minimum_height=gr.setter('height'), minimum_width=gr.setter('width'))
        for i in range(8):
            row = []
            for j in range(8):
                btn = Button(text='', size_hint=(None, None), font_size=40)
                btn.top = 100 * j + 100
                btn.x = 100 * i
                if((i + j) % 2 == 0):
                    btn.background_color = (200,200,0,1)
                else:
                    btn.background_color = (0,200,200,1)
                btn.height = btn.width = 100
                btn.bind(on_press=self.button_press)
                gr.add_widget(btn)
                row.append(btn)
            btns.append(row)
        btns[2][1].color = [1, 1, 0, 0]
        gr.add_widget(test)
        return gr
    def button_press(self, instance):
        pass

TicTacToe().run()