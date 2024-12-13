import tkinter
from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button
from generate_password import Generate_password

window= Tk()
window.title("Password Manager")
window.minsize(width= 400, height=400)
window.config(padx= 40, pady= 40)

canvas= Canvas(width=360, height= 360,  highlightthickness=0)
img= PhotoImage(file= 'img.png')
canvas.create_image(190,180,image= img)
canvas.grid(column= 0,row=0, columnspan= 3)

password= Generate_password()
# passw= None
def generate():
    # global passw
    passw= password.generate()
    password_input.insert(index=0, string=f"{passw}")

def save_data():
    if website_input.get() == "":
        website_input.insert(index=0,string="Enter website to continue")
    elif password_input.get() == "":
        password_input.insert(index=0,string="Enter or generate password to continue")
    else:
        with open("data.txt", "a") as data_text:
            data_text.write(f"{website_input.get()}|{email_input.get()}|{password_input.get()}"+"\n")
        website_input.delete(0,tkinter.END)
        password_input.delete(0, tkinter.END)

label_website= Label(text= "Website :", font= ("Arial ", 12 ,"bold"))
label_website.grid(column= 0,row=1, padx= 20, pady= 5)

label_email= Label(text= "Email/Username :", font= ("Arial ", 12 ,"bold"))
label_email.grid(column= 0,row=2, padx= 20, pady= 5)

label_password= Label(text= "Password :", font= ("Arial ", 12 ,"bold"))
label_password.grid(column= 0,row=3, padx= 20, pady= 5)

website_input= Entry(width= 70 , highlightcolor= "Green" , highlightthickness= 2)
website_input.grid(column= 1, row= 1, columnspan= 2)

email_input= Entry(width= 70 , highlightcolor= "Green" , highlightthickness= 2)
email_input.grid(column= 1, row= 2, columnspan= 2)
email_input.insert(index= 0, string="surya.2003amuari@gmail.com")

password_input= Entry(width= 30 , highlightcolor= "Green", highlightthickness= 2)
password_input.grid(column= 1, row= 3)

add_button= Button(text= "Add", width= 42, font= ("Arial ", 12 ,"bold"), command= save_data)
add_button.grid(column= 1, row= 4, columnspan= 2, padx= 20, pady= 5)

generate_button= Button(text= "Generate Password", width= 19, font= ("Arial ", 12 ,"bold"), command=generate)
generate_button.grid(column= 2, row= 3, columnspan= 2, padx= 20, pady= 5)

window.mainloop()