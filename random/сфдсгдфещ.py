import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("600x800")
        self.root.configure(bg="#2C3E50")
        
        self.expression = ""
        
        self.create_display()
        self.create_buttons()
        self.configure_grid()
    
    def create_display(self):
        self.display_frame = tk.Frame(self.root, bg="#34495E", bd=10, relief=tk.RIDGE)
        self.display_frame.grid(row=0, column=0, columnspan=4, sticky="nsew")
        
        self.display = tk.Entry(
            self.display_frame, font=("Arial", 32), bd=10, relief=tk.RIDGE, 
            justify='right', bg="#ECF0F1", fg="#2C3E50"
        )
        self.display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    def create_buttons(self):
        self.button_frame = tk.Frame(self.root, bg="#2C3E50")
        self.button_frame.grid(row=1, column=0, sticky="nsew")
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('(', 5, 0), (')', 5, 1), ('√', 5, 2), ('^', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('log', 6, 3),
            ('π', 7, 0), ('e', 7, 1), ('%', 7, 2), ('=', 7, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(
                self.button_frame, text=text, font=("Arial", 18), bd=5, 
                width=8, height=3, bg="#ECF0F1", fg="#2C3E50",
                command=lambda t=text: self.on_button_click(t)
            )
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        
        for i in range(8):
            self.button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.button_frame.grid_columnconfigure(j, weight=1)
    
    def configure_grid(self):
        for i in range(2):
            self.root.grid_rowconfigure(i, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
    
    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = self.expression.replace("^", "**").replace("√", "math.sqrt")
                self.expression = self.expression.replace("π", "math.pi").replace("e", "math.e")
                self.expression = self.expression.replace("log", "math.log10").replace("%", "/100*")
                self.expression = self.expression.replace("sin", "math.sin").replace("cos", "math.cos").replace("tan", "math.tan")
                self.expression = str(eval(self.expression))
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
        else:
            self.expression += char
        
        self.update_display()
    
    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
