from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.left(angle=90)
        self.goto(STARTING_POSITION)
        self.finish_line = FINISH_LINE_Y

    def forward_move(self):
        self.forward(MOVE_DISTANCE)

    def backward_move(self):
        self.backward(MOVE_DISTANCE)

    def start_line(self):
        self.goto(STARTING_POSITION)