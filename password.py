import tkinter as tk
from tkinter import ttk
import string
import random

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        self.root.config(bg="#333333")

        self.create_widgets()
        
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Password Generator", font=("Helvetica", 20, "bold"), fg="#FFFFFF", bg="#333333")
        self.title_label.pack(pady=20)

        self.length_label = tk.Label(self.root, text="Password Length:", font=("Helvetica", 12), fg="#FFFFFF", bg="#333333")
        self.length_label.pack(pady=5)

        self.length_entry = ttk.Entry(self.root, font=("Helvetica", 12))
        self.length_entry.pack(pady=5)

        self.generate_button = ttk.Button(self.root, text="Generate Password", command=self.generate_password, style="TButton")
        self.generate_button.pack(pady=20)

        self.password_label = tk.Label(self.root, text="", font=("Helvetica", 14), fg="#00FF00", bg="#333333")
        self.password_label.pack(pady=5)

        self.animation_label = tk.Label(self.root, text="", font=("Helvetica", 12), fg="#FFFFFF", bg="#333333")
        self.animation_label.pack(pady=5)

        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#D4A017", foreground="#333333", font=('Helvetica', 12))

    def generate_password(self):
        self.password_label.config(text="")
        self.animation_label.config(text="")
        
        length = self.length_entry.get()
        if not length.isdigit():
            self.password_label.config(text="Please enter a valid number.", fg="#FF0000")
            return
        
        length = int(length)
        if length <= 0:
            self.password_label.config(text="Please enter a positive number.", fg="#FF0000")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        
        self.animate_password_generation(password)

    def animate_password_generation(self, password):
        self.animation_label.config(text="Generating password...")
        
        self.root.after(1000, self.display_password, password)
    
    def display_password(self, password):
        self.animation_label.config(text="")
        self.password_label.config(text=password, fg="#00FF00")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
