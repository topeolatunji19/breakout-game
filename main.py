from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
from scoreboard import ScoreBoard
import time

my_screen = Screen()
my_screen.setup(width=490, height=600)
my_screen.title("Break Out Game")
my_screen.bgcolor("black")
my_screen.tracer(0)

paddle = Paddle((0, -250))

ball = Ball()
my_wall = Wall()
wall_list = my_wall.create_wall()
scores = ScoreBoard()

my_screen.listen()

# Move paddle
my_screen.onkey(paddle.go_left, "Left")
my_screen.onkey(paddle.go_right, "Right")

game_time = 0.1
game_is_on = True

lives = 3
while game_is_on:
    time.sleep(game_time)
    my_screen.update()
    ball.move_ball()

    # Detect wall collision
    if ball.ycor() > 280:
        ball.y_bounce()
    # Detect Loss
    elif ball.ycor() < -280:
        if lives > 0:
            ball.reset()
            game_time = 0.1
            lives -= 1
        else:
            scores.show_final_score()
            game_is_on = False

    # Detect Wall collision
    if ball.xcor() > 220 or ball.xcor() < -220:
        ball.x_bounce()

    # Detect Brick collision
    for wall in wall_list:
        if ball.distance(wall) < 50 and ball.ycor() > -100:
            ball.y_bounce()
            wall.reset()
            scores.point()
            wall_list.remove(wall)
            if len(wall_list) == 0:
                scores.you_win()
                game_is_on = False

    # Detect paddle collision
    if ball.ycor() < -220 and ball.distance(paddle) < 50:
        game_time /= 1.15
        ball.y_bounce()


my_screen.exitonclick()
