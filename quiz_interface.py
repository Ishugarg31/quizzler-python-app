import tkinter
import data
from app_brain import QuizBrain

theme_color="#375362"

class QuizInterface:
    def __init__(self,app_brain: QuizBrain):
        self.quiz=app_brain
        self.screen=tkinter.Tk()
        self.screen.title("Quizzler")
        self.screen.config(padx=20,pady=20,bg=theme_color)

        #Label
        self.score_label=tkinter.Label(text="Score: 0", bg=theme_color, fg="white")
        self.score_label.grid(row=0,column=1)

        #Canvas
        self.canvas=tkinter.Canvas(width=300, height=200,highlightthickness=0)
        self.que_text=self.canvas.create_text(150,100, width=280, text="Some text here",font=("Arial",18,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2, padx=50,pady=50)

        #Button
        yes_image=tkinter.PhotoImage(file="images/true.png")
        no_image=tkinter.PhotoImage(file="images/false.png")
        self.yes_button=tkinter.Button(image=yes_image,highlightthickness=0, command=self.yes_pressed)
        self.yes_button.grid(row=2, column=0)
        self.no_button=tkinter.Button(image=no_image,highlightthickness=0, command=self.no_pressed)
        self.no_button.grid(row=2, column=1)

        self.next_question()

        self.screen.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.get_next_question()
            self.canvas.itemconfig(self.que_text, text=q_text)
        else:
            self.canvas.itemconfig(self.que_text, text="You have reached the end of quiz")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def yes_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def no_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.screen.after(1000,self.next_question)




