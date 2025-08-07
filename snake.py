from turtle import Turtle
STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
    def create_snake(self):
        for position in STARTING_COORDINATES:
            new_block = Turtle(shape='square')
            new_block.color("#e7a94d")
            new_block.penup()
            new_block.goto(position)
            self.segments.append(new_block)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_FORWARD)


