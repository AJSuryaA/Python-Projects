from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.win_score = 10
        self.hideturtle()
        self.penup()
        self.update()

    def update(self):
        self.clear()
        self.a()
        self.r()
        self.l()
        self.h()
        self.b()

    def a(self):
        self.color("red")
        self.goto(250, 200 )
        self.write("Score :", align="center", font=("Arial ", 20 , "bold"))

    def b(self):
        self.color("white")
        self.goto(-200 , 325)
        self.write("Ping Pong Game ", align="center", font=("Arial ", 30 , "bold"))

    def add_score_player_1(self):
        self.player_1_score += 1
        self.update()

    def add_score_player_2(self):
        self.player_2_score += 1
        self.update()

    def r(self):
        self.color("green")
        self.goto(300, 100)
        self.write(f"Player 1 : \t{self.player_1_score}", align="center", font=("Arial ", 15, "bold"))

    def h(self):
        self.color("white")
        self.goto(300, -200)
        self.write(f"Take {self.win_score} points to win", align="center", font=("Arial ", 15, "bold"))


    def l(self):
        self.color("blue")
        self.goto(300, 0)
        self.write(f"Player 2 : \t{self.player_2_score}", align="center", font=("Arial ", 15, "bold"))

    def win(self):
        if self.player_1_score == self.win_score :
            self.clear()
            self.color("red")
            self.goto(300, -100)
            self.write(f"player 1 Wins", align="center", font=("Arial ", 20 , "bold"))
            self.l()
            self.r()
            self.a()
            self.b()

        if self.player_2_score == self.win_score :
            self.clear()
            self.color("red")
            self.goto(300, -100)
            self.write(f"player 2 Wins", align="center", font=("Arial ", 20 , "bold"))
            self.l()
            self.r()
            self.a()
            self.b()




