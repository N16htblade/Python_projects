from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pyperclip

PROJECT_PATH = "C:/PyLearning/projects/Day 29 + Day 30 Password Manager/"

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# --------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice( letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = web_entry.get()
    username = email_entry.get()
    password = pass_entry.get()
    new_data = {website: {
                    "email": username,
                    "password": password}}

    if len(website) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open (f"{PROJECT_PATH}data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open (f"{PROJECT_PATH}data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open(f"{PROJECT_PATH}data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- SEARCH --------------------------------- #
def search_for_mail():
    try:
        with open (f"{PROJECT_PATH}data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No entries saved yet")
    else:
        website = web_entry.get()
        if website in data:
            lost_password = data[website]["password"]
            username = data[website]["email"]
            messagebox.showinfo(title="Search", message=f"Username: {username}\n"
                                                    f"Password: {lost_password}")
        else:
            messagebox.showerror(title="Entry not found", message="Sorry, entry does not exist.")

# ---------------------------- UI SETUP ------------------------------- #
#Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Canvas
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="C:\PyLearning\projects\Day 29 + Day 30 Password Manager\logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

#Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1, sticky="e")
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky='e')
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3, sticky='e')

#Entry
web_entry = Entry(width=30)
web_entry.grid(column=1, row=1, sticky="w")
web_entry.focus()
email_entry = Entry(width=53)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0, "random@gmail.com")
pass_entry = Entry(width=30)
pass_entry.grid(column=1, row=3, sticky="w")

#Buttons
search_button = Button(text="Search", width=15, command=search_for_mail)
search_button.grid(column=2, row=1, sticky="w")
generate_pass_button = Button(text="Generate Password", width=15, command=generate_password)
generate_pass_button.grid(column=2, row=3, sticky="w")
add_button = Button(text="Add", width=44, command=save_to_file)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()