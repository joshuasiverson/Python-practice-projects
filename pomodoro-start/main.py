from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #
def rest_timer():
    window.after_cancel(TIMER)
    time_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer, text="00:00")
    checkmark.config(text='')
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 2 == 1:
        countdown(work_sec)
        time_label.config(text="Work", fg=GREEN)
    elif REPS % 8 == 0:
        countdown(long_break_sec)
        time_label.config(text="Break", fg=RED)
    else:
        countdown(short_break_sec)
        time_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ''
        for x in range(math.floor(REPS / 2)):
            mark += '✔'
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

time_label = Label(text="Timer", font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
time_label.grid(column=1, row=0)
start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", command=rest_timer)
reset.grid(column=2, row=2)

checkmark = Label(text='', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, 'bold'))
checkmark.grid(column=1, row=3)

window.mainloop()
