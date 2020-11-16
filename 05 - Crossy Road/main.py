from turtle import Screen, Turtle
from player import Player
from cars import Cars
from score import Score
import time

#Setting up the screen
sc = Screen()
sc.tracer(0)
sc.setup(width = 600, height = 600)
difficulty_increase = 1.25



#Instantiating the Cars, Player, and Scoreboard
player = Player()
score = Score()
cars = Cars()
sc.listen()
sc.onkey(player.move_up, 'Up')


playing = True
while playing:
    time.sleep(0.1)
    sc.update()
    cars.move_cars()

    #Checking for collision
    for car in cars.cars:
        if player.distance(car) < 20:
            playing = False
            score.goto(0,0)
            score.write("YOU LOSE", font=('times', 20, 'normal'), align='center')
    if player.ycor() > 250:
        player.resetting()
        cars.increase *= 1.15
        cars.resetting()
        score.score += 1
        score.write_score()

sc.exitonclick()