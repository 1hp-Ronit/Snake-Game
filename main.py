from turtle import Screen, Turtle
import time
from snake import Snake
# Configuring screen
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Butter Check kariye")
screen.tracer(0)  # Turning off the tracer that is screen refreshing so we can manually update the screen

# Making objects

snake = Snake()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()