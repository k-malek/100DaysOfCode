from tkinter import Tk,Label,Canvas,Button
from PIL import ImageTk,Image
from quiz_brain import QuizBrain
from question_model import Question

THEME_COLOR = '#375362'
ITEM_PADDING=20

class QuizInterface:

    def __init__(self):
        self.quiz=self.get_new_quiz()

        self.window=Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.question_counter=Label(master=self.window, font=('Ariel',15,'italic'),bg=THEME_COLOR,fg='white')
        self.question_counter.grid(row=0,column=0,padx=ITEM_PADDING,pady=ITEM_PADDING)

        self.score_text=Label(master=self.window,text='Score: 0',font=('Ariel',15,'italic'),bg=THEME_COLOR,fg='white')
        self.score_text.grid(row=0,column=1,padx=ITEM_PADDING,pady=ITEM_PADDING)

        self.question_canvas = Canvas(width=300, height=250,master=self.window)
        self.question_text_field=self.question_canvas.create_text(150,125,font=('Arial', 20, 'italic'),width=280,text='Here be question',justify='center')
        self.question_canvas.grid(row=1, column=0,columnspan=2,padx=ITEM_PADDING,pady=ITEM_PADDING)
        
        true_img = ImageTk.PhotoImage(Image.open('images/true.png'))
        false_img = ImageTk.PhotoImage(Image.open('images/false.png'))
        self.true_button = Button(master=self.window, image=true_img, highlightthickness=0, command=lambda:self.check_answer('true'))
        self.false_button = Button(master=self.window, image=false_img, highlightthickness=0, command=lambda:self.check_answer('false'))
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.restart_button = Button(master=self.window, text='Play again', font=('Arial', 16), command=self.restart_game)

        self.update_question()

        self.window.mainloop()

    @staticmethod
    def get_new_quiz():
        return QuizBrain(Question.get_questions())
    
    def update_score(self):
        self.score_text.config(text=f'Score {self.quiz.score}')

    def update_question(self):
        if self.quiz.still_has_questions():
            self.question_canvas.config(bg='white')
            self.question_canvas.itemconfig(self.question_text_field,text=self.quiz.next_question())
            self.question_counter.config(text=f'Question {self.quiz.question_number} of {self.quiz.questions_count}')

    def check_answer(self,ans): 
        result=self.quiz.check_answer(ans)
        if result:
            self.question_canvas.config(bg='green')
        else:
            self.question_canvas.config(bg='red')
        self.update_score()
        if self.quiz.still_has_questions(): 
            self.window.after(1000,self.update_question)           
        else:
            self.window.after(1000,self.end_game)

    def restart_game(self):
        self.quiz=self.get_new_quiz()
        self.update_score()
        self.question_canvas.itemconfig(self.question_text_field,font=('Arial', 20, 'italic'))
        self.update_question()
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        self.restart_button.grid_remove()

    def end_game(self):
        self.question_canvas.config(bg='white')
        self.question_canvas.itemconfig(self.question_text_field,
                                            text=f'GG, you scored {self.quiz.score}/{self.quiz.questions_count}',
                                            font=('Arial', 30, 'bold')
                                            )
        self.true_button.grid_remove()
        self.false_button.grid_remove()
        self.restart_button.grid(row=2,column=0,columnspan=2)
