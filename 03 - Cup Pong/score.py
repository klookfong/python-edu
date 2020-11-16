from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,270)
        self.color('white')
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.formatting = ('times', 20, 'normal')
        self.write("LEFT: " + str(self.left_score) + "   SCORE   " + " RIGHT: " + str(self.right_score), font=self.formatting, align='center')


    def write_score(self):
        self.clear()
        self.write("LEFT: " + str(self.left_score) + "   SCORE   " + " RIGHT: " + str(self.right_score), font = self.formatting, align = 'center')

    def update_score(self, isright):
        if isright:
            self.right_score += 1
        else:
            self.left_score += 1
        self.write_score()