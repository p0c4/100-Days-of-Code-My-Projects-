from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    # In case of using QuizBrain in QuizInterface class, we added it to the init func. as below
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some question text", fill=THEME_COLOR, font=("Arial", 18, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        r_image = PhotoImage(file="images/true.png")
        self.r_button = Button(image=r_image, bg=THEME_COLOR, highlightthickness=0, command=self.is_true)
        self.r_button.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, bg=THEME_COLOR,highlightthickness=0, command=self.is_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # After feedback color is given, change the color back to white
        self.canvas.config(bg="white")
        # Check if still have question
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        # if questions has ended disable the buttons and inform the player
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.r_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_true(self):
        is_true = self.quiz.check_answer("true")
        self.give_feedback(is_true)

    def is_false(self):
        is_false = self.quiz.check_answer("false")
        self.give_feedback(is_false)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, func=self.get_next_question)






