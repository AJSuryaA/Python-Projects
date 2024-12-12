from tkinter import *

window = Tk()
window.title("Length Unit Converter")
window.minsize(width= 300 , height= 150)

input = Entry(width= 10 , highlightcolor="Green" , highlightthickness=2)
input.grid(column= 0, row= 1,padx=10, pady=10)

label1 = Label(text= "=", font= ("Arial ", 16 ,"normal"))
label1.grid(column= 1, row= 1,padx=10, pady=10)

display_output= Label(text="0",font= ("Arial ", 16 ,"normal"))
display_output.grid(column= 2, row= 1,padx=10, pady=10)

def calculate():
    unit_1 = selected_option1.get()
    unit_2 = selected_option2.get()
    ip = input.get()
    if unit_1 != 'unit' and unit_2 != 'unit' and ip.strip() != "":
        output = factor[unit_1][unit_2] * float(ip)
        display_output.config(text=f"{output}")
        display_output.grid(column= 2, row= 1,padx=10, pady=10)
    else:
        # error = Label(text="fill all requisites",font= ("Arial ", 10 ,"normal"))
        display_output.config(text="fill all requisites",font= ("Arial ", 10 ,"normal"))
        display_output.grid(column=2, row=1,padx=10, pady=10)



button = Button(text= "Calculate", command=calculate)
button.grid(column=1,row=3,padx=10, pady=10)


factor = {
    "Miles": {"Miles": 1, "Km": 1.60934, "m": 1609.34, "cm": 160934, "mm": 1609340},
    "Km": {"Miles": 0.621371, "Km": 1, "m": 1000, "cm": 100000, "mm": 1000000},
    "m": {"Miles": 0.000621371, "Km": 0.001, "m": 1, "cm": 100, "mm": 1000},
    "cm": {"Miles": 6.2137e-6, "Km": 1e-5, "m": 0.01, "cm": 1, "mm": 10},
    "mm": {"Miles": 6.2137e-7, "Km": 1e-6, "m": 0.001, "cm": 0.1, "mm": 1}
}

options = ["Miles", "Km", "m", "cm", "mm"]

selected_option1 = StringVar()
selected_option1.set("unit")  # Set the default value

# Create the dropdown menu
dropdown_q = OptionMenu(window, selected_option1, *options)
dropdown_q.config(width=10)  # Set width for consistency
dropdown_q.grid(column=0, row=2, padx=10, pady=10)

selected_option2 = StringVar()
selected_option2.set("unit")  # Set the default value

# Create the dropdown menu
dropdown_r = OptionMenu(window, selected_option2, *options)
dropdown_r.config(width=10)  # Set width for consistency
dropdown_r.grid(column=2, row=2, padx=10, pady=10)

window.mainloop()
