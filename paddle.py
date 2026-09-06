from turtle import Turtle
USER_STARTING_POSITIONS = [(-380, 0), (-380, -20), (-380, -40)]
COMPUTER_STARTING_POSITIONS = [(380, 0), (380, -20), (380, -40)]
MOVE_DISTANCE = 20
UP_TURN_ANGLE = 90
DOWN_TURN_ANGLE = 270


class Paddle:




    def __init__(self):
        self.user_paddle_segments = []
        self.computer_paddle_segments = []
        self.create_user_paddle()
        self.create_computer_paddle()
        self.head =self.user_paddle_segments[0]


    def create_user_paddle(self):
        for position in USER_STARTING_POSITIONS:
            paddle_seg = Turtle(shape="square")
            paddle_seg.color("white")
            paddle_seg.penup()
            paddle_seg.goto(position)
            self.user_paddle_segments.append(paddle_seg)


    def create_computer_paddle(self):
        for position in COMPUTER_STARTING_POSITIONS:
            paddle_seg = Turtle(shape="square")
            paddle_seg.color("white")
            paddle_seg.penup()
            paddle_seg.goto(position)
            self.user_paddle_segments.append(paddle_seg)


    def up(self):
        for paddle in self.user_paddle_segments:
            paddle.setheading(UP_TURN_ANGLE)
            paddle.forward(MOVE_DISTANCE)


    def down(self):
        for paddle in self.user_paddle_segments:
            paddle.setheading(DOWN_TURN_ANGLE)
            paddle.forward(MOVE_DISTANCE)
