from turtle import Turtle, Screen
import random
import turtle

turti = Turtle()

turti.shape("turtle")
turtle.colormode(255)
turti.pensize(5)
turti.speed('fastest')
angles = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


for _ in range(45):
    turti.color(random_color())
    turti.circle(150)
    turti.setheading(turti.heading() + 8)


my_screen = Screen()
my_screen.exitonclick()
