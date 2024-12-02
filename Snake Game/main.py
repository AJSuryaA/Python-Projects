import time
from turtle import Screen
from boundary import Boundary
from snake import *
from food import *



object_screen = Screen()
object_screen.setup(width= 600 , height= 600)

object_screen.bgcolor("black")
object_screen.title(titlestring="My Snake Game")
object_screen.tracer(0)



snake_obj = Snake()
food_obj = Food()
boundary = Boundary()
object_screen.listen()
object_screen.onkey( snake_obj.up , "Up")
object_screen.onkey( snake_obj.right , "Right")
object_screen.onkey( snake_obj.left , "Left")
object_screen.onkey( snake_obj.down , "Down")


while snake_obj.start_game :
    object_screen.update()
    time.sleep(0.1)
    snake_obj.move()
    food_obj.spawn_food()
    food_obj.catch_food(snake_obj.head.xcor() ,snake_obj.head.ycor())
    snake_obj.update_snake()
    if (snake_obj.head.xcor() > 280) | (snake_obj.head.xcor() < -280) | (snake_obj.head.ycor() > 280) | (snake_obj.head.ycor() < -280) :
        food_obj.trigg_clear()
        snake_obj.restart_game()
    if snake_obj.collision() :
        food_obj.trigg_clear()
        snake_obj.restart_game()

object_screen.exitonclick()