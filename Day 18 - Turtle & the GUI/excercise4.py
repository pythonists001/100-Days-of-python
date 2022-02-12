from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ["green yellow", "lime", "beige", "dark olive green", "goldenrod", "peru", "chocolate", "dark red", "purple",
          "magenta", "medium orchid", "dark violet"]
direction = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")

for _ in range(500):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()
