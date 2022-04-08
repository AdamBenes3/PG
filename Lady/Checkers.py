from random import choice
from tkinter import MOVETO
from turtle import *
from freegames import vector, floor, square

tiles = []
width = 800
height = 800

figuresRed = []
figuresBlue = []
figureDrawer = Turtle(visible=False)
moving = None
redOnmove = False

def getCornetoIndex(index):
    x = index%8
    y = floor(index, 8)/8
    return x, y


def deployment():
    global width, height
    size = width/8
    for x in range(len(tiles)):
        for y in range(len(tiles[0])):
            if tiles[x][y] == "black" and y<3:
                figuresRed.append(vector(x,y))
            elif tiles[x][y] == "black" and y>4:
                figuresBlue.append(vector(x,y))
    drawFigures()

def drawFigures():
    size = width/8
    figureDrawer.clear()
    for fig in figuresRed:
        figureDrawer.penup()
        figureDrawer.goto(fig.x*size-width/2 + size/2,height/2 - fig.y*size - size)
        figureDrawer.pendown()
        figureDrawer.begin_fill()
        figureDrawer.fillcolor("red")
        figureDrawer.circle(size/2)
        figureDrawer.end_fill()
    for fig in figuresBlue:
        figureDrawer.penup()
        figureDrawer.goto(fig.x*size-width/2 + size/2,height/2 - fig.y*size - size)
        figureDrawer.pendown()
        figureDrawer.begin_fill()
        figureDrawer.fillcolor("blue")
        figureDrawer.circle(size/2)
        figureDrawer.end_fill()
    if moving != None:
        figureDrawer.penup()
        figureDrawer.goto(moving.x*size-width/2 + size/2,height/2 - moving.y*size - size)
        figureDrawer.pendown()
        figureDrawer.begin_fill()
        figureDrawer.fillcolor("pink")
        figureDrawer.circle(size/2)
        figureDrawer.end_fill()        
       
def click(x,y):
    global moving, redOnmove
    x = floor(x + width/2, width/8) / (width/8)
    y = floor(height/2 - y, height/8) / (width/8)
    if moving == None:
        if redOnmove:
            if vector(x,y) in figuresRed:
                moving = vector(x,y)
        else:
            if vector(x,y) in figuresBlue:
                moving = vector(x,y)
    else:
        if moving == vector(x,y):
            moving = None
        elif isPlayabel(moving, vector(x,y)):
            if redOnmove:
                figuresRed.remove(moving)
                figuresRed.append(vector(x,y))
            else:
                figuresBlue.remove(moving)
                figuresBlue.append(vector(x,y))
            moving = None
            redOnmove = not redOnmove
    drawFigures()

def isPlayabel(moving, target):
    global redOnmove
    if not isEmpty(target):
        return False
    print(moving, target, redOnmove)
    if target.x>7 or target.x<0 or target.y>7 or target.y<0:
        return False
    if redOnmove:
        if target.y -1 != moving.y:
            return False
        if target.x-1 != moving.x and target.x+1 != moving.x:
            return False
    else:
        if target.y+1 != moving.y:
            return False
        if target.x-1 != moving.x and target.x+1 != moving.x:
            return False
    return True
        

def isEmpty(target):
    print(figuresRed, figuresBlue)
    if target in figuresRed or target in figuresBlue:
        print("not empty")
        return False
    else:
        return True


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

def drawChessboard():
    global width, height
    size = width/8
    for x in range(len(tiles)):
        for y in range(len(tiles[0])):
            square(x*size-width/2,height/2 - y*size - size, size,tiles[x][y])


setup(width, height, 370, 100)
tracer(False)
chessboard()
listen()
onscreenclick(lambda x,y: click(x,y),1)
drawChessboard()
deployment()


done()