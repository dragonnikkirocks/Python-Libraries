#Buttons

from tkinter import *

root = Tk()# creates a blank window

def rightClick(event):
    print("right")

def leftClick(event):
    print("left")

def middleClick(event):
    print("middle")


frame1 = Frame(root,width=300,height=400)
frame1.bind("<Button-1>",func=leftClick)
frame1.bind("<Button-2>",func=middleClick)
frame1.bind("<Button-3>",func=rightClick)
frame1.pack()



root.mainloop()#continously on screen until we close..puts in an infinte loop until we close




