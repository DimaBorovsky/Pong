from turtle import Turtle



class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.setheading(270)
        self.penup()
        self.forward(10)
        self.pendown()

    def dashed_line(self):
        self.penup()
        self.goto(0,380)
        self.setheading(270)
        for step in range(100):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
