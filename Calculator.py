import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.config(bg="#333333")

        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.operation = ""
        self.result = False

        self.display_frame = tk.Frame(self.root, bg="#333333")
        self.display_frame.pack(expand=True, fill="both")

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(expand=True, fill="both")

        self.create_display()
        self.create_buttons()

    def create_display(self):
        self.display = tk.Entry(self.display_frame, font=("Helvetica", 24), fg="#FFFFFF", bg="#333333", bd=0, justify="right")
        self.display.pack(expand=True, fill="both")

    def create_buttons(self):
        buttons = [
            'C', '+/-', '%', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '='
        ]

        row_val = 0
        col_val = 0

        for button in buttons:
            if button == "0":
                btn = tk.Button(self.button_frame, text=button, font=("Helvetica", 18), fg="#FFFFFF", bg="#505050", command=lambda x=button: self.num_press(x))
                btn.grid(row=row_val, column=col_val, columnspan=2, sticky="nsew")
                col_val += 2
            elif button == "C":
                btn = tk.Button(self.button_frame, text=button, font=("Helvetica", 18), fg="#FFFFFF", bg="#D4A017", command=self.clear)
                btn.grid(row=row_val, column=col_val, sticky="nsew")
                col_val += 1
            elif button == "=":
                btn = tk.Button(self.button_frame, text=button, font=("Helvetica", 18), fg="#FFFFFF", bg="#D4A017", command=self.calculate)
                btn.grid(row=row_val, column=col_val, sticky="nsew")
                col_val += 1
            else:
                btn = tk.Button(self.button_frame, text=button, font=("Helvetica", 18), fg="#FFFFFF", bg="#505050", command=lambda x=button: self.num_press(x) if x.isdigit() or x == '.' else self.operation_press(x))
                btn.grid(row=row_val, column=col_val, sticky="nsew")
                col_val += 1

            if col_val > 3:
                col_val = 0
                row_val += 1

        for i in range(5):
            self.button_frame.grid_rowconfigure(i, weight=1)
            self.button_frame.grid_columnconfigure(i, weight=1)

    def num_press(self, num):
        self.result = False
        first_num = self.display.get()
        second_num = str(num)
        if self.new_num:
            self.current = second_num
            self.new_num = False
        else:
            if second_num == '.':
                if second_num in first_num:
                    return
            self.current = first_num + second_num
        self.display.delete(0, "end")
        self.display.insert(0, self.current)

    def clear(self):
        self.result = False
        self.current = "0"
        self.display.delete(0, "end")
        self.display.insert(0, self.current)
        self.new_num = True

    def operation_press(self, op):
        self.current = float(self.current)
        if self.op_pending:
            self.perform_calc()
        elif not self.result:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.operation = op
        self.result = False

    def perform_calc(self):
        if self.operation == "+":
            self.total += self.current
        if self.operation == "-":
            self.total -= self.current
        if self.operation == "*":
            self.total *= self.current
        if self.operation == "/":
            if self.current == 0:
                self.total = "Error"
            else:
                self.total /= self.current
        self.new_num = True
        self.op_pending = False
        self.display.delete(0, "end")
        self.display.insert(0, self.total)

    def calculate(self):
        self.result = True
        self.current = float(self.current)
        self.perform_calc()

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
