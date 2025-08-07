from turtle import Screen, Turtle


# Configuring screen
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Butter Check kariye")
screen.exitonclick()
# Making objects
starting_coordinates = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_coordinates:
    new_block = Turtle(shape='square')
    new_block.color("#e7a94d")
    new_block.goto(position)
    segments.append(new_block)
