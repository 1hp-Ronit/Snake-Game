from turtle import Screen
import time
from snake import Snake
from food import Food
from Score_Board import ScoreBoard
# Configuring screen
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Butter Check kariye")
screen.tracer(0)  # Turning off the tracer that is screen refreshing so we can manually update the screen

# Making objects

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

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
        scoreboard.increase_score()
    # Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()