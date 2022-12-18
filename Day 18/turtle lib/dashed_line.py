from turtle import Turtle, Screen

turti = Turtle()

turti.shape("turtle")
turti.color("orange")
colors = ['red', 'blue', 'orange', 'green', 'yellow', 'brown', 'black', 'pink', 'purple', 'grey']


def draw_shape(num_sides):
    ang = 360 / num_sides
    for _ in range(num_sides):
        turti.forward(100)
        turti.right(ang)


for shape_side in range(3, 11):
    turti.color(colors[shape_side - 3])
    draw_shape(shape_side)


my_screen = Screen()
my_screen.exitonclick()
