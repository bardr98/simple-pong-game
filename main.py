import turtle

wn = turtle.Screen()
wn.title("@Bardr98 game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_blue = 0
score_red = 0

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("BLUE: {}  RED: {}".format(score_blue, score_red), align="center", font=("Courier", 24, "normal"))

# how to move
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color("white")
pen1.penup()
pen1.hideturtle()
pen1.goto(280, 260)
pen1.write("[up: Up(^) | down: Down(^)] ", align="center", font=("Courier", 10, "normal"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(-300, 260)
pen2.write("[up: w | down: s]", align="center", font=("Courier", 10, "normal"))

# paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.05
ball.dy = 0.05

# functions
def a_up():
    if paddle_a.ycor() < 260:
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

def a_down():
    if paddle_a.ycor() > -260:
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

def b_up():
    if paddle_b.ycor() < 260:
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

def b_down():
    if paddle_b.ycor() > -260:
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(a_up, "w")
wn.onkeypress(a_down, "s")
wn.onkeypress(b_up, "Up")
wn.onkeypress(b_down, "Down")

# main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_blue += 1
        ball.dx = 0.05
        ball.dy = 0.05
        ball.color("white")
        pen.clear()
        pen.write("BLUE: {}  RED: {}".format(score_blue, score_red), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_red += 1
        ball.dx = 0.05
        ball.dy = 0.05
        ball.color("white")
        pen.clear()
        pen.write("BLUE: {}  RED: {}".format(score_blue, score_red), align="center", font=("Courier", 24, "normal"))

    # ball bounce
    if 340 < ball.xcor() < 350 and (
            ball.ycor() < paddle_b.ycor() + 50 and (ball.ycor() > paddle_b.ycor() - 50)):
        ball.dx *= -1
        ball.dx *= 1.15
        ball.dy *= 1.15
        ball.color("red")
    if -340 > ball.xcor() > -350 and (
            ball.ycor() < paddle_a.ycor() + 50 and (ball.ycor() > paddle_a.ycor() - 50)):
        ball.dx *= -1
        ball.dx *= 1.15
        ball.dy *= 1.15
        ball.color("blue")
