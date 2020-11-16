from turtle import Turtle, Screen
import time

class Snake:
    def __init__(self):
        self.turtles = []
        self.STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
        self.MOVE_DISTANCE = 20
        self.UP = 90
        self.DOWN = 270
        self.LEFT = 180
        self.RIGHT = 0
        self.new_snake()
        self.head = self.turtles[0]


    def new_snake(self):
        for pos in self.STARTING_POSITIONS:
            self.new_segment(pos)
            
    def new_segment(self, pos):
        t = Turtle(shape='square')
        t.color('white')
        t.penup()
        t.goto(pos)
        self.turtles.append(t)

    def extend(self):
        pos = self.turtles[-1].position()
        self.new_segment(pos)

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[i - 1].xcor()
            y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(x,y)
        self.turtles[0].forward(20)

    def up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)
    def down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)
    def left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)
    def right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)

        

