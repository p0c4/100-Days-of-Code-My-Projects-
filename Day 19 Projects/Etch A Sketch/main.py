from turtle import Turtle, Screen

turti = Turtle()


def move_forward():
    turti.forward(10)


def move_backward():
    turti.forward(-10)


def counter_clockwise():
    turti.left(10)
    turti.forward(10)


def clockwise():
    turti.right(10)
    turti.forward(10)


def clear_drawing():
    turti.clear()
    turti.penup()
    turti.home()
    turti.pendown()


screen = Screen()
screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="c", fun=clear_drawing)
screen.exitonclick()
