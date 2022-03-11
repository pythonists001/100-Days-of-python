from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#ffffff"
FONT_NAME = "Courier"

# --------------------------------PASSWORD GENERATOR ------------------------------#
#Password Generator Project
#Password Generator Project
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ------------------------------SAVE PASSWORD ------------------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200,bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="Day 29 - Building a Password Manager GUI App with Tkinter/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1,row=0)

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email}"
                                f"\nPassword:{password} \nIs it ok to save?")
        if is_ok:
            with open('./Day 29 - Building a Password Manager GUI App with Tkinter/data.txt', mode="a") as file: ##mode a as append
                
                file.write(f"{website} | {email} | {password}\n")
                
                website_entry.delete(0,END)
                password_entry.delete(0,END)

#Labels
website_label = Label(text="Website:", bg=WHITE)
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg=WHITE)
email_label.grid(row=2, column=0)

passsword_label = Label(text="Password:",bg=WHITE)
passsword_label.grid(row=3, column=0)


#Enteries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0, "arvindsingh.cs@hotmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)


#generate buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add",width=36, command=save)
add_button.grid(row=4,column=1, columnspan=2)



   

window.mainloop()
