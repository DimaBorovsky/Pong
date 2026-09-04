from turtle import Turtle
USER_STARTING_POSITIONS = [(-290, 0), (-290, -20), (-290, -40)]
COMPUTER_STARTING_POSITIONS = [(290, 0), (290, -20), (290, -40)]

class Paddle:



    def __init__(self):
        self.paddle_segments = []
        self.create_user_paddle()
        self.create_computer_paddle()
        self.head =self.paddle_segments[0]


    def create_user_paddle(self):
        for position in USER_STARTING_POSITIONS:
            paddle_seg = Turtle(shape="square")
            paddle_seg.color("white")
            paddle_seg.penup()
            paddle_seg.goto(position)
            self.paddle_segments.append(paddle_seg)


    def create_computer_paddle(self):
        for position in COMPUTER_STARTING_POSITIONS:
            paddle_seg = Turtle(shape="square")
            paddle_seg.color("white")
            paddle_seg.penup()
            paddle_seg.goto(position)
            self.paddle_segments.append(paddle_seg)
