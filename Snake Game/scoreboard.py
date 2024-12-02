from turtle import Turtle

updates = False


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-270, 260)
        self.high_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.current_score} \t High Score : {self.high_score}", align="left", font=("Arial ", 12, "normal"))

    def add_score(self):
        self.current_score += 1
        self.update_scoreboard()
        global updates
        updates = True

    def clear_score(self):
        if self.current_score > self.high_score :
            self.high_score = self.current_score
        self.current_score = 0
        self.update_scoreboard()
