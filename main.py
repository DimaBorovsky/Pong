from turtle import Screen
from paddle import Paddle
from time import sleep
from soreboard import ScoreBoard


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)



scoreboard = ScoreBoard()

right =Paddle((350, 0))
left =Paddle((-350, 0))


screen.listen()
screen.onkey(fun=right.up,key="Up")
screen.onkey(fun=right.down,key="Down")
screen.onkey(fun=left.up,key="w")
screen.onkey(fun=left.down,key="s")

game_is_on = True
while game_is_on:
    screen.update()








screen.exitonclick()