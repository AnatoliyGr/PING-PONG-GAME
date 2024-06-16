import turtle
from random import choice, randint

window = turtle.Screen()
window.title("Ping Pong")
window.setup(width = 1.0, height = 1.0)
window.bgcolor('black')
window.tracer(3)

scoreA = 0
scoreB = 0
FONT = ('Arial', 40)
s1 = turtle.Turtle()
s1.hideturtle()
s1.color('white')
s1.setposition(-200, 300)
s1.write(scoreA, font=FONT)

s2 = turtle.Turtle()
s2.hideturtle()
s2.color('white')
s2.setposition(200, 300)
s2.write(scoreB, font = FONT)


shape = turtle.Turtle()
shape.hideturtle()
shape.speed(0)
shape.color('green')
shape.begin_fill()
shape.goto(-500, 300)
shape.down()
shape.goto(-500, -300)
shape.goto(500, -300)
shape.goto(500, 300)
shape.goto(-500, 300)
shape.end_fill()

center = turtle.Turtle()
center.hideturtle()
center.speed(0)
center.color('white')
center.goto(0, 300)
center.goto(0, -300)

rocketA = turtle.Turtle()
rocketA.up()
rocketA.speed(0)
rocketA.goto(-450, 0)
rocketA.color('white')
rocketA.shape('square')
rocketA.shapesize(5, 1)

def move_up():
    y = rocketA.ycor() + 20
    if y > 250:
        y = 250
    rocketA.sety(y)


def move_down():
    y = rocketA.ycor() - 20
    if y < -250:
        y = -250
    rocketA.sety(y)


rocketB = turtle.Turtle()
rocketB.up()
rocketB.speed(0)
rocketB.goto(450, 0)
rocketB.color('white')
rocketB.shape('square')
rocketB.shapesize(5, 1)

def move_upB():
    y = rocketB.ycor() + 20
    if y > 250 :
        y = 250
    rocketB.sety(y)


def move_downB():
    y = rocketB.ycor() - 20
    if y < -250:
        y = -250
    rocketB.sety(y)


ball = turtle.Turtle()
ball.color('red')
ball.shape('circle')
ball.dx = 3
ball.dy = 3
ball.penup()
ball.speed(0)


window.listen()
window.onkeypress(move_upB, 'Up')
window.onkeypress(move_downB, 'Down')
window.onkeypress(move_up, 'w')
window.onkeypress(move_down, 's')

while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.dy = - ball.dy

    if ball.xcor() >= 490:
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])
        scoreA += 1
        s1.clear()
        s1.write(scoreA, font=FONT)
    if ball.xcor() <= - 490:
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])
        scoreB += 1
        s2.clear()
        s2.write(scoreB, font=FONT)
    if ball.ycor() >= rocketB.ycor() - 50 and ball.ycor() <= rocketB.ycor() + 50\
        and ball.xcor() >= rocketB.xcor() - 5 and ball.xcor() <= rocketB.xcor() + 5:
        ball.dx = - ball.dx
    if ball.ycor() >= rocketA.ycor() - 50 and ball.ycor() <= rocketA.ycor() + 50\
        and ball.xcor() >= rocketA.xcor() - 5 and ball.xcor() <= rocketA.xcor() + 5:
        ball.dx = - ball.dx


window.mainloop()