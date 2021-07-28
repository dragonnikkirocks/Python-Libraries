from tkinter import *

root = Tk()

one = Label(root,text="One",bg="Black",fg="red")
one.pack()
two = Label(root,text="Two",bg="Black",fg="blue")
two.pack(fill='x')#fill stretches in x direction as window moves
three = Label(root,text="Three",bg="Black",fg="green")
three.pack(fill='both')#fill stretches in y direction as window moves


root.mainloop()