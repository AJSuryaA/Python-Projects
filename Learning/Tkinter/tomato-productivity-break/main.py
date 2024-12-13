import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer= None

window= Tk()
window.title("Productivity Timer")
window.config(bg="white")

label = Label(text="Timer", fg=GREEN, bg="White", font=(FONT_NAME, 45 ,"bold"))
label.grid(column= 1,row=0)
mini = 00
sec = 00

canvas= Canvas(width=500, height= 500, bg="White", highlightthickness=0)
png= PhotoImage(file='tomato.png')
canvas.create_image(250, 250, image= png)
timer_text= canvas.create_text(250, 300,text= "00:00", font= (FONT_NAME, 45 ,"bold"), fill="White")
canvas.grid(column= 1,row=1)

rep = 1

def start_timer():
    if rep == 8:
        timer_count(LONG_BREAK_MIN * 60)
        label.config(text="LONG BREAK", fg=GREEN)
    elif rep % 2 == 0 :
        timer_count(SHORT_BREAK_MIN * 60)
        label.config(text="SHORT BREAK", fg=GREEN)
    else:
        timer_count(WORK_MIN * 60)
        label.config(text="WORK", fg=GREEN)

def timer_count(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer= window.after(1000, timer_count, count - 1 )
    else :
        global rep
        rep += 1
        start_timer()

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="WORK", fg=GREEN)


start_button= Button(text="START", highlightthickness= 0, command= start_timer)
start_button.grid(column= 0,row=2,padx=10, pady=10)

reset_button= Button(text="RESET", highlightthickness= 0, command= reset_timer)
reset_button.grid(column= 2,row=2,padx=30, pady=30)

check_mark= Label(text='✔', fg=GREEN, bg="White")
check_mark.grid(column= 1,row=2)
check_mark.config(font= (FONT_NAME, 30 ,"bold"))

window.mainloop()