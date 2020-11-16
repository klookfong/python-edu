from turtle import Turtle
import random

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.increase = 1
        self.move_speed = 10
        self.cars = []
        self.hideturtle()
        self.create_cars()

    def create_cars(self):
        for i in range(0,3):
            for i in range(0, len(self.colors)-1):
                new_car = Turtle(shape='square')
                new_car.penup()
                new_car.color(self.colors[i])
                new_car.goto(240, -200)
                self.cars.append(new_car)

        for i in range(len(self.cars)):
            self.cars[i].left(180)
            x = self.cars[i].xcor() + 10*(random.randint(1,40))
            y = self.cars[i].ycor() + 10*(random.randint(1,40))
            self.cars[i].goto(x,y)
  

            
    
    def resetting(self):
        for car in self.cars:
            car.goto(240, -200)
            x = car.xcor() + 10*(random.randint(1,40))
            y = car.ycor() + 10*(random.randint(1,40))
            car.goto(x,y)

    def increase_speed(self):
        self.move_speed *= self.increase

    def move_cars(self):
        for car in self.cars:
            if len(self.cars) < 20:
                forward = self.increase
                car.forward(forward*random.randint(1,10))

    

