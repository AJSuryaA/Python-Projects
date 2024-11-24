from random import randint
from turtle import Turtle
from scoreboard import Score

class Food:


    def __init__(self):
        self.food = 0
        self.object_food = Turtle("circle")
        self.object_score = Score()
        self.object_food.color("red")
        self.object_food.shapesize(0.5)
        self.object_food.penup()
        self.f_cor = [(0 , 0)]

    def spawn_food(self):
        while self.food == 0 :
            food_cor = (randint(-280, 280), randint(-280, 280))
            self.object_food.goto(food_cor)
            self.food = 1
            self.f_cor = [food_cor]


    def catch_food(self , x_cor , y_cor):
        if self.object_food.distance(x_cor , y_cor) <= 20 :
            self.spawn_food()
            self.object_score.add_score()
            self.food = 0