from turtle import Screen
import time
from snake import Snake
from food import Food
# Configuring screen
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Butter Check kariye")
screen.tracer(0)  # Turning off the tracer that is screen refreshing so we can manually update the screen

# Making objects

snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
screen.exitonclick()