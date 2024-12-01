from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# prev = 0

class CarManager:
    def __init__(self):
        self.all_cars = list([])
        self.i = 6
        self.j = [1]

    def spawn_cars(self):
        a = random.randint(0,self.i)
        if a in self.j :
            new_car_1 = Turtle()
            new_car_1.penup()
            new_car_1.shape("square")
            new_car_1.color(random.choice(COLORS))
            new_car_1.shapesize(1,2)
            new_position = (300 , random.choice([x for x in range(-250,250,30)]))
            # global prev
            # if new_position != prev :
            new_car_1.goto(new_position)
            self.all_cars.append(new_car_1)
                # prev = new_position


    def move_cars(self):
        for i in range(len(self.all_cars)):
            self.all_cars[i].backward(MOVE_INCREMENT)

    def check_boundary(self):
        for i in range(len(self.all_cars)- 1, -1, -1):
            if self.all_cars[i].xcor() < -300:
                print(i)
                self.all_cars[i].color("black")



    def increase_i(self):
        self.i += 2
        self.j += 1