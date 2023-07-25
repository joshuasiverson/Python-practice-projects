from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.window.minsize(width=320, height=270)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="question",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR,
                                                     width=280
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text="score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        correct_image = PhotoImage(file="images/true.png")
        incorrect_image = PhotoImage(file="images/false.png")
        self.correct = Button(image=correct_image, highlightthickness=0, command=self.true)
        self.correct.grid(row=2, column=0)
        self.incorrect = Button(image=incorrect_image, highlightthickness=0, command=self.false)
        self.incorrect.grid(row=2, column=1)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="That's the end of the quiz")
            self.correct.config(state="disabled")
            self.incorrect.config(state="disabled")

    def true(self):
        is_right = self.quiz.check_answer('True')
        self.feedback(is_right)

    def false(self):
        is_right = self.quiz.check_answer('False')
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_question)

