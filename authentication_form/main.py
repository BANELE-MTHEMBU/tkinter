from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from PIL import ImageTk, Image    # first pip install pillow

#showing the image into our window
image=Image.open("../window/Logo.png")
print(image)

#window initialization
window =Tk()
window.iconbitmap('../window/icon.ico')
#setting the properties of the window
window.title("User Details")
#set width and height
w=500
h=200
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
position_from_top=int(screen_height/2-h/2)
position_from_right=int(screen_width/2-w/2)
#setting a fixed username and password
username_1="Banele"
password_1="Banele"

#function for performing log in

def login (username :str,password: str):
    if username.lower().scrip()==username_1 and password==password_1:
        #error.config(text="")
        messagebox.showinfo("App","You are logged in.")
    else:
        messagebox.showerror("Invalid credentials.")

#Closing the window
def close():
    response=messagebox.askyesnocancel("Close App","Are you sure you want to close this app")
    if response == True:
        window.destroy()
    else:
        window.focus()
def hideShow():
    if password_eye.get() == True:
        password.config(show="")
        eye.config(text="Hide password")
    else:
        password.config(show="*")
        eye.config(text="Show password")
#print(screen_width,screen_height)
window.geometry("{}x{}+{}+{}".format(w,h,position_from_right,position_from_top))
window.resizable(False,True)
Label(window, text="Logo").grid(
    row=0, column=0, columnspan=3
)
Label(window,text="Login Form",font=("Arial",13,"bold")).grid(row=1,column=1)
Label(window,text="Username",font=("Arial",13,)).grid(row=2, column=0,pady=5)
Label(window,text="Password",font=("Arial",13,)).grid(row=3, column=0,pady=5)
#Label(window,text="Gender",font=("Arial",13,)).grid(row=3, column=0,pady=5,sticky=W)



#gender_var= StringVar()
#genders=["Male","Female","Trans-gender"]
#visibility of password
password_eye=BooleanVar()

username=Entry(window, font=("Arial",10))
username.grid(row=2,column=1,sticky=W)

password=Entry(window,font=("Arial",10))
password.grid(row=3,column=1,sticky=W,pady=5)
eye=Checkbutton(window,variable=password_eye,command=hideShow,onvalue=True,offvalue=False)
eye.grid(row=4,column=1)

#buttons
Button(window,text="Login",font=("Calibri",12),bg="green",fg="white",width=10,bd=5,
       command=lambda : login(username.get(),password.get())


       ).grid(row=5,column=0)
Button(window,text="Register",font=("Calibri",12),bg="orange",fg="white",width=10,bd=5).grid(row=5,column=1)
Button(window,text="Close",font=("Calibri,12"),bg="red",fg="white",width=10,bd=5,command=close).grid(row=5,column=2)

#gender=OptionMenu(window,gender_var,*genders)
#gender.grid(row=3,column=1,pady=5,sticky=W)
#Label(window,text="Enter your description below: ",font=("Calibri",12)).grid(row=4,column=0,sticky=W,columnspan=3)
#description=scrolledtext.ScrolledText(window,width=30,height=8,font=("Calibri",10),bg="green")
#description.grid(row=5,column=0,sticky=W,columnspan=3)
window.mainloop()
