from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("slowest")
        self.x_moves = 10
        self.y_moves = 10

    def move_ball(self):
        x_val = self.xcor() + self.x_moves
        y_val = self.ycor() + self.y_moves
        self.goto(x_val, y_val)

    def y_bounce(self):
        self.y_moves *= -1

    def x_bounce(self):
        self.x_moves *= -1

    def reset(self):
        self.setpos(0, 0)
        self.y_bounce()
