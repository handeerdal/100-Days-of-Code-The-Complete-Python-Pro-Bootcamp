import tkinter as tk
import requests
import random
import html

BGCOLOR='#c6ac8f'
QUESTION='#eae0d5'
RED='#e63946'
GREEN='#7ae582'
score=0
answer=''
response=requests.get('https://opentdb.com/api.php?amount=50&category=15&type=boolean')
response.raise_for_status()
data=response.json()



def getquestion():
    global answer
    global data
    randomquestion=random.randint(0,49)
    question=data["results"][randomquestion]['question']
    decoded_question = html.unescape(question)
    answer=data["results"][randomquestion]['correct_answer']
    canvas.config(background=QUESTION)
    canvas.itemconfig(question_text, text=decoded_question)
    
    
    



def true_clicked():
    global answer
    global score
    if answer=='True':
        score+=1
        label.configure(text=f'Score: {score}',background=BGCOLOR)
        canvas.config(background=GREEN)
    else:
        canvas.config(background=RED)
    canvas.after(300, getquestion)





def false_clicked():
    global score
    global answer
    if answer=='False':
        score+=1
        label.configure(text=f'Score: {score}',background=BGCOLOR)
        canvas.config(background=GREEN)
    else:
        canvas.config(background=RED)
    canvas.after(300, getquestion)




window=tk.Tk()
window.configure(width=500,height=500)
window.title('TRIVIA APP')
window.config(background=BGCOLOR)
window.configure(padx=50,pady=50)


canvas = tk.Canvas(window, width=300, height=300, bg=QUESTION)
canvas.grid(column=0, row=1, columnspan=2)  # Let canvas span both columns

trueimage=tk.PhotoImage(file=r'27-Trivia Game App\a.png')
falseimage=tk.PhotoImage(file=r'27-Trivia Game App\b.png')

label=tk.Label(window,width=5,height=5)
label.configure(text=f'Score: {score}',background=BGCOLOR)
label.grid(column=1,row=0,sticky='E')

question_text = canvas.create_text(
    150, 150,  # X, Y coordinates (center of canvas)
    text="Question goes here",
    fill="black",
    font=('Comic Sans MS', 15, 'bold'),
    width=280  # Wrap text within 280 pixels
)


getquestion()


# True button
truebutton = tk.Button(window, width=70, height=70,image=trueimage,highlightthickness=0,background=BGCOLOR,command=true_clicked)
truebutton.grid(column=0, row=2, pady=10, padx=10)  

# False button
falsebutton = tk.Button(window, width=70, height=70,image=falseimage,highlightthickness=0,background=BGCOLOR,command= false_clicked)
falsebutton.grid(column=1, row=2, pady=10, padx=10) 





window.mainloop()

