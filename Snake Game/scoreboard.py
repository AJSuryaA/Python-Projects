from turtle import Turtle

updates = False


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.current_score}", align="left", font=("Arial ", 12, "normal"))


    def add_score(self):
        self.current_score += 1
        self.update_scoreboard()
        global updates
        updates = True