import random
import pyperclip
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image,ImageTk
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_list = []
    password_list+= [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list+= [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list+= [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password=''.join(password_list)

    password_var.set(password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    if not website_var.get() or not user_var.get() or not password_var.get():
        messagebox.showerror(title="Empty data",message="Make sure to fill all the fields!")
    else:
        with open("pass.txt","a+",encoding="utf-8") as f:
            f.write(f'{website_var.get()}/{user_var.get()}/{password_var.get()}\n')
            website_var.set('')
            password_var.set('')

        messagebox.showinfo(title="Success", message="Your password has been stored in a super secret place!")
    

# ---------------------------- UI SETUP ------------------------------- #

# Main window
window = tk.Tk()
window.title("Password manager")
window.configure(padx=50,pady=50,bg="white")

# Canvas with image
canvas=tk.Canvas(width=200,height=200,bg="white",highlightthickness=0)
logo_img = ImageTk.PhotoImage(Image.open("logo.png"))
canvas.create_image(100,100,image=logo_img)

# Labels

website_label=ttk.Label(text="Website:",background="white")
user_label=ttk.Label(text="Email/Username:",background="white")
password_label=ttk.Label(text="Password:",background="white")

# Variables for entries

website_var=tk.StringVar()
user_var=tk.StringVar(value="k_m781235@oijudas.hr") # Prepopulated email value
password_var=tk.StringVar()

# Entries

website_input=ttk.Entry(width=51,textvariable=website_var)
user_input=ttk.Entry(width=51,textvariable=user_var)
password_input=ttk.Entry(width=32,textvariable=password_var)
website_input.focus()

# Buttons

gen_pass_button=ttk.Button(width=17,text="Generate password",command=generate_password)
add_button=ttk.Button(width=51,text="Add",command=save_data)


# UI elements positioning

canvas.grid(row=0,column=1)
website_label.grid(row=1,column=0, sticky="e")
user_label.grid(row=2,column=0, sticky="e")
password_label.grid(row=3,column=0, sticky="e")
website_input.grid(row=1,column=1,columnspan=2, sticky="w")
user_input.grid(row=2,column=1,columnspan=2, sticky="w")
password_input.grid(row=3,column=1, sticky="w")
gen_pass_button.grid(row=3,column=2, sticky="w")
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()