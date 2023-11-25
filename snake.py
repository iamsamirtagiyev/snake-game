import turtle
import time
import random

speed = 0.15
tails = []
count = 0

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('lightgreen')
screen.title('Snake Game')
screen.tracer(0)

snake = turtle.Turtle()
snake.color('black')
snake.direction = 'stop'
snake.speed(0)
snake.penup()
snake.shape('square')
snake.goto(0, 100)

object = turtle.Turtle()
object.color('red')
object.shapesize(0.80, 0.80)
object.speed(0)
object.penup()
object.shape('circle')
object.goto(0, 0)

score = turtle.Turtle()
score.speed(0)
score.shape('square')
score.color('white')
score.penup()
score.goto(0, 260)
score.hideturtle()
score.write('score: {}'.format(count), align='center', font=('Courier', 24, 'normal'))


def move():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 20)

def up():
    if snake.direction != 'down':
        snake.direction = 'up'

def down():
    if snake.direction != 'up':
        snake.direction = 'down'

def left():
    if snake.direction != 'right':
        snake.direction = 'left'

def right():
    if snake.direction != 'left':
        snake.direction = 'right'

screen.listen()

screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')


while True:
    screen.update()

    if snake.xcor() > 300 or snake.xcor() < -300 or snake.ycor() > 300 or snake.ycor() < -300:
        snake.direction = 'stop'
        time.sleep(1)
        snake.goto(0, 0)

        for i in tails:
            i.goto(1000, 1000)

        tails = []
        count = 0
        speed = 0.15

    if snake.distance(object) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        object.goto(x, y)

        tail = turtle.Turtle()
        tail.shape('square')
        tail.speed(0)
        tail.penup()
        tail.color('white')
        tails.append(tail)

        count = count + 10
        score.clear()
        score.write('score: {}'.format(count), align='center', font=('Courier', 24, 'normal'))

        speed = speed - 0.001

    for i in range(len(tails) - 1, 0, -1):
        x = tails[i - 1].xcor()
        y = tails[i - 1].ycor()
        tails[i].goto(x, y)

    if len(tails) > 0:
        x = snake.xcor()
        y = snake.ycor()
        tails[0].goto(x, y)

    move()
    time.sleep(speed)