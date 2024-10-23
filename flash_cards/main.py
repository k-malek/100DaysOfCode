import tkinter as tk
from PIL import ImageTk,Image
from card import Card

# ---------------------------- FlashCard handling ------------------------------- #

FILE='french_words.csv'
CARDSET=Card.get_set(FILE)


def update_ui_data(card):
    side,word = card.get_set()
    canvas.itemconfig(language_label,text=Card.subjects[side])
    canvas.itemconfig(word_label,text=word)
    canvas.itemconfig(card_bg,image=card_images[side])

def update_card_data(card,answer):
    card.last_answer=answer
    choose_new_card()

def choose_new_card():
    global curr_card
    curr_card=Card.choose_new_card()
    update_ui_data(curr_card)

def flip_card():
    curr_card.flip_card()
    update_ui_data(curr_card)

# ---------------------------- UI SETUP ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

# Main window
window = tk.Tk()
window.title("Flashy")
window.configure(padx=50,pady=50,bg=BACKGROUND_COLOR)

# Images

card_images = {'front':ImageTk.PhotoImage(Image.open("images/card_front.png")),
               'back':ImageTk.PhotoImage(Image.open("images/card_back.png"))}
right_image = ImageTk.PhotoImage(Image.open("images/right.png"))
wrong_image = ImageTk.PhotoImage(Image.open("images/wrong.png"))

# Canvas with image
canvas=tk.Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)

canvas.bind("<Button-1>", lambda x: flip_card())

card_bg=canvas.create_image(400,263,image=card_images['front'])
language_label=canvas.create_text(400,150,font=("Ariel",40,"italic"))
word_label=canvas.create_text(400,263,font=("Ariel",60,"bold"))

# Buttons

right_button=tk.Button(image=right_image, highlightthickness = 0, bd = 0, command=lambda:update_card_data(curr_card,'correct'))
wrong_button=tk.Button(image=wrong_image, highlightthickness = 0, bd = 0, command=lambda:update_card_data(curr_card,'wrong'))

# UI elements positioning

canvas.grid(row=0,column=0,columnspan=2)
right_button.grid(row=1,column=0)
wrong_button.grid(row=1,column=1)

# ---------------------------- Prepare and run program ------------------------------- #

curr_card=None
choose_new_card()

window.mainloop()


