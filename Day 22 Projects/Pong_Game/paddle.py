from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.color("white")
        self.penup()

    def move_up(self):
        y_cor = self.ycor()
        x_cor = self.xcor()
        self.goto(x_cor, y_cor + 20)

    def move_down(self):
        y_cor = self.ycor()
        x_cor = self.xcor()
        self.goto(x_cor, y_cor - 20)