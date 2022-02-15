# TODO Create a Snake Body
# TODO Move the Snake
# TODO Control the Snake
# TODO Detect collision with food
# TODO Create a scoreboard
# TODO Detect collision with wall
# TODO Detect collision with tail

from turtle import Screen, Turtle
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turning th tracer off, to off the animation

starting_positions = [(0,0), (-20,0), (-40,0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.pu()
    new_segment.goto(position)
    # Create a Snake Body - completed
    segments.append(new_segment)
#screen.update()  # To turn on the animation again

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):  # start=3, stop=0, step=-1
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()

        segments[seg_num].goto(new_x, new_y)  # getting hold of last segment and going to first segment position
                                              # 185 to revisit for concepts
    segments[0].forward(20) # Moving the first segment to a new position

screen.exitonclick()