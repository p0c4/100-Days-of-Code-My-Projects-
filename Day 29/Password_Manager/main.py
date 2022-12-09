from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)  # clipboard password

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = entry_website.get()
    e_mail = entry_username.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0 :
        messagebox.showinfo(title="oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {e_mail} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {e_mail} | {password}\n")
                entry_website.delete(0, END)
                entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

# Canvas
canvas =Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Labels
lable_website = Label(text="Website")
lable_website.grid(column=0, row=1)

lable_username = Label(text="Email/Username")
lable_username.grid(column=0, row=2)

lable_password = Label(text="Password")
lable_password.grid(column=0, row=3)

# Buttons

button_generate_password = Button(text="Generate Password",width=16, command=generate_password)
button_generate_password.grid(row=3, column=2,columnspan=2, sticky="w")

button_add = Button(text="Add", width=51, command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="w")

# Entries

entry_website = Entry(width=60)
entry_website.grid(column=1, row=1, columnspan=2, sticky="w")
entry_website.focus()  # Focus on this entry, cursor ready.

entry_username = Entry(width=60)
entry_username.grid(column=1, row=2, columnspan=2, sticky="w")
entry_username.insert(0, "p0c4")  # Fill the entry box with predefined username or e-mail, starting from 1st char.

entry_password = Entry(width=38)
entry_password.grid(column=1, row=3, sticky="w")

window.mainloop()
