#Grid layout
from tkinter import *

root = Tk()
label_1= Label(root, text="Name")
label_2 =Label(root,text="Password")
entry1= Entry(root)
entry2= Entry(root)

label_1.grid(row=0,sticky=E)#sticks to east - right aligned
label_2.grid(row=1,sticky=E)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

c= Checkbutton(root,text="Keep me logged in")
c.grid(columnspan=2)# keeps it in two columns- merges two columns and places it in the center

root.mainloop()