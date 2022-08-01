from tkinter import *
window = Tk()
window .title("User Details")
window .geometry("500x200+{}+{}".format(500, 300))
window .resizable(False, False)
window .iconbitmap('..//window/icon.ico')
#adding a label
Label(window,text="Label",font=("Ariel",12,"bold"), bg ="red",fg="White").pack()
Button(window, text="Button",font=("Ariel",13,"bold"),bg="pink",fg="yellow").pack()
window .mainloop()