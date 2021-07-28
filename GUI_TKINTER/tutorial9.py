from tkinter import *
import tkinter.messagebox

def doNothing():
    print("Not doing anything")


root = Tk()# creates a blank window

tkinter.messagebox.showinfo("Window titleee", message="Niks is an idiot")
answer= tkinter.messagebox.askquestion("Do you still want this?")

if answer == "yes":
    print("OK then continue")


root.mainloop()#continously on screen until we close..puts in an infinte loop until we close




