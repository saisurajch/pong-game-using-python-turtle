from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(x,y)

    def up(self):
        if self.ycor() < 260:
            y_ax = self.ycor() + 20
            self.goto(self.xcor(), y_ax)

    def down(self):
        if self.ycor() > -240:
            y_ax = self.ycor() - 20
            self.goto(self.xcor(), y_ax)
