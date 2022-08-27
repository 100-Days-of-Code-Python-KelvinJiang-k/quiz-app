from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 10, "italic")
SCORE_FONT = ("Arial", 15, "bold")


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="test",
                                                     width=280, font=QUESTION_FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        # Label
        self.score_label = Label(text=f"Score: {self.quiz.score} / {self.quiz.question_number}",
                                 fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Buttons
        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score} / {self.quiz.question_number}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.button_cooldown()
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        self.button_cooldown()
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    # prevents spam clicking true or false button to bug app
    def button_cooldown(self):
        self.false_button.config(state='disabled')
        self.window.after(1000, lambda: self.false_button.config(state='active'))
        self.true_button.config(state='disabled')
        self.window.after(1000, lambda: self.true_button.config(state='active'))
