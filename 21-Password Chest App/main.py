import tkinter as tk
import random
import string
from tkinter import messagebox
import json


BGCOLOR='#F1F2F2'
EMAILLABEL='E-mail/Username'
WEBSITE='Website'
PASS='Password'
GENBUTTON='Generate'
ADD='Add'



# ---------------------------- SEARCH BUTTON  ------------------------------- #

def searchbuttonclicked():
    website=website_text.get("1.0", tk.END).lower()

    try:
        with open("21-Password Chest App\data.json", "r") as my_file:
            data= json.load(my_file)
            email= data[f"{website}"]['email']
            password=data[f"{website}"]['password']
            messagebox.askokcancel(message=f'Your e mail: {email}\nYour password:{password}')
    except FileNotFoundError:
            messagebox.askokcancel(message='There is no such file.')
    except KeyError:
            messagebox.askokcancel(message=f'{website} is not found.')





# ---------------------------- ADD BUTTON  ------------------------------- #
def addbuttonclicked():
     website=website_text.get("1.0", tk.END).lower()
     email=email_text.get("1.0", tk.END).lower()
     password=password_text.get("1.0", tk.END)

     new_json_data={
        website: {'email': email,
                'password':password}}

     message= messagebox.askokcancel(message=f'{WEBSITE}:{website_text.get("1.0", tk.END)}\n{EMAILLABEL}:{email_text.get("1.0", tk.END)}\n{PASS}:{password_text.get("1.0", tk.END)}\nAre these vallues are ok?')
     
     if message:

        try:
            with open("21-Password Chest App\data.json", "r") as my_file:
                data= json.load(my_file)
            #my_file.write(f'{WEBSITE}:{website_text.get("1.0", tk.END)}|||{EMAILLABEL}:{email_text.get("1.0", tk.END)}|||{PASS}:{password_text.get("1.0", tk.END)}\n')
        except FileNotFoundError:
            with open("21-Password Chest App\data.json", "w") as my_file:
                json.dump(new_json_data,my_file)

        else:
            with open("21-Password Chest App\data.json", "w") as my_file:
            #my_file.write(f'{WEBSITE}:{website_text.get("1.0", tk.END)}|||{EMAILLABEL}:{email_text.get("1.0", tk.END)}|||{PASS}:{password_text.get("1.0", tk.END)}\n')
                data.update(new_json_data)
                json.dump(data,my_file,indent=4)




# ---------------------------- GEN PASS SETUP ------------------------------- #

def genpass():
    password = ''
    for _ in range(16):
        number= random.randint(1, 50) 
        password += string.printable[number]
    password_text.delete('1.0', tk.END)
    password_text.insert('1.0', password)   




# ---------------------------- UI SETUP ------------------------------- #

window=tk.Tk()
window.minsize(width=600,height=600)
window.configure(background=BGCOLOR)
window.title('Password Chest')
window.config(pady=30,padx=30)

canvas=tk.Canvas(width=300,height=300)
photochest=tk.PhotoImage(file=r'C:\Users\snrpc\Desktop\Python\21-Password Chest App\4.png')
canvas.create_image(150,150,image=photochest)
canvas.grid(column=1,row=0)

# ---------------------------- MAIL SETUP ------------------------------- #

email_label=tk.Label(width=15, height=2, text=EMAILLABEL , font=('Adorno' , 10  , 'bold') )
email_label.grid(column=0,row=1)

email_text=tk.Text(width=60, height=1, font=('Adorno' , 10  , 'normal') )
email_text.focus()
email_text.grid(column=1,row=1)
email_text.insert('1.0', "example@gmail.com")

# ---------------------------- WEBSITE SETUP ------------------------------- #

website_label=tk.Label(width=7, height=2 , text=WEBSITE , font=('Adorno' , 10  , 'bold') )
website_label.grid(column=0,row=2)

website_text=tk.Text(width=50, height=1, font=('Adorno' , 10  , 'normal') )
website_text.grid(column=1,row=2,sticky="w")

# ---------------------------- PASS SETUP ------------------------------- #

password_label=tk.Label(width=8, height=2 , text=PASS , font=('Adorno' , 10  , 'bold') )
password_label.grid(column=0,row=3)

password_text=tk.Text(width=50, height=1, font=('Adorno' , 10  , 'normal') )
password_text.grid(column=1,row=3,sticky="w")


# ---------------------------- PASS GENERATE SETUP ------------------------------- #

generatebutton=tk.Button(width=8, height=2 , text=GENBUTTON , font=('Adorno' , 8  , 'bold'),command=genpass)
generatebutton.grid(column=1,row=3,sticky="E")


# ---------------------------- ADD BUTTON SETUP ------------------------------- #


addbutton=tk.Button(width=30, height=2 , text=ADD , font=('Adorno' , 10  , 'bold'), command=addbuttonclicked) 
addbutton.grid(column=0,row=5,columnspan=3)


# ---------------------------- SEARCH BUTTON SETUP ------------------------------- #
searchbutton=tk.Button(width=8, height=2 , text='Search' , font=('Adorno' , 9  , 'bold'), command=searchbuttonclicked) 
searchbutton.grid(column=1,row=2,sticky="E")


window.mainloop()
