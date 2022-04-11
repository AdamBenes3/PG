from random import choice
from tkinter import MOVETO
from turtle import *
from freegames import vector, floor, square
from requests import options

tiles = []
width = 800
height = 800

figuresRed = []
figuresBlue = []
figureDrawer = Turtle(visible=False)
moving = None
redOnmove = False
options = []
thisFigureJump = -1

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
        figureDrawer.goto(fig.x*size-width/2 + size/2, height/2 - fig.y*size - size)
        figureDrawer.pendown()
        figureDrawer.begin_fill()
        figureDrawer.fillcolor("red")
        figureDrawer.circle(size/2)
        figureDrawer.end_fill()
    for fig in figuresBlue:
        figureDrawer.penup()
        figureDrawer.goto(fig.x*size-width/2 + size/2, height/2 - fig.y*size - size)
        figureDrawer.pendown()
        figureDrawer.begin_fill()
        figureDrawer.fillcolor("blue")
        figureDrawer.circle(size/2)
        figureDrawer.end_fill()
    if moving != None:
        figureDrawer.penup()
        figureDrawer.goto(moving.x*size-width/2 + size/2, height/2 - moving.y*size - size)
        figureDrawer.pendown()
        figureDrawer.begin_fill()
        figureDrawer.fillcolor("grey")
        figureDrawer.circle(size/2)
        figureDrawer.end_fill()   
    for option in options:
        figureDrawer.penup()
        figureDrawer.goto(option.x*size-width/2 + size/2, height/2 - option.y*size - size)
        figureDrawer.pendown()
        figureDrawer.begin_fill()
        figureDrawer.fillcolor("white")
        figureDrawer.circle(size/2)
        figureDrawer.end_fill()      
       
def click(x,y):
    global moving, redOnmove, options, thisFigureJump
    x = floor(x + width/2, width/8) / (width/8)
    y = floor(height/2 - y, height/8) / (width/8)
    if moving == None: #and thisFigureJump == -1:
        if redOnmove:
            if vector(x,y) in figuresRed:
                moving = vector(x,y)
                createOptions(moving)
        else:
            if vector(x,y) in figuresBlue:
                moving = vector(x,y)
                createOptions(moving)
    else:
        if moving == vector(x,y):
            moving = None
            thisFigureJump = -1
        elif isPlayabel(moving, vector(x,y)):
            if redOnmove:
                figuresRed.remove(moving)
                figuresRed.append(vector(x,y))
                thisFigureJump = vector(x,y)
                #last = moving
                #for row in range(moving.y+1,y,2):
                #    pass
            else:
                figuresBlue.remove(moving)
                figuresBlue.append(vector(x,y))
                thisFigureJump = vector(x,y)
            moving = None
            redOnmove = not redOnmove
        options = []
    drawFigures()
    
def createOptions(moving):
    global options, redOnmove, thisFigureJump
    options = []
    jumpOptions = []
    if(not redOnmove):
        if isEmpty(vector(moving.x + 1, moving.y - 1)):
            options.append(vector(moving.x + 1, moving.y - 1))
        if isEmpty(vector(moving.x - 1, moving.y - 1)):
            options.append(vector(moving.x - 1, moving.y - 1))
        #if thisFigureJump != -1:
        jumpOptions.append(canJump(moving))
        for jump in jumpOptions:
            options.append(jump)
        print(options)
    else:
        if isEmpty(vector(moving.x + 1, moving.y + 1)):
            options.append(vector(moving.x + 1, moving.y + 1))
        if isEmpty(vector(moving.x - 1, moving.y + 1)):
            options.append(vector(moving.x - 1, moving.y + 1))
        jumpOptions = canJump(moving)
        while len(jumpOptions) > 0:
            help = []
            for jump in jumpOptions:
                options.append(jump)
                for jump2 in canJump(jump):
                    help.append(jump2)
            jumpOptions = help
    thisFigureJump = -1
    
def isPlayabel(moving, target):
    global redOnmove, options
    return target in options

def canJump(moving):
    global redOnMove
    jumpOptions = []
    if(not redOnmove):
        if isEmpty(vector(moving.x + 2, moving.y - 2)) and vector(moving.x + 1, moving.y - 1) in figuresRed:
            jumpOptions.append(vector(moving.x + 2, moving.y - 2))
        if isEmpty(vector(moving.x - 2, moving.y - 2)) and vector(moving.x - 1, moving.y - 1) in figuresRed:
            jumpOptions.append(vector(moving.x - 2, moving.y - 2))
        print(jumpOptions)
    else:
        if isEmpty(vector(moving.x + 2, moving.y + 2)) and vector(moving.x + 1, moving.y + 1) in figuresBlue:
            jumpOptions.append(vector(moving.x + 2, moving.y + 2))
        if isEmpty(vector(moving.x - 2, moving.y + 2)) and vector(moving.x - 1, moving.y + 1) in figuresBlue:
            jumpOptions.append(vector(moving.x - 2, moving.y + 2))
    return jumpOptions

def removeFigure(x, y):
    if(vector(x, y)) in figuresBlue:
        figuresBlue.remove(vector(x, y))
    elif(vector(x, y)) in figuresRed:
        figuresRed.remove(vector(x, y))
    drawFigures

def isEmpty(target):
    if target.x < 0 or target.y < 0 or target.x > 7 or target.y > 7:
        return False
    if target in figuresRed or target in figuresBlue:
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