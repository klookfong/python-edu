from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


#Configuring the Screen
sc = Screen()
sc.tracer(0) #Don't use animations
sc.bgcolor('black')
sc.title('🏐 Pong')
sc.setup(width = 800, height = 600)


#Instantiating two padels, scoreboard and a ball
player1 = Paddle(left_panel=False)
player2 = Paddle(left_panel=True)
score = Score()
ball = Ball()



#Key bindings
sc.listen()
sc.onkey(player1.go_up, 'Up')
sc.onkey(player1.go_down, 'Down')

sc.onkey(player2.go_up, 'w')
sc.onkey(player2.go_down, 's')


#Start While Loop
playing = True
while playing:
    time.sleep(0.1)
    sc.update()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.move_y *= -1
    
    #Detect collision with the paddles
    if ball.xcor() > 320 or ball.xcor() < -320:
        if ball.distance(player1) < 50 or ball.distance(player2) < 50:
            ball.move_x *= -1
    
    #Detecting misses with the paddle
    if ball.xcor() > 400:
        ball.goto(0,0)
        score.update_score(False)
    elif ball.xcor() < -400:
        ball.goto(0,0)
        score.update_score(True)

    ball.move()
   
    


sc.exitonclick()