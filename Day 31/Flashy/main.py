from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


# ---------------------------- Words Dictionary ------------------------------- #
try:
    data_file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data_file.to_dict(orient="records")


# ---------------------------- Functions ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    french_word = current_card["French"]
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    canvas.itemconfig(canvas_back_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(canvas_back_image, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_back_image = canvas.create_image(400, 263, image=card_front_image)
lang_text = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 250, text="", fill="black", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=wrong_image, command=next_card, highlightthickness=0, bg=BACKGROUND_COLOR)
cross_button.grid(column=0, row=1)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=is_known, highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(column=1, row=1)

next_card()


window.mainloop()
