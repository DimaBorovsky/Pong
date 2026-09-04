from turtle import Screen
from paddle import Paddle
from time import sleep

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


paddle = Paddle()

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    paddle.create_computer_paddle()
    paddle.create_user_paddle()







screen.exitonclick()