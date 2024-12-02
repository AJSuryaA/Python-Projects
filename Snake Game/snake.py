from turtle import Turtle

import scoreboard

snake_position_default = [(0, 0), (-10, 0), (-20, 0)]
snake_position = snake_position_default
distance = 10

class Snake:
    def __init__(self):
        self.snakes = []
        self.spawn()
        self.head = self.snakes[0]
        self.start_game = True
        self.exit_game = True

    def spawn(self):
        for position in snake_position:
            s = Turtle("square")
            s.color("white")
            s.shapesize(0.5)
            s.penup()
            s.speed("fastest")
            s.goto(position)
            self.snakes.append(s)

    def update_snake(self):
        if scoreboard.updates :
            s = Turtle("square")
            s.color("white")
            s.shapesize(0.5)
            s.penup()
            index_of_last_snake =  len(snake_position)-1
            u_x = snake_position[index_of_last_snake][0] - 10
            snake_position.append((u_x , 0))
            self.snakes.append(s)
            scoreboard.updates = False

    def collision(self):
        for i in range(len(self.snakes)-1 , 0 , -1):
            if self.head.distance(self.snakes[i]) < 5 :
                return True

    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            xcor = self.snakes[i - 1].xcor()
            ycor = self.snakes[i - 1].ycor()
            self.snakes[i].goto(xcor, ycor)
        self.head.forward(10)

    def up(self):
        if self.head.heading() != 270 :
            self.head.setheading(90)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def restart_game(self):
        print(self.snakes)
        for i in range(len(self.snakes)):
            self.snakes[i].hideturtle()
        self.snakes.clear()
        print(self.snakes)
        global snake_position
        print(snake_position)
        snake_position.clear()
        print(snake_position)
        snake_position = [(0, 0), (-10, 0), (-20, 0)]
        print(snake_position)
        self.spawn()
        self.head = self.snakes[0]

    def exit_g(self):
        self.exit_game = False