import turtle
from turtle import Turtle
import random
COLOR_LIST = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72)]


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.x_axis = -220
        self.y_axis = 280

    def create_wall(self):
        wall_list = []
        for wall in range(56):
            wall = Turtle(shape="square")
            turtle.colormode(255)
            wall.color(random.choice(COLOR_LIST))
            wall.penup()
            wall.pen(outline=3)
            wall.shapesize(stretch_len=3, stretch_wid=1, outline=1)
            wall.setpos(x=self.x_axis, y=self.y_axis)
            wall_list.append(wall)
            if len(wall_list) % 8 == 0:
                self.y_axis -= 20
                self.x_axis = -220
            else:
                self.x_axis += 60
        return wall_list
