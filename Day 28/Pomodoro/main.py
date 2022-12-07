from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_clicked():
    window.after_cancel(timer) # when reset clicked, cancel: timer =  window.after(count_down........)
    canvas.itemconfig(timer_text, text="00:00")
    t_label.config(text="timer", fg=GREEN)
    cm_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    loong_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        t_label.config(text="Break", fg=PINK)
        count_down(loong_break_sec)
    elif reps % 2 == 0:
        t_label.config(text="Break", fg=GREEN)
        count_down(short_break_sec)
    else:
        t_label.config(text="Work", fg=RED)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # changing parameters in canvas. it was config for labels.
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # wait 1 sec(1000ms), do something(count_down()). (window.after for time func.)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        cm_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# In order to add a picture, we first need to create a canvas.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # Canvas accept only tkinter's PhotoImage files.
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)  # If we don't pack or grid or coordinate object, it will not show on the screen.

# Labels
t_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
t_label.grid(column=1, row=0)

cm_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "normal"))
cm_label.grid(column=1, row=3)

# Buttons
start_button = Button(text="start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", command=reset_clicked)
reset_button.grid(column=2, row=2)

# so our window to stays on the screen.
window.mainloop()
