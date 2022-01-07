import turtle

#Create the screen of the game
wind = turtle.Screen()
#Set the title of the window
wind.title("Ping pong by Salah")
#set the background color of the window
wind.bgcolor("black")
#Set the width and the height of the window
wind.setup(width=800, height=600)
#stop the window from updating
wind.tracer(0)


#Player 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("red")
player1.shapesize(stretch_len=1, stretch_wid=5)
player1.penup()
player1.goto(-380, 0)

#Player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("blue")
player2.shapesize(stretch_len=1, stretch_wid=5)
player2.penup()
player2.goto(370, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_len=1, stretch_wid=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

#Functions
def player1_up():
    y = player1.ycor()
    y += 20
    player1.sety(y)

def player1_down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)

def player2_up():
    y = player2.ycor()
    y += 20
    player2.sety(y)

def player2_down():
    y = player2.ycor()
    y -= 20
    player2.sety(y)
# Keyboard
wind.listen()
wind.onkeypress(player1_up,"w")
wind.onkeypress(player1_down,"s")

wind.onkeypress(player2_up,"Up")
wind.onkeypress(player2_down,"Down")



#Update the screen
while True:
    wind.update()

    # Move the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1

    if (ball.xcor() > 350 and ball.xcor() < 360 ) and (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40):
        ball.setx(350)
        ball.dx *= -1

    if (ball.xcor() < -350 and ball.xcor() > -360) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40):
        ball.setx(-350)
        ball.dx *= -1
