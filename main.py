from time import sleep
from turtle import Screen
from paddle import Paddle
from soreboard import ScoreBoard
from ball import Ball

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)





scoreboard = ScoreBoard()
ball = Ball()
right =Paddle((350, 0))
left =Paddle((-350, 0))


screen.listen()
screen.onkey(fun=right.up,key="Up")
screen.onkey(fun=right.down,key="Down")
screen.onkey(fun=left.up,key="w")
screen.onkey(fun=left.down,key="s")

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()

    ball.ball_movment()
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.y_bounce()

    if ball.distance(right) < 50 and ball.xcor() > 320 or ball.distance(left) < 50 and ball.xcor() < -320:
        ball.x_bounce()


    if ball.xcor() > 400:
        ball.reset()
        scoreboard.l_point()
        ball.x_move +=5

    elif ball.xcor() < -400 :
        scoreboard.r_point()
        ball.reset()
        ball.x_move +=5








screen.exitonclick()