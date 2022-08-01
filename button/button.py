from tkinter import *

root = Tk()
root.title("My app")
root.geometry("500x200+{}+{}".format(500, 300))
root.resizable(False, True)
#python to navigate twice to another folder window which has an icon image
root.iconbitmap('../window/icon.ico')

def sayHello():
    print("Hello welcome to the wolrd of creating application")
Button(root, text="start button", width=100, bg="blue", fg="white", command=sayHello()).pack()

root.mainloop()