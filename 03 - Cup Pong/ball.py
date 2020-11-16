from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('circle')
        self.move_x = 10
        self.move_y = 10

    def move(self):
        x = (self.xcor() + self.move_x)
        y = (self.ycor() + self.move_y) 
        self.goto(x,y)
