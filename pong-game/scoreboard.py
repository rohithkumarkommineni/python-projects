from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-20, 250)
        self.write(self.l_score, align="center", font=("Courier", 30, "normal"))
        self.goto(20, 250)
        self.write(self.r_score, align="center", font=("Courier", 30, "normal"))

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def l_point(self):
        self.l_score += 1
        self.update_score()
