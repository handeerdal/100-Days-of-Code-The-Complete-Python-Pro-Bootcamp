from tkinter import *
import requests

def get_quote():
    respond=requests.get('https://dummyjson.com/quotes/random')
    data=respond.json()
    quote=data['quote']
    canvas.itemconfig(quote_text,text=quote)



window = Tk()
window.title("Believe in Yourself...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=r"25-Quote Generator\background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Believe in Yourself....", width=250, font=("Arial", 15, "bold"), fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=r"25-Quote Generator\believe.png")
kanye_button = Button(image=kanye_img, highlightthickness=0,command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()