from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(x,y)
        self.add_score()

    def add_score(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=("Courier", 60, "normal"))
        self.score += 1
