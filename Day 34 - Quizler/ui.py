from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
PATH = "C:/PyLearning/projects/Day 34 - Quizler/images"

class Ui():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quizler")

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.main_canvas = Canvas(height=250, width=300)
        self.canvas_text = self.main_canvas.create_text(150, 125, text="Test canvas text", font=FONT, width=280)
        self.main_canvas.grid(column=0, row=1, columnspan=2, pady=40)

        true_button_image = PhotoImage(file=PATH + "/true.png")
        self.true_button = Button(image=true_button_image, borderwidth=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        
        false_button_image = PhotoImage(file=PATH + "/false.png")
        self.false_button = Button(image=false_button_image, borderwidth=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.main_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.main_canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.main_canvas.itemconfig(self.canvas_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))
    
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):   
        if is_right:
            self.main_canvas.config(bg="green")
        else:
            self.main_canvas.config(bg="red")
        
        self.window.after(1000, self.get_next_question)