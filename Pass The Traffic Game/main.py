import time
from turtle import Screen

from sqlalchemy.testing import fails_on

from player import *
from car_manager import *
from scoreboard import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.forward_move,"Up")
screen.onkey(player.backward_move,"Down")

def cross_finish_line():
    if player.ycor() >= player.finish_line :
        score.add_score()
        player.start_line()
a = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cross_finish_line()
    car.move_cars()
    car.check_boundary()
    if a == 3:
        car.spawn_cars()
        a = 0
    for cars in car.all_cars:
        if player.distance(cars) < 25 :
            score.game_over()
            game_is_on = False
    a += 1
    if score.start_score == score.win_score:
        score.win_notice()
        game_is_on = False

screen.exitonclick()