from tkinter import *
import pandas as pd
import random

# --- GET THE DATA ---
try:
    # Open the saved file (already played)
    saved_data = pd.read_csv("data/words_toLearn.csv")
except FileNotFoundError:
    # Open the original file (first time)
    original_data = pd.read_csv("data/Deu_Eng_words.csv")
    to_learn_words = original_data.to_dict(orient="records")
else:
    # Convert the data into a dictionary
    to_learn_words = saved_data.to_dict(orient="records")

# --- VARIABLES ---
original_lang = "English"
learning_lang = "Deutch"
current_word = {}


# --- CREATE FUNCTIONS ---
def update_card():
    global current_word, timer
    # Cancel the timer
    rt.after_cancel(timer)
    # Get a random word (deutch-english)
    current_word = random.choice(to_learn_words)
    # Update the card texts and image
    card.itemconfig(language, text=learning_lang, fill="black")
    card.itemconfig(word, text=current_word[learning_lang], fill="black")
    card.itemconfig(img_background, image=img_front)
    # Restart the timer to 3 seconds
    timer = rt.after(ms=3000, func=flip_card)


def flip_card():
    # Show the translation and change the image
    card.itemconfig(language, text=original_lang, fill="white")
    card.itemconfig(word, text=current_word[original_lang], fill="white")
    card.itemconfig(img_background, image=img_back)


def remove_word():
    global to_learn_words
    # Remove the word from the dictionary
    del to_learn_words[to_learn_words.index(current_word)]
    # Create a file with the words to learn
    dt = pd.DataFrame(to_learn_words)
    # "index" removes the column of automatic numbers
    dt.to_csv("data/words_toLearn.csv", index=False)
    update_card()


# --- USER INTERFACE (GUI) ---
rt = Tk()
rt.title("Flash Card Learning")
rt.geometry("1000x800")
rt.resizable(width=False, height=False)
rt.config(padx=50, pady=50, background="#B1DDC6")
timer = rt.after(ms=3000, func=flip_card)

# Create the card
img_front = PhotoImage(file="./imgs/card_front.png")
img_back = PhotoImage(file="./imgs/card_back.png")
card = Canvas(width=900, height=600, background="#B1DDC6", highlightthickness=0)
img_background = card.create_image(450, 270, image=img_front)
language = card.create_text(450, 150, text=learning_lang, font=("Arial", "40", "italic"))
word = card.create_text(450, 320, text="Hallo", font=("Arial", "60", "bold"))
card.grid(row=0, column=0, columnspan=2)

# Create the buttons
img1 = PhotoImage(file="./imgs/wrong.png")
wrong_btn = Button(image=img1, highlightthickness=0, command=update_card)
wrong_btn.grid(row=1, column=0)
img2 = PhotoImage(file="./imgs/right.png")
correct_btn = Button(image=img2, highlightthickness=0, command=remove_word)
correct_btn.grid(row=1, column=1)

# First card
update_card()

rt.mainloop()
