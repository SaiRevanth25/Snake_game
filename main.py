from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Score

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with food.

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall.

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        food.done()
        score.game_over()
        game_is_on = False

    # Detect collision with tail
    for segments in snake.segments[1:]:

        if snake.head.distance(segments) < 10:
            score.game_over()
            food.done()
            game_is_on = False

screen.exitonclick()
