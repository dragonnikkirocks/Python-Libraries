import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.label = tk.Label(root, text="Hello World", padx=10, pady=10)
        self.label.pack()


if __name__=="__main__":
    root = Root()
    root.mainloop()
