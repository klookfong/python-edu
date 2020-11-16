from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.left(90)
        self.resetting()

    def move_up(self):
        self.forward(10)
    
    def resetting(self):
        self.goto(0,-250)