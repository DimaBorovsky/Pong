from turtle import Screen
from paddle import Paddle
from time import sleep
from soreboard import ScoreBoard


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


paddle = Paddle()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=paddle.up,key="Up")
screen.onkey(fun=paddle.down,key="Down")

paddle.create_computer_paddle()
paddle.create_user_paddle()

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)








screen.exitonclick()