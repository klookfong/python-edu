from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, left_panel):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.left_panel = left_panel
        if self.left_panel:
            self.goto(-350,0)
        else:
            self.goto(350,0)

    def go_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def go_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)
