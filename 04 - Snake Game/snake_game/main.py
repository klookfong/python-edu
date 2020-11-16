from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

sc = Screen()
sc.setup(width=600, height = 600)
sc.bgcolor('black')
sc.title("🐍 Game")
sc.tracer(0)
alive = True

sn = Snake()
food = Food()
score = Scoreboard()

sc.onkey(sn.up, "Up")
sc.onkey(sn.down, "Down")
sc.onkey(sn.left, "Left")
sc.onkey(sn.right, "Right")


sc.listen()

while alive:
    sc.update()
    time.sleep(0.1)
    sn.move()
    if sn.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        sn.extend()
    
    for segment in sn.turtles[1:]:
        if sn.head.distance(segment) < 10:
            alive = False


    if sn.head.xcor() > 300 or sn.head.xcor() < -300 or sn.head.ycor() > 300 or sn.head.ycor() < -300:
        alive = False
score.game_over()


sc.exitonclick()