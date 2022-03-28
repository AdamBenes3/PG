from random import randrange
from turtle import *
from freegames import vector, square

food = vector(0, 0)
poisons = [vector(100,0)]
snake = [vector(10, 0)]
aim = vector(0, -10)
state = {'score': 1, 'heighscore': 1,}
height = 420
width = 420
playing = False
writer = Turtle(visible=False)


def start():
    global aim
    global snake
    global food
    global poisons
    global score
    global heighscore
    global playing
    clear()
    playing = True
    food = vector(0, 0)
    poisons = [vector(100,0)]
    snake = [vector(10, 0)]
    aim = vector(0, -10)
    if state['score'] > state['heighscore']:
        state['heighscore'] = state['score']
    state['score'] = 1
    writer.undo()
    writer.write(str(state['heighscore']) + '\n' + str(state['score']))
    update()
def menu():
    global playing
    playing = False
    clear()
    onkey(start, 'space')
    onkey(move, 'space')
    write("Menu", align='center', font=('Arial', 30, 'normal'))
    update()
def inside(head):
    return -width/2 < head.x < width/2 and -height/2 < head.y < height/2
def change(x, y):
    aim.x = x
    aim.y = y
def move():
    global score
    global heighscore
    global playing
    if playing:
        head = snake[-1].copy()
        head.move(aim)
        if not inside(head) or head in snake or head in poisons:
            square(head.x,head.y,9,'red')
            update()
            start()
            ontimer(move, 100)
        else:
            snake.append(head)
            if head == food:
                food.x = randrange(round(-width/20)+1, round(width/20)-1)*10
                food.y = randrange(round(-height/20)+1, round(height/20)-1)*10
                while food in snake or food in poisons:
                    food.x = randrange(round(-width/20)+1, round(width/20)-1)*10
                    food.y = randrange(round(-height/20)+1, round(height/20)-1)*10
                poison = vector(randrange(round(-width/20)+1, round(width/20)-1)*10, randrange(round(-height/20)+1, round(height/20)-1)*10)
                while poison in snake or poison in poisons:
                    poison = vector(randrange(round(-width/20)+1, round(width/20)-1)*10, randrange(round(-height/20)+1, round(height/20)-1)*10)
                poisons.append(poison)
                state['score'] = len(snake)
                writer.undo()
                writer.write(str(state['heighscore'])+'\n' + str(state['score']))
            else:
                snake.pop(0)
            clear()

            for body in snake:
                square(body.x, body.y,9,'black')
            square(food.x,food.y,9,'green')
            for poison in poisons:
                square(poison.x, poison.y, 9, 'purple')
            update()
            ontimer(move, 100)
setup(width, height, 370, 100)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
onkey(start, 'space')
onkey(menu, 'Escape')
hideturtle()
tracer(False)
writer.color('white')
writer.goto(180, 180)
writer.color('black')
writer.write(str(state['heighscore']) + '\n' + str(state['score']))
start()
move()
done()