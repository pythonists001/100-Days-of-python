from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('./Day 24 - Files, Directories and Paths/data.txt') as f:
            self.high_score = int(f.read())
        # self.high_score = int(self.get_highScore())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # self.write_highScore()
            with open('./Day 24 - Files, Directories and Paths/data.txt', mode="w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def get_highScore(self):
    #     with open('./Day 24 - Files, Directories and Paths/data.txt') as f:
    #         return f.read()
    
    def write_highScore(self):
        with open('./Day 24 - Files, Directories and Paths/data.txt', mode ='w') as f:
            f.write(str(self.high_score))
