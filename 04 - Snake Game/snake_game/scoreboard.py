from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0,250)
        self.scores = [0]
        self.high_score = 0
        self.score_file('a')
        self.score_file('r')
        self.write("SCORE: " + str(self.score) + "    HIGHSCORE: " + str(self.high_score) , font=('times', 20, 'normal'), align='center')


    def update_score(self):
        self.write("SCORE: " + str(self.score) + "     HIGHSCORE: " + str(self.high_score) , font=('times', 20, 'normal'), align='center')

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.score_file('a', self.score)
        self.write('Game over', font=('times', 20, 'normal'), align='center')

    def score_file(self, mode, value=0):
        snake = open('snake.txt', mode) 
        if mode == "a":
            snake.write(str(value))
            snake.write('\n')
        elif mode == 'r':
            line = snake.readline()
            while line != "":
                try:
                    self.scores.append(int(line))
                    line = snake.readline()
                except:
                    pass
            self.high_score = max(self.scores)
        else:
            pass
        snake.close()
            