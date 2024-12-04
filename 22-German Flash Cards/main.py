import json
import tkinter as tk
import random
import time
from PIL import Image, ImageTk
from tkinter import messagebox

BGCOLORWINDOW='#ffc8dd'
BGCOLORCANVAS='#ffafcc'
truelist=[]
random_eng_word=''
ct=0


#-----------------------------------WELCOME----------------------------------#


#-----------------------------------BUTTON CLICK----------------------------------#


def enable_buttons():
    truebutton.config(state="normal")
    falsebutton.config(state="normal")
    


def truebuttonclicked():
    global ct
    if not data:  
        print("Dictionary is empty. Cannot proceed.")
        example_label.configure(text=f'{ct}/50 words guessed correct')

        return 
    
    example_label.configure(text=random_eng_word)
    truelist.append(random_eng_word)
    data.pop(random_eng_word)
    ct+=1
    print(ct)
    truebutton.config(state="disabled")
    falsebutton.config(state="disabled")

    wordloop()





#-----------------------------------WORD LOOP----------------------------------#

def wordloop():
    window.after(3000, enable_buttons)
    global random_eng_word
    random_eng_word=random.choice(list(data.keys()))
    example_label.configure(text=random_eng_word)
    english_label.configure(text='English')
    window.after(3000, wait) 





#-----------------------------------WAIT FUNCTION----------------------------------#

def wait():
    getkey=example_label.cget("text")
    example_label.configure(text=data[getkey])
    english_label.configure(text='German')





    

#-----------------------------------UI----------------------------------#

window=tk.Tk()

window.title('German Flash Cards')

window.minsize(width=500,height=500)

window.config(background=BGCOLORWINDOW,padx=100,pady=100)

canvas=tk.Canvas()
canvas.config(width=400,height=400,background=BGCOLORCANVAS,highlightthickness=0)
canvas.grid(column=1,row=1,sticky='', pady=30)

english_label = tk.Label(canvas, text='English', bg=BGCOLORCANVAS, font=('Comic Sans MS', 20, 'italic'))
example_label = tk.Label(canvas, text='English example', bg=BGCOLORCANVAS, font=('Comic Sans MS', 20, 'bold', 'italic'))

canvas.create_window(200, 150, window=english_label)  # Position (x=200, y=150)
canvas.create_window(200, 250, window=example_label)   # Position (x=200, y=250)

true_image = tk.PhotoImage(file=r"22-German Flash Cards\a.png")
false_image = tk.PhotoImage(file=r"22-German Flash Cards\b.png")


truebutton=tk.Button(image=true_image,width=110,height=90,text='true',command=truebuttonclicked,background=BGCOLORCANVAS,highlightthickness=0)
truebutton.config(padx=5,pady=5)
truebutton.grid(column=1,row=3,sticky='W')


falsebutton=tk.Button(image=false_image,width=110,height=90,text='false',command=wordloop,background=BGCOLORCANVAS,highlightthickness=0)
falsebutton.config(padx=5,pady=5)
falsebutton.grid(column=1,row=3,sticky='E')






#-----------------------------------OPEN FILE ----------------------------------#


with open(r'22-German Flash Cards\a1.json','r', encoding='utf-8') as myfile:
    data=json.load(myfile)
    truebutton.config(state="disabled")
    falsebutton.config(state="disabled")
    wordloop()


def on_closing():
    global ct
    messagebox.showinfo("Closing Application", f'{ct}/50 words guessed correct')
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)


window.mainloop()