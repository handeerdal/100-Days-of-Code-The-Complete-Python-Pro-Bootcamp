
import tkinter as tk
import time
import datetime
# ---------------------------- CONSTANTS ------------------------------- #
BG='#FBF4DB'
TEXTCOLOR='black'


reps=0
timer=None
timer_active = False
# ---------------------------- TIMER RESET ------------------------------- #


def resettimer():
     global timer,timer_active
     if timer is not None:
        window.after_cancel(timer)
        timer=None
     text_var.set('POMODORO')
     canvas.itemconfig(texttime, text='00:00')
     text_checkmark.set('')
     global reps
     reps=0
     timer_active = False 

     



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def callcountdown():
         global timer_active
         if not timer_active:  # Start the timer only if it's not already active
            timer_active = True
            countdown(5)


def countdown(count):
    global timer_active
    if not timer_active:  # Exit if the timer has been reset
        return
    global reps

    if count>=0 and reps%2==0: 
          minutes, seconds = divmod(count, 60)
          text_var.set('POMODORO')
          canvas.itemconfig(texttime, text=f"{minutes:02}:{seconds:02}")
          window.after(1000,countdown,count-1)
          if count==0:
               reps+=1
               countdown(2)

    elif  count>=0 and reps%2==1:
          minutes, seconds = divmod(count, 60)
          text_var.set('BREAK')
          canvas.itemconfig(texttime, text=f"{minutes:02}:{seconds:02}")
          global timer
          timer= window.after(1000,countdown,count-1)
          if count==0:
               if reps!=7:
                   reps+=1
                   text_checkmark.set('✔️'*((reps+1)//2))
                   countdown(5)

               elif reps==7:
                    text_var.set('You reached your goal today')
                    text_checkmark.set('✔️'*((reps+1)//2))
                    timer_active = False 
                
                




# ---------------------------- UI SETUP ------------------------------- #

window=tk.Tk()
window.minsize(width=600,height=600)
window.configure(background=BG)
window.title('♥Pomodoro App♥')
window.config(pady=30,padx=30)

text_var = tk.StringVar()
text_var.set('POMODORO')
label = tk.Label(textvariable=text_var, fg=TEXTCOLOR,bg=BG, font=('Lucida Handwriting' ,20, 'bold'))
label.grid(column=1,row=0)





canvas=tk.Canvas(width=712,height=512,bd=0,highlightthickness=0, relief='ridge')
photo_tomato=tk.PhotoImage(file=r'C:\Users\snrpc\Desktop\Python\20-Pomodoro App\1.png')
canvas.create_image(256,256,image=photo_tomato)
canvas.configure(background=BG)
texttime=canvas.create_text(550, 279, text='00:00', fill=TEXTCOLOR, font=('Helvetica 30 bold'))
canvas.grid(column=1,row=1)


startbutton=tk.Button(text='Start',width=10,height=3,background=BG,highlightthickness=0,relief='ridge',command=callcountdown)
startbutton.grid(column=0,row=3)

stopbutton=tk.Button(text='Reset',width=10,height=3,background=BG,highlightthickness=0,relief='ridge',command=resettimer)
stopbutton.grid(column=2,row=3)


text_checkmark = tk.StringVar()
text_checkmark.set('')
checkmark=tk.Label(textvariable=text_checkmark, fg='green',bg=BG, font=('Lucida Handwriting' ,15, 'bold'))
checkmark.grid(column=1,row=4)



window.mainloop()