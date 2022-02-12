from turtle import Turtle, Screen

tim = Turtle()
for _ in range(15):
    tim.pd()
    tim.forward(10)
    tim.pu()
    tim.forward(10)

screen = Screen()
screen.exitonclick()
