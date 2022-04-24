from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.coordinates = coordinates

        self.penup()
        self.setpos(self.coordinates)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
