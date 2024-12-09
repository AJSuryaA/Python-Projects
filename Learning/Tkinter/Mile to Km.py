from cProfile import label
from tkinter import *

window = Tk()
window.title("Km To Mile")
window.minsize(width= 400 , height= 600)

input = Entry(width= 10 , highlightcolor="Green" , highlightthickness=2)
input.grid(column= 1, row= 0)

label1 = Label(text= "is equal to", font= ("Arial ", 16 ,"normal"))
label1.grid(column= 0, row= 1)

def calculate():
    pass

button = Button(text= "Calculate", command=calculate)
window.mainloop()
