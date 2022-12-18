from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_generated = []
        self.move_distance = 5

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            cari = Turtle("square")
            cari.shapesize(stretch_wid=1, stretch_len=2)
            cari.color(random.choice(COLORS))
            cari.penup()
            cari.goto(300, random.randint(-250, 250))
            cari.setheading(180)
            self.car_generated.append(cari)

    def move_car(self):
        for car in self.car_generated:
            car.forward(self.move_distance)

    def increment_move_speed(self):
        self.move_distance += 10
