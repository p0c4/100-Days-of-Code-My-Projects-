import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']
y_poss = [-75, -45, -15, 15, 45, 75]
all_turtles = []

for turti_index in range(0, 6):
    turti = Turtle(shape='turtle')
    turti.penup()
    turti.color(colors[turti_index])
    turti.goto(x=-230, y=y_poss[turti_index])
    all_turtles.append(turti)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
