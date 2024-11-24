from turtle import Turtle

class Boundary(Turtle) :
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.goto(290 , 290)
        for i in range(0, 4):
            self.pendown()
            self.pensize(10)
            self.right(90)
            self.forward(580)

