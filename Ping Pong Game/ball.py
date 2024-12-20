
from turtle import Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(-200,0)
        self.x_move = 0.2
        self.y_move = 0.2

    def ball_move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    # def paddle_bounce_right(self,x1,x2):
    #     if x2 > x1 :
    #         self.x_move = abs(self.x_move) * -1
    #         self.y_move = abs(self.y_move)
    #     if x2 == x1 :
    #         self.bounce_x()
    #     else :
    #         self.x_move = abs(self.x_move) * -1
    #         self.y_move = abs(self.y_move) * -1
    #
    # def paddle_bounce_left(self,x1,x2):
    #     if x2 > x1:
    #         self.x_move = abs(self.x_move)
    #         self.y_move = abs(self.y_move)
    #     if x2 == x1 :
    #         self.bounce_y()
    #     else :
    #         self.x_move = abs(self.x_move)
    #         self.y_move = abs(self.y_move) * -1
