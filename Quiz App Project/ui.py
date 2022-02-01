from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain : QuizBrain) :
        self.quiz = quiz_brain
        

        self.window = Tk()
        self.window.title(string="Quizzler")
        self.window.config(padx=20,pady=20, bg= THEME_COLOR)

        self.score_label = Label(bg=THEME_COLOR,text=f"Score: {self.quiz.score}", font=("Arial",10,"bold"),fg="white")
        self.score_label.grid(column=1,row=0)
        
        self.question_canvas = Canvas(height=250,width=300)
        self.question_text = self.question_canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question text", 
            fill=THEME_COLOR, 
            font=("Arial",20,"italic")
            )
        self.question_canvas.grid(column=0,row=1,columnspan=2,pady=50)
        
        true_image = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_image,highlightthickness=0,command=self.clicking_right)
        self.true_button.grid(column=0,row=3)

        self.false_button = Button(image=false_img,highlightthickness=0, command=self.clicking_cross)
        self.false_button.grid(column=1,row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg="White",highlightthickness=0)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text,text=f"Quiz Completed.\nYour score was {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def clicking_right(self):
        self.feedback(self.quiz.check_answer("True"))
        
    def clicking_cross(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self,is_true):
        if is_true:
            self.question_canvas.config(bg="Green",highlightthickness=0)
            
        else:
            self.question_canvas.config(bg="Red",highlightthickness=0)

        self.window.after(1000,func=self.get_next_question)
        







        



        

        
        




        