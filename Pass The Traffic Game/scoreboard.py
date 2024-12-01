from turtle import Turtle

FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.font = FONT
        self.start_score = 0
        self.win_score = 10
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.score_board()

    def score_board(self):
        self.color("white")
        self.penup()
        self.goto(-200 , 260)
        self.write(f"Level : {self.start_score}",align="center",font=self.font)

    def add_score(self):
        self.start_score += 1
        self.update_score()

    def win_notice(self):
        self.clear()
        self.color("blue")
        self.penup()
        self.goto(0, 0)
        self.write("You Win", align="center", font=("Courier", 30, "bold"))
        self.score_board()

    def game_over(self):
        self.clear()
        self.color("red")
        self.penup()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 30, "bold"))
        self.score_board()



