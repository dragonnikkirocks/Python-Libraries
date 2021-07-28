from tkinter import *



class NikkiButton():
    def __init__(self,master):#master is the root main window
        frame= Frame(master)
        frame.pack()

        self.printButton= Button(frame,text="Print a message",command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton= Button(frame,text="Quit",command=frame.quit)# quit breaks the main loop
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Nikki class")


root = Tk()# creates a blank window
b = NikkiButton(root)
root.mainloop()#continously on screen until we close..puts in an infinte loop until we close




