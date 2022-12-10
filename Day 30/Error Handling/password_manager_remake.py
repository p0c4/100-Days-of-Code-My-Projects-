import json
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
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    e_mail = entry_username.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": e_mail,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data:
                # Reading old data
                data_file = json.load(data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            # updating old data with new data
            data_file.update(new_data)
            with open("data.json", "w") as data:
                # Saving updated data
                json.dump(new_data, data, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = entry_website.get()
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            username = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"username: {username} \npassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} info found.")
    finally:
        entry_website.delete(0, END)
        entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

# Canvas
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website")
label_website.grid(column=0, row=1)

label_username = Label(text="Email/Username")
label_username.grid(column=0, row=2)

label_password = Label(text="Password")
label_password.grid(column=0, row=3)

# Buttons

button_generate_password = Button(text="Generate Password", width=16, command=generate_password)
button_generate_password.grid(row=3, column=2, columnspan=2, sticky="w")

button_add = Button(text="Add", width=51, command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="w")

button_search = Button(text="Search", width=16, command=search)
button_search.grid(row=1, column=2, columnspan=2, sticky="w")

# Entries

entry_website = Entry(width=38)
entry_website.grid(column=1, row=1, columnspan=2, sticky="w")
entry_website.focus()  # Focus on this entry, cursor ready.

entry_username = Entry(width=60)
entry_username.grid(column=1, row=2, columnspan=2, sticky="w")
entry_username.insert(0, "p0c4")  # Fill the entry box with predefined username or e-mail, starting from 1st char.

entry_password = Entry(width=38)
entry_password.grid(column=1, row=3, sticky="w")

window.mainloop()
