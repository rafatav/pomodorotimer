from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checks = ""
global_timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global checks
    global reps
    window.after_cancel(global_timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checks = ""
    check_label.config(text=checks)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer = LONG_BREAK_MIN
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        timer = SHORT_BREAK_MIN
        timer_label.config(text="Break", fg=PINK)
    else:
        timer = WORK_MIN
        timer_label.config(text="Work", fg=GREEN)
    count_down(timer * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global checks
    count_min = int(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global global_timer
        global_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checks += "✔"
            check_label.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(background=YELLOW, padx=100, pady=50)

timer_label = Label(text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

check_label = Label(foreground=GREEN, background=YELLOW, font=35)
check_label.grid(column=1, row=3)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

pomodoro_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="White")
canvas.grid(column=1, row=1)

window.mainloop()
