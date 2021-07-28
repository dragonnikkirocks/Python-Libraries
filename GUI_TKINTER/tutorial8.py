from tkinter import *
import tkinter.messagebox

def doNothing():
    print("Not doing anything")


root = Tk()# creates a blank window
menu = Menu(root)
root.config(menu=menu)

subMenu= Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New project ..",command=doNothing)
subMenu.add_command(label="New file ..",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit ..",command=root.quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Edit file",command=doNothing)

#Creating the tool bar

toolbar= Frame(root,bg="blue")
insertButton = Button(toolbar,text="insert image", command=doNothing)
insertButton.pack(side=LEFT,padx=2,pady=2) #padding is jst extra space
printButton = Button(toolbar,text="Print",command=doNothing)
printButton.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)


#Creating status bar

statusbar = Label(root,text="Preparing to do nothing ..", bd=1, relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)

root.mainloop()#continously on screen until we close..puts in an infinte loop until we close




