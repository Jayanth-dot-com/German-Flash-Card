from pandas import *
from tkinter import *
from random import randint

VALUE = {}

with open("<ENTER YOUR DATA FILE LOCATION>") as data:
    words = read_csv(data)
    dictionary = words.to_dict(orient="records")

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background="#B1DDC6")

def card():
    global VALUE
    VALUE = dictionary[randint(0, len(dictionary)-1)]
    canvas.itemconfig(page, image=white_square)
    canvas.itemconfig(title, text="German")
    canvas.itemconfig(text, text=VALUE["German"])
    window.after(5000, flip_card)
def correct():
    dictionary.remove(VALUE)
    card()
def wrong():
    card()
def flip_card():
    canvas.itemconfig(page, image=green_square)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(text, text=VALUE["English"])

canvas = Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)

white_square = PhotoImage(file="<ENTER YOUR IMAGE LOCATION>")
green_square = PhotoImage(file="<ENTER YOUR IMAGE LOCATION>")
correct_button = PhotoImage(file="<ENTER YOUR IMAGE LOCATION>")
incorrect_button = PhotoImage(file="<ENTER YOUR IMAGE LOCATION>")
# beginning_button = PhotoImage(file="play.png")

page = canvas.create_image(400, 263, image=white_square)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(columnspan=2, column=0, row=0)

right_button = Button(image=correct_button, highlightthickness=0, background="#B1DDC6", command=correct)
wrong_button = Button(image=incorrect_button, highlightthickness=0, background="#B1DDC6", command=wrong)
# start_button = Button(image=beginning_button, highlightthickness=0, background="#B1DDC6")

right_button.grid(column=0, row=1)
wrong_button.grid(column=1, row=1)
# start_button.grid(column=0, row=1, columnspan=2)

card()

mainloop()