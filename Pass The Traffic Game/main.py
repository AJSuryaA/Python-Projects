import time
from turtle import Screen
from player import *
from car_manager import *
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car = CarManager()

screen.listen()
screen.onkey(player.forward_move,"Up")
screen.onkey(player.backward_move,"Down")

def cross_finish_line():
    if player.ycor() >= player.finish_line :
        player.start_line()
a = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cross_finish_line()
    car.move_cars()
    if a == 5 :
        car.spawn_cars()
        a = 0
    a += 1
