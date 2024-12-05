import tkinter

window=tkinter.Tk()
window.title('My new window')
window.minsize(width=300,height=300)
mylabel=tkinter.Label(text='my label',font=('Arial',24,'italic'))
def buttonclicked():
    mylabel.config(text='hello')
    print(myinput.get())

myinput=tkinter.Entry()
mybutton=tkinter.Button(text='my button',command=buttonclicked)

newbutton=tkinter.Button(text='new button')

mylabel.grid(column=0,row=0)
newbutton.grid(column=3,row=0)

mybutton.grid(column=1,row=1)
myinput.grid(column=4,row=4)








window.mainloop()

