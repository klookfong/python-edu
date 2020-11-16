from turtle import Turtle, Screen
import random

racing = False
screen = Screen()
screen.setup(width=500, height=400)


def make_turtles():
    screen.resetscreen()
    racing = False
    turtles = []
    y_positions = [-70, -40, -10, 20, 50, 80]
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    for i in range(len(colors)):
        new_turtle = Turtle(shape='turtle')
        new_turtle.penup()
        new_turtle.color(colors[i])
        new_turtle.goto(x=-230, y=y_positions[i])
        turtles.append(new_turtle)
    racing = True
    start(racing = racing, turtles = turtles, user_bet = user_bet)


def start(racing, turtles, user_bet):
    while racing:
        for turtle in turtles:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                racing = False
            turtle.forward(random.randint(10,20))
    print("The winner was", winning_color.upper())
    print("You Win!" if user_bet == winning_color else "You Lose")



screen.onkey(make_turtles, 'r')

screen.listen()
screen.exitonclick()