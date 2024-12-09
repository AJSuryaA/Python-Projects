import tkinter

window = tkinter.Tk() # window
window.title("My First GUI Program") # title of window
window.minsize(width= 500, height= 300) # window size

label = tkinter.Label(text= "Label", font= ("Arial ", 24 ,"bold"))
label.grid(row = 0 , column = 0)

# label["text"] = "New_text"
# label.config(text="new_text")

def button_clicked():
    n_input = input.get()
    label.config(text=n_input)

button = tkinter.Button(text="click me", command=button_clicked)
button.grid(row = 1 , column = 1)


button1 = tkinter.Button(text="click me", command=button_clicked)
button1.grid(row = 0 , column = 3)


input = tkinter.Entry(width=10,highlightcolor="Green" , highlightthickness=2 )
input.grid(row = 4 , column = 4)



window.mainloop()