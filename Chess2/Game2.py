from cProfile import label
from ctypes import sizeof
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

pawnBlack=[]
pawnWhite=[]
sizeBtn = 100
whichPawn = 0
for i in range(8):
    pawnBlack.append(0)
    pawnBlack[i] = Button(text='', size_hint=(None, None), font_size=40)
    pawnBlack[i].disabled = True
    pawnBlack[i].top = 200
    pawnBlack[i].x =  sizeBtn * (i)
    pawnBlack[i].background_color=(0.3,0.3,0.3,10)
    pawnBlack[i].size = [100,100]
for i in range(8):
    pawnWhite.append(0)
    pawnWhite[i] = Button(text='', size_hint=(None, None), font_size=40)
    pawnWhite[i].disabled = True
    pawnWhite[i].top = 700
    pawnWhite[i].x =  sizeBtn * (i)
    pawnWhite[i].background_color=(2,2,2,10)
    pawnWhite[i].size = [100,100]
    
class TicTacToe(App):
    def build(self):
        #for i in range(8):
        #    pawnBlack[i].bind(on_press=self.movePawnBlack)
        #    whichPawn = i
        gr = RelativeLayout(size = (200,200))
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
                gr.add_widget(btn)
                row.append(btn)
            btns.append(row)
        for i in range(8):
            gr.add_widget(pawnBlack[i])
        for i in range(8):
            gr.add_widget(pawnWhite[i])
        #pawnBlack.x=200
        
        return gr
    


TicTacToe().run()