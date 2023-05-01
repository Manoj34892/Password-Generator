from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
def save():
    website = w_e.get()
    email = e_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        show = messagebox.showerror(title='Check Details', message="Please fill the Details")
    else:
        is_ok = messagebox.askokcancel(title="Check Details" , message= f" Here is your Final Details\n Webesite :{website}\n "
                                                                f"Email : {email}\n Password:{password}")
        if is_ok :
            with open("data.txt","a") as your_data:
                your_data.write(f"{website} | {email} | {password}\n")
                w_e.delete(0,END)
                password_entry.delete(0,END)
                e_entry.delete(0,END)

#PAssword Genrator
def generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_pass = [choice(letters) for  _ in range(randint(8,12))]
    number_pass = [choice(numbers) for _ in  range(randint(2,4))]
    symbols_pass = [choice(symbols) for _ in range(randint(2,4))]

    main_password = letter_pass + number_pass + symbols_pass

    shuffle(main_password)
    final_password = "".join(main_password)
    password_entry.insert(0,final_password)


window =Tk()
window.title("Password Generator")
# window.size(width = 300,height = 300)
window.config(padx = 20,pady =20)

canvas = Canvas(height=200,width=200)
lock_image = PhotoImage(file="logo.png")
logo = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(row=0,column=1)
#labels
w = Label(text = "Website")
w.grid(column=0,row=1,columnspan=1)
email = Label(text= "Email/Username")
email.grid(column=0,row=2,columnspan=1)
pswrd = Label(text = "Password")
pswrd.grid(column = 0, row =3)


#entries
w_e = Entry(width=35)
w_e.grid(column=1,row=1,columnspan=2)
w_e.focus()
e_entry = Entry(width=35)
e_entry.grid(column=1,row=2,columnspan=2)

password_entry = Entry(width=25)
password_entry.grid(column=1,row=3,)

#BUttons
gp = Button(text="Generate Password" ,command=generate)
gp.grid(column=2,row=3,)

add = Button(text = 'ADD',width= 35,command= save)
add.grid(column= 1,row = 4,columnspan=2)




window.mainloop()

