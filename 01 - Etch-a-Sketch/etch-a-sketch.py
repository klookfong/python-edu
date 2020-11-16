from turtle import Turtle, Screen


screen = Screen()
turtle = Turtle()

def up():
    turtle.forward(10)
def down():
    turtle.forward(-10)
def left():
    turtle.left(10)
def right():
    turtle.right(10)
def clear():
    turtle.clear()


screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(clear, "c")


screen.listen()



screen.exitonclick()