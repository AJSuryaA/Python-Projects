import turtle , random
from turtle import Turtle , Screen
import pandas as pd
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


screen = Screen()
screen.title("GUESS INDIAN STATES")
screen.setup(600,600)
image = "indian_map.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)  // used to get xcor and ycor of every states by clicking the map
# turtle.onscreenclick(get_mouse_click_coor)

score = 0

data = pd.read_csv("indian_states.csv")
all_states = data.states.tolist()

answer = ""
def ask():
    global answer
    answer = screen.textinput(title=f"{score}/30 Guess States of India", prompt="What's the next state name ?").title()

list = []
def display_state(x,y):
    global list
    t = Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x,y)
    t.color(random.choice(colors))
    t.write(f"{answer}")
    list.append(answer)

while True:
    ask()
    if answer in all_states:
        if answer not in list:
            a = data[data["states"] == answer ]
            score += 1
            display_state(float(a.x.item()) , float(a.y.item()))
            print(score)

screen.exitonclick()