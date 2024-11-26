import time
from lib2to3.fixes.fix_input import context
from turtle import Screen
from score import *

from playground import playa_area
from paddle import *
from ball import *
game_start = True

canvas = Screen()
canvas.setup(1000,600)
canvas.bgcolor("white")
canvas.title("Ping Pong Game")
canvas.tracer(0)

playa_area()
right_paddle = Paddle((70,0))
left_paddle = Paddle((-460,0))

ball = Ball()
score = Score()

canvas.listen()
canvas.onkeypress(right_paddle.go_up , "Up")
canvas.onkeypress(right_paddle.go_down , "Down")
canvas.onkeypress(left_paddle.go_up , "w")
canvas.onkeypress(left_paddle.go_down , "s")

def player_1_point():
    if ball.xcor() < -480:
        score.add_score_player_1()
        ball.goto(-200,0)
        ball.bounce_x()

def player_2_point():
    if ball.xcor() > 70:
        score.add_score_player_2()
        ball.goto(-200, 0)


def collide_y():
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
def collide_paddle_right():
    if ball.xcor() > 50 and ball.distance(right_paddle) <= 80 :
        ball.bounce_x()

def collide_paddle_left():
    if ball.xcor() < -440 and ball.distance(left_paddle) <= 80 :
        ball.bounce_x()

while game_start :
    canvas.update()
    ball.ball_move()
    collide_y()
    collide_paddle_right()
    collide_paddle_left()
    player_1_point()
    player_2_point()

canvas.exitonclick()