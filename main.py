# need 1. scores, 2. a pair of 'paddles' # a ball
# player paddle controls, computer paddle controls

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

player1 = Paddle((350, 0))
player2 = Paddle((-350, 0))
ball = Ball()
scores = ScoreBoard()

game_going = True
screen.listen()
screen.onkey(fun=player1.up, key="Up")
screen.onkey(fun=player1.down, key="Down")
screen.onkey(fun=player2.up, key="w")
screen.onkey(fun=player2.down, key="s")

while game_going:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    # detect collision w/ wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with paddle
    if (ball.distance(player1) < 50 and ball.xcor() > 330) or (ball.distance(player2) < 50 and ball.xcor() < -330):
        ball.bounce_x()
    # detect a miss
    if ball.xcor() > 390:
        ball.new_point()
        scores.l_point()
    if ball.xcor() < -390:
        ball.new_point()
        scores.r_point()
    # end game
    if scores.r_score == 7 or scores.l_score == 7:
        game_going = False

screen.exitonclick()
