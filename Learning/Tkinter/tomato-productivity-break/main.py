from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window= Tk()
window.title("Productivity Timer")
window.config(bg="white")

label = Label(text="Timer", fg=GREEN, bg="White", font=(FONT_NAME, 45 ,"bold"))
label.grid(column= 1,row=0)

canvas= Canvas(width=500, height= 500, bg="White", highlightthickness=0)
png= PhotoImage(file='tomato.png')
canvas.create_image(250, 250, image= png)
canvas.create_text(250, 300,text= "00:00", font= (FONT_NAME, 45 ,"bold"), fill="White")
canvas.grid(column= 1,row=1)

window.mainloop()