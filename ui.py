from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=30, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.text = self.canvas.create_text(150, 125,
                                            width=280,
                                            fill='black',
                                            font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right = PhotoImage(file='images/true.png')
        self.correct = Button(image=right, highlightthickness=0, bg=THEME_COLOR, command=self.true_click)
        self.correct.grid(column=0, row=2)

        wrong = PhotoImage(file='images/false.png')
        self.incorrect = Button(image=wrong, highlightthickness=0, bg=THEME_COLOR, command=self.false_click)
        self.incorrect.grid(column=1, row=2)

        self.score_label = Label(text=f'Score: {self.quiz.score}', font=("Arial", 18, 'normal'), fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz.")
            self.correct.config(state='disabled')
            self.incorrect.config(state='disabled')

    def true_click(self):
        check = self.quiz.check_answer('True')
        if check:
            self.canvas.config(bg='green')
            self.quiz.score += 1
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.next_question)

    def false_click(self):
        check = self.quiz.check_answer('False')
        if not check:
            self.canvas.config(bg='green')
            self.quiz.score += 1
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.next_question)
