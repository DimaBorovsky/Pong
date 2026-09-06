from turtle import Turtle

class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        user = Turtle()
        computer = Turtle()
        self.user_score  = 0
        self.computer_score = 0
        user.ht()
        computer.ht()
        user.penup()
        computer.penup()
        user.goto(-50,270)
        computer.goto(50,270)
        user.color("white")
        computer.color("white")
        user.write(arg=f"User: {self.computer_score}",align="right",font=("Arial",14,"normal"))
        computer.write(arg=f"Computer: {self.computer_score}",align="right",font=("Arial",14,"normal"))


    def increase_user_score(self):
        self.clear()
        self.user_score +=1
        self.write(self.user_score, align="left", font=("Arial", 24, "normal"))



    def increase_computer_score(self):
        self.clear()
        self.computer_score +=1
        self.write(self.computer_score, align="right", font=("Arial", 24, "normal"))





