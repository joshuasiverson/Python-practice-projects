from tkinter import *
from random import randint
import pandas

BACKGROUND_COLOR = "#B1DDC6"
card_counter = 0
word_index = 0


# ---------------------------- Functions ------------------------------- #
# show back of the card aka 'card2'
def flip_card():
    translation = word_dict[word_index][n_lang]
    card.itemconfig(card_image, image=card_back)
    card.itemconfig(language, text=n_lang, fill='white')
    card.itemconfig(foreign_word, text=translation, fill='white')


def get_new_card():
    global word_index, word
    word_index = randint(0, bank_len)
    word = word_dict[word_index][f_lang]
    card.itemconfig(card_image, image=card_front)
    card.itemconfig(language, text=f_lang, fill='black')
    card.itemconfig(foreign_word, text=word, fill='black')


def right_answer():
    global bank_len, flip_timer
    window.after_cancel(flip_timer)
    bank_len -= 1
    del word_dict[word_index]
    get_new_card()
    words_to_learn = pandas.DataFrame(word_dict)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    flip_timer = window.after(3000, func=flip_card)


def wrong_answer():
    global word_index, flip_timer
    window.after_cancel(flip_timer)
    get_new_card()
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- Word Bank ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/QuestionableKanjiTranslations.csv")
word_bank = pandas.DataFrame(data)
df_col = word_bank.columns
f_lang = df_col[0]
n_lang = df_col[1]
word_dict = word_bank.to_dict(orient='records')
bank_len = len(word_dict)-1
word_index = randint(0, bank_len)
word = word_dict[word_index][f_lang]

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Kanji flashcards")
window.minsize(height=550, width=800)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
card_image = card.create_image(400, 263, image=card_front)
language = card.create_text(400, 150, text=f_lang, font=("Arial", 40, "italic"))
foreign_word = card.create_text(400, 263, text=word, font=("Arial", 60, "bold"))
card.grid(row=0, column=0, columnspan=2)

check = PhotoImage(file="images/right.png")
correct = Button(image=check, highlightthickness=0, command=right_answer)
correct.grid(row=1, column=1)

ex = PhotoImage(file="images/wrong.png")
wrong = Button(image=ex, highlightthickness=0, command=wrong_answer)
wrong.grid(row=1, column=0)

flip_timer = window.after(3000, func=flip_card)

window.mainloop()
