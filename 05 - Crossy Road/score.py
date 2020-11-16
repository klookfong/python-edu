from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-200, 240)
        self.hideturtle()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.reset()
        self.penup()
        self.goto(-200, 240)
        self.hideturtle()
        self.write("SCORE: " + str(self.score), align = 'left', font = ('times', 20, 'normal'))
