from turtle import Turtle
ALINGMENT = "center"
FONT = ("Courier",20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALINGMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALINGMENT, font=FONT)




    def increase_score(self):
        self.score += 2
        self.clear()
        self.update_scoreboard()

        