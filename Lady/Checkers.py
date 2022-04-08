from random import choice
from tkinter import MOVETO
from turtle import *
from freegames import vector, floor, square

tiles = []
width = 800
height = 800

figuresRed = []
figuresBlue = []

def getCornetoIndex(index):
    x = index%8
    y = floor(index, 8)/8
    return x, y

def move(figure, x, y):
    global figuresRed, figuresBlue
    if figure in figuresRed:
        figuresRed.remove(figure)
    elif figure in figuresBlue:
        figuresBlue.remove(figure)
    figure.move(x,y)
    if figure in figuresRed:
        figuresRed.append(figure)
    elif figure in figuresBlue:
        figuresBlue.append(figure)
        
def check(figure, x, y):
    global figuresRed, figuresBlue
    if figure in figuresRed:
        figuresRed.remove(figure)
    elif figure in figuresBlue:
        figuresBlue.remove(figure)
    figure.move(x,y)
    if figure in figuresRed:
        figuresRed.append(figure)
    elif figure in figuresBlue:
        figuresBlue.append(figure)


def deployment():
    global width, height
    size = width/8
    for x in range(len(tiles)):
        for y in range(len(tiles[0])):
            if tiles[x][y] == "black" and y<3:
                drawFigure(x,y,"red")
                figuresRed.append(vector(x,y))
            elif tiles[x][y] == "black" and y>4:
                drawFigure(x,y,"blue")
                figuresBlue.append(vector(x,y))

def drawFigure(x,y,color):
    size = width/8
    penup()
    goto(x*size-width/2 + size/2,height/2 - y*size - size)
    pendown()
    begin_fill()
    fillcolor(color)
    circle(size/2)
    end_fill()

def chessboard():
    global height, width
    tiles.clear()
    for x in range(8):
        row = []
        for y in range(8):
            if (x + y) % 2 == 0:
                row.append("white")
            else:
                row.append("black")
        tiles.append(row)

def draw():
    global width, height
    size = width/8
    for x in range(len(tiles)):
        for y in range(len(tiles[0])):
            square(x*size-width/2,height/2 - y*size - size, size,tiles[x][y])


setup(width, height, 370, 100)
tracer(False)
chessboard()
listen()
draw()
deployment()
drawPawns()


done()