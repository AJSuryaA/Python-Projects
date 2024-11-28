from turtle import Screen
from score import *

from playground import playa_area
from paddle import *
from ball import *
start_game = True

canvas = Screen()
canvas.setup(1000,600)
canvas.bgcolor("black")
canvas.title("Ping Pong Game")
canvas.tracer(0)

playa_area()
right_paddle = Paddle((70,0))
left_paddle = Paddle((-460,0))

ball = Ball()
score = Score()
score.update()

canvas.listen()
canvas.onkeypress(right_paddle.go_up , "Up")
canvas.onkeypress(right_paddle.go_down , "Down")
canvas.onkeypress(left_paddle.go_up , "w")
canvas.onkeypress(left_paddle.go_down , "s")


def player_1_point():
    if ball.xcor() < -470 :
        score.add_score_player_1()
        ball.goto(-200,0)
        ball.bounce_x()
        score.r()
        if score.player_1_score == score.win_score :
            score.win()
            global start_game
            start_game = False

def player_2_point():
    if ball.xcor() > 70:
        score.add_score_player_2()
        ball.goto(-200, 0)
        ball.bounce_x()
        score.r()
        if score.player_2_score == score.win_score :
            score.win()
            global start_game
            start_game = False

def collide_y():
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

def collide_paddle_right():
    if ball.xcor() > 50 and ball.distance(right_paddle) <= 80 :
        ball.bounce_x()

def collide_paddle_left():
    if ball.xcor() < -440 and ball.distance(left_paddle) <= 80 :
        ball.bounce_x()



while start_game :
    canvas.update()
    ball.ball_move()
    collide_y()
    collide_paddle_right()
    collide_paddle_left()
    player_1_point()
    player_2_point()

canvas.exitonclick()
