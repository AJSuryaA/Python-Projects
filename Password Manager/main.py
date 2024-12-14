import tkinter
from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button , messagebox
import pyperclip, json

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


def generate():
    passw= password.generate()
    password_input.insert(index=0, string=f"{passw}")

def save_data():
    if website_input.get() == "":
        website_input.insert(index=0,string="Enter website to continue")
        messagebox.askokcancel(title= "Warning", message= "enter all requisites to save")

    elif password_input.get() == "":
        password_input.insert(index=0,string="Enter or generate password to continue")
        messagebox.askokcancel(title= "Warning", message= "enter all requisites to save")
    else:
        web = website_input.get().title()
        email = email_input.get()
        p = password_input.get()
        pass_dict = {
            web: {
                "email": email,
                "password": p
            }
        }
        isok= messagebox.askokcancel(title="Warning", message=f"check the details you enter\n website :"
                            f"{website_input.get()} \n email : {email_input.get()} \n password : "
                                                              f"{password_input.get()} is it ok to save ")
        if isok:
            try:
                with open(file="data.json", mode="r") as file:
                    data= json.load(fp=file)
            except FileNotFoundError:
                with open(file= "data.json", mode="w") as file:
                    json.dump(obj= pass_dict, fp= file, indent= 4)
            else:
                data.update(pass_dict)
                with open(file= "data.json", mode="w") as file:
                    json.dump(obj= data, fp= file, indent= 4)
            finally:
                website_input.delete(0,tkinter.END)
                password_input.delete(0, tkinter.END)
                oktocopy= messagebox.askokcancel(title="Warning", message="click ''ok'' to copy password to clipboard")
                if oktocopy:
                    pyperclip.copy(p)

def search_password():
    website_looking= website_input.get().title()
    if website_looking != "":
        try:
            with open(file="data.json", mode="r") as file:
                data= json.load(fp=file)
        except FileNotFoundError:
            messagebox.showinfo(title="Warning", message= "No Data File Found")
        else:
            if website_looking in data:
                email= data[website_looking]["email"]
                password1= data[website_looking]["password"]
                askok= messagebox.askokcancel(title= "Search Result", message= f"email : {email} \n password : {password1}"
                                                                     f"\nClick ''ok'' to copy password")
                if askok:
                    pyperclip.copy(password1)
                    website_input.delete(0,tkinter.END)
            else:
                messagebox.showinfo(title="Warning", message= "No Data Found")
    else:
        messagebox.showinfo(title="Warning", message="Enter Website To Search")

label_website= Label(text= "Website :", font= ("Arial ", 12 ,"bold"))
label_website.grid(column= 0,row=1, padx= 20, pady= 5)

label_email= Label(text= "Email/Username :", font= ("Arial ", 12 ,"bold"))
label_email.grid(column= 0,row=2, padx= 20, pady= 5)

label_password= Label(text= "Password :", font= ("Arial ", 12 ,"bold"))
label_password.grid(column= 0,row=3, padx= 20, pady= 5)

website_input= Entry(width= 30 , highlightcolor= "Green" , highlightthickness= 2)
website_input.grid(column= 1, row= 1)

email_input= Entry(width= 70 , highlightcolor= "Green" , highlightthickness= 2)
email_input.grid(column= 1, row= 2, columnspan= 2)
email_input.insert(index= 0, string="surya.2003amuari@gmail.com")

password_input= Entry(width= 30 , highlightcolor= "Green", highlightthickness= 2)
password_input.grid(column= 1, row= 3)

add_button= Button(text= "Add", width= 42, font= ("Arial ", 12 ,"bold"), command= save_data)
add_button.grid(column= 1, row= 4, columnspan= 2, padx= 20, pady= 5)

generate_button= Button(text= "Generate Password", width= 19, font= ("Arial ", 12 ,"bold"), command=generate)
generate_button.grid(column= 2, row= 3, columnspan= 2, padx= 20, pady= 5)

search_button= Button(text= "Search", width= 19, font= ("Arial ", 12 ,"bold"), command=search_password)
search_button.grid(column= 2, row= 1, columnspan= 2,pady= 5)

window.mainloop()