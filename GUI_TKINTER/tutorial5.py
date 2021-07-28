from tkinter import *

root = Tk()# creates a blank window

def printName(event):
    print("Hello Nikki here")

button1= Button(root,text="Button 1")
button1.bind("<Button-1>",printName) # like a callback - notice <> that has to be there
button1.pack()



root.mainloop()#continously on screen until we close..puts in an infinte loop until we close