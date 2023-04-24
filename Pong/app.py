import turtle

window  = turtle.Screen()

window.title("Ping-Pong Game")
window.bgcolor("black")
window.setup(width=900, height=700)
window.tracer(0)

# Paddle 1
paddleOne = turtle.Turtle()
paddleOne.speed(0)
paddleOne.shape("square")
paddleOne.shapesize(stretch_wid= 5, stretch_len=1)
paddleOne.color("red")
paddleOne.penup()
paddleOne.goto(-400, 0)


# Paddle 2
paddleTwo = turtle.Turtle()
paddleTwo.speed(0)
paddleTwo.shape("square")
paddleTwo.shapesize(stretch_wid= 5, stretch_len=1)
paddleTwo.color("blue")
paddleTwo.penup()
paddleTwo.goto(400, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# Score
p1 = 0
p2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("White")
score.penup()
score.hideturtle()
score.goto(0,300)
score.write("Player1: {}  Player2: {}".format(p1, p2), align="center", font=("courier", 24, "normal"))


### Functionalities ###

# Paddle 1 movement

def paddleOneUp():
    y = paddleOne.ycor()
    if y < 280:
        y += 10
        paddleOne.sety(y)

def paddleOneDown():
    y = paddleOne.ycor()
    if y > -280:
        y -= 10
        paddleOne.sety(y)


# Paddle 2 movement

def paddleTwoUp():
    y = paddleTwo.ycor()
    if y < 280:
        y += 10
        paddleTwo.sety(y)

def paddleTwoDown():
    y = paddleTwo.ycor()
    if y > -280:
        y -= 10
        paddleTwo.sety(y)

#  Ball movement

def ballMovement():
    global p1, p2
    if ball.ycor() > 350:
        ball.dy *= -1
    if ball.ycor() < -350:
        ball.dy *= -1
    if ball.xcor() < -450:
        ball.goto(0,0)
        ball.dx *= -1
        p2 += 1
        score.clear()
        score.write("Player1: {}  Player2: {}".format(p1, p2), align="center", font=("courier", 24, "normal"))

    if ball.xcor() > 450 :
        ball.goto(0,0)
        ball.dx *= -1
        p1 += 1
        score.clear()
        score.write("Player1: {}  Player2: {}".format(p1, p2), align="center", font=("courier", 24, "normal"))




    if (ball.xcor() > 390 and ball.xcor() < 450) and (ball.ycor() < paddleTwo.ycor() + 40 and ball.ycor() > paddleTwo.ycor() -40):
        ball.setx(390)
        ball.dx *= -1
    if (ball.xcor() < -390 and ball.xcor() > -450) and (ball.ycor() < paddleOne.ycor() +40 and ball.ycor() > paddleOne.ycor() - 40):
        ball.setx(-390)
        ball.dx *= -1
        

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

window.listen()
# Paddle 1
window.onkeypress(paddleOneUp, "w")
window.onkeypress(paddleOneDown, "s")

# Paddle 2
window.onkeypress(paddleTwoUp, "Up")
window.onkeypress(paddleTwoDown, "Down")

while True:
    window.update()
    ballMovement()