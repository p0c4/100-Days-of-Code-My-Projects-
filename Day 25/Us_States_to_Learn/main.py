import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
list_state = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in  list_state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("purple")
        data_state = data[data.state == answer_state]
        t.goto(int(data_state.x), int(data_state.y) )
        t.write(answer_state, align="center", font=("Arial", 8, "normal"))

#After prompt = exit, create a file for states to learn.
states_to_learn = []
for state in list_state:
    if state not in guessed_states:
        states_to_learn.append(state)

data_states_to_learn = pandas.DataFrame(states_to_learn)
data_states_to_learn.to_csv("data_states_to_learn.csv")
