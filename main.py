# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import turtle as tl

wn = tl.Screen()
wn.title("Mahsa Mohammadi")
wn.bgcolor("gray")
wn.setup(width=800,height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0


# player A
paddle_a =tl.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# player B
paddle_b =tl.Turtle()
paddle_b.speed(0)

paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball =tl.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2

#pen

pen = tl.Turtle()
pen.speed()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A : 0  player B : 0",align="center",font=("courer",24,"normal"))


# function

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

    # keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"y")
wn.onkeypress(paddle_b_down,"h")



# Main Loop
while True :
    wn.update()
    # movethe ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("player A : {}  player B : {}".format(score_a,score_b), align="center",
                  font=("courer", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("player A : {}  player B : {}".format(score_a, score_b), align="center",
                  font=("courer", 24, "normal"))

    # paddle and conflicts
    if ((ball.xcor() > 340 and ball.xcor() < 350 )and
            ball.xcor() < 350 and
        (ball.ycor() < paddle_b.ycor() + 40 ) and (ball.ycor()> paddle_b.ycor() -40 )):
        ball.setx(340)
        ball.dx *= -1

    if ((ball.xcor() < -340 and ball.xcor() > 350 )and
            ball.xcor() < 350 and
        (ball.ycor() < paddle_a.ycor() + 40 ) and (ball.ycor()> paddle_a.ycor() -40 )):
        ball.setx(340)
        ball.dx *= -1