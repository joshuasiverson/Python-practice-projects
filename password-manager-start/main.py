from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = ''.join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = web_entry.get()
    email = email_entry.get()
    pw = pass_entry.get()
    new_data = {
        site: {
            "email": email,
            "password": pw
        }
    }
    if site == '' or email == '' or pw == '':
        messagebox.showerror(title="Missing Fields", message="Fill out all fields dummy")
    else:
        try:
            with open("punchtheprimeminister.json", 'r') as data_file:
                pw_data = json.load(data_file)  # read old data

        except FileNotFoundError:
            with open("punchtheprimeminister.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            pw_data.update(new_data)  # update said data
            with open("punchtheprimeminister.json", 'w') as data_file2:
                json.dump(pw_data, data_file2, indent=4)  # save updates
        finally:
            web_entry.delete(0, 'end')
            # email_entry.delete(0, 'end')
            pass_entry.delete(0, 'end')


# ---------------------------- Search ------------------------------- #
def search():
    site = web_entry.get()
    try:
        with open("punchtheprimeminister.json", 'r') as data_file:
            pw_data = json.load(data_file)  # read old data
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if site in pw_data:
            messagebox.showinfo(title=site, message=f"Email: {pw_data[site]['email']}"
                                                    f"\nPassword: {pw_data[site]['password']}")
        else:
            messagebox.showinfo(title=site, message="No details for that website exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:")
web_entry = Entry(width=26)
web_label.grid(row=1, column=0)
web_entry.grid(row=1, column=1)

email_label = Label(text="Email/Username:")
email_entry = Entry(width=45)
email_entry.insert(0, "joshuasiverson@gmail.com")
email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1, columnspan=2)

pass_label = Label(text="Password:")
pass_entry = Entry(width=26)
pass_label.grid(row=3, column=0)
pass_entry.grid(row=3, column=1)

pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=40, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)

window.mainloop()
