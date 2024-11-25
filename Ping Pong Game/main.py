from turtle import Screen , Turtle
from playground import playa_area
from paddle import *

canvas = Screen()
canvas.setup(1000,600)
canvas.bgcolor("white")
canvas.title("Ping Pong Game")

playa_area()
right_paddle = Paddle((70,0))
left_paddle = Paddle((-460,0))

canvas.listen()
canvas.onkey(right_paddle.go_up , "Up")
canvas.onkey(right_paddle.go_down , "Down")
canvas.onkey(left_paddle.go_up , "w")
canvas.onkey(left_paddle.go_down , "s")

canvas.exitonclick()