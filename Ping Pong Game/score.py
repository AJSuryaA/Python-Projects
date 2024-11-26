from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(300,250)
        self.update()

    def update(self):

        self.clear()
        self.write(f"Score : \n\n\t player_1_score : {self.player_1_score} \n\n\t  "
                   f"player_2_score : {self.player_2_score}"
                        , align="center", font=("Arial ", 14, "normal"))

    def add_score_player_1(self):
        self.player_1_score += 1
        print(self.player_1_score)
        self.update()

    def add_score_player_2(self):
        self.player_2_score += 1
        print(self.player_2_score)
        self.update()