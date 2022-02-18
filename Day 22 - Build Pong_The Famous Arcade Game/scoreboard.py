from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        # TODO : Create a line seprator b/w the scoreboard
        
    def create_line(self):
        self.shape("square")
        self.color("white")
        self.goto(0,280)
        self.tilt(270)
        self.forward(200)
        self.pu()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
    