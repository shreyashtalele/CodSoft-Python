import tkinter as tk
from tkinter import messagebox, ttk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("700x700")

        self.tasks = []

        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#ccc")
        self.style.configure("TCheckbutton", padding=6, background="#fff")

        self.frame = ttk.Frame(self.root)
        self.frame.pack(pady=10)

        self.canvas = tk.Canvas(self.frame)
        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.entry_task = ttk.Entry(self.root, width=50)
        self.entry_task.pack(pady=10)

        self.add_button = ttk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = ttk.Button(self.root, text="Update Selected Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = ttk.Button(self.root, text="Delete Selected Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.entry_task.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
        self.entry_task.delete(0, tk.END)

    def update_task(self):
        selected_task = self.get_selected_task()
        if selected_task is not None:
            new_task = self.entry_task.get()
            if new_task != "":
                self.tasks[selected_task[0]] = new_task
                self.update_task_list()
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        selected_task = self.get_selected_task()
        if selected_task is not None:
            del self.tasks[selected_task[0]]
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def get_selected_task(self):
        for idx, var in enumerate(self.task_vars):
            if var.get():
                return (idx, var)
        return None

    def update_task_list(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        self.task_vars = []
        for task in self.tasks:
            var = tk.BooleanVar()
            checkbox = ttk.Checkbutton(self.scrollable_frame, text=task, variable=var)
            checkbox.pack(anchor="w", padx=10, pady=5)
            self.task_vars.append(var)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
