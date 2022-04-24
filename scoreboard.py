from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0

    def point(self):
        self.score += 1

    def show_final_score(self):
        self.setpos(x=0, y=0)
        self.write(f"Game Over!\nYour Score is\n{self.score}", align="center", font=("Courier", 40, "normal"))

    def you_win(self):
        self.setpos(x=0, y=0)
        self.write(f"You Win!\nYour Score is\n{self.score}", align="center", font=("Courier", 40, "normal"))

