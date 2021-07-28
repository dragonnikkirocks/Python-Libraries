import tkinter as tk
import tkinter.ttk as ttk

class Todo(tk.Tk):
    def __init__(self,tasks= None):
        super().__init__()
        if not tasks:
            self.tasks=[]
        else:
            self.tasks= tasks
        
        self.title("Nikki App")
        self.geometry("300x400")

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        todo1 = tk.Label(self, text="Add new items here",background="lightgrey", padx=10, pady=10)
        self.tasks.append(todo1)

        for task in self.tasks:
            task.pack(side= tk.TOP,fill= tk.X)

        self.task_create = tk.Text(self, height=3, bg ="white", fg= "black")

        #self.grid(row=0,column=0,sticky="ew")
        self.task_create.pack(side= tk.BOTTOM,fill= tk.X)
        self.task_create.focus_set()
        self.bind("<Return>", self.add_task)
        self.colour_schemes = [{"bg": "lightblue", "fg": "blue"}, {"bg": "pink", "fg": "red"}]

        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.task_create.yview)
        #self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.scrollbar.pack()

        #  communicate back to the scrollbar
        self.task_create['yscrollcommand'] = self.scrollbar.set

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0,tk.END).strip()
        if len(task_text) > 0:
            new_task = tk.Label(self, text=task_text, pady=10)
            _, task_style_choice = divmod(len(self.tasks), 2)
            my_scheme_choice = self.colour_schemes[task_style_choice]
            new_task.configure(bg=my_scheme_choice["bg"])
            new_task.configure(fg=my_scheme_choice["fg"])
            new_task.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(new_task)
        self.task_create.delete(1.0, tk.END)


if __name__=="__main__":
    todo = Todo()
    todo.mainloop()