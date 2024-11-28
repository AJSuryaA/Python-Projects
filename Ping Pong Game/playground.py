from turtle import Turtle


def playa_area():

    background = Turtle("square")
    background.color("white")
    background.shapesize(30, 1)
    background.penup()
    background.goto(100, 0)

    background = Turtle("square")
    background.color("white")
    background.shapesize(1, 30)
    background.penup()
    background.goto(-200, 290)

    background = Turtle("square")
    background.color("white")
    background.shapesize(30, 1)
    background.penup()
    background.goto(-490, 0)

    background = Turtle("square")
    background.color("white")
    background.shapesize(1, 30)
    background.penup()
    background.goto(-200, -290)


