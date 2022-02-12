from turtle import Turtle, Screen
import random

tim = Turtle()
colors = ["green yellow", "lime", "beige", "dark olive green", "goldenrod", "peru", "chocolate", "dark red", "purple",
          "magenta", "medium orchid", "dark violet"]
# num_sides = 3
# final = 10


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()
