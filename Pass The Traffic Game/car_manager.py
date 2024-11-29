from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

prev = 0

class CarManager:
    def __init__(self):
        self.all_cars = []


    def spawn_cars(self):
        new_car_1 = Turtle()
        new_car_1.penup()
        new_car_1.shape("square")
        new_car_1.color(random.choice(COLORS))
        new_car_1.shapesize(1,2)
        new_position = (300 , random.choice([x for x in range(-250,250,30)]))
        pos = new_position
        global prev
        if pos != prev :
            new_car_1.goto(pos)
        prev = pos
        new_car_1.left(angle=180)
        self.all_cars.append(new_car_1)

    def move_cars(self):
        for i in range(len(self.all_cars)):
         self.all_cars[i].forward(MOVE_INCREMENT)