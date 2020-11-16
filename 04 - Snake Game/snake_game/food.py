import random
from turtle import Screen, Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('white')
        self.speed('fastest')
        self.refresh()
    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x,y)