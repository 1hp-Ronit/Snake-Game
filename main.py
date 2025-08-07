from turtle import Screen, Turtle
import time

# Configuring screen
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Butter Check kariye")
screen.tracer(0)  # Turning off the tracer that is screen refreshing so we can manually update the screen

# Making objects
starting_coordinates = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_coordinates:
    new_block = Turtle(shape='square')
    new_block.color("#e7a94d")
    new_block.penup()
    new_block.goto(position)
    segments.append(new_block)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)


screen.exitonclick()