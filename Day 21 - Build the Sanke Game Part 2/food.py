from turtle import Turtle
import random
colors = ["red", "orange", "blue", "green", "white"]
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("green")
        #self.color(random.choice(colors))
        #self.speed("fastest")
        self.speed(5)
        self.refresh()
        

    def refresh(self):
        self.color(random.choice(colors))
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)