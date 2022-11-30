from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.current_level =0
        self.goto(-280, 250)
        self.level_update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)

    def level_update(self):
        self.write(f"Level: {self.current_level}", align="left", font=FONT)

    def level_up(self):
        self.clear()
        self.current_level += 1
        self.level_update()







