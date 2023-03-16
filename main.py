from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Gomu Gomu no Culverine Game")
screen.tracer(0)

game_over = False

snake = Snake()
food = Food()
points = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.end_game, key='x')


while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.chase()

    # detect food collision
    if snake.fist.distance(food) < 15:
        food.refresh()
        snake.extend()
        points.score += 1
        points.add_point()

    # detect wall collision
    if snake.fist.xcor() > 280 or snake.fist.xcor() < -280 or snake.fist.ycor() > 280 or snake.fist.ycor() < -280:
        points.reset_game()
        snake.new_attack()

    # detect tail collision
    for gomu in snake.python[1:]:
        if snake.fist.distance(gomu) < 10:
            points.reset_game()
            snake.new_attack()

    game_over = snake.shut_off

screen.exitonclick()
