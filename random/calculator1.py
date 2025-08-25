import tkinter as tk
from tkinter import messagebox
import math
import re

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Мощный калькулятор")
        self.root.geometry("400x700")
        self.root.resizable(False, False)

        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        # Поле ввода
        self.entry = tk.Entry(self.root, font=("Arial", 24), borderwidth=5, relief="ridge", justify="right")
        self.entry.pack(pady=20, padx=20, fill="x")

        # Стандартные кнопки
        self.create_standard_buttons()

        # Научные кнопки
        self.create_scientific_buttons()

    def create_standard_buttons(self):
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', 'C', '+'),
            ('(', ')', '=', 'CE')
        ]

        for row in buttons:
            row_frame = tk.Frame(buttons_frame)
            row_frame.pack(expand=True, fill="both")
            for btn_text in row:
                btn = tk.Button(row_frame, text=btn_text, font=("Arial", 18), height=2, width=5,
                                command=lambda text=btn_text: self.on_button_click(text))
                btn.pack(side="left", expand=True, fill="both")

    def create_scientific_buttons(self):
        sci_frame = tk.Frame(self.root)
        sci_frame.pack(pady=10)

        sci_buttons = [
            ('sin', 'cos', 'tan', 'sqrt'),
            ('log', 'ln', 'pi', 'e'),
            ('^', '!', 'abs', 'exp')
        ]

        for row in sci_buttons:
            row_frame = tk.Frame(sci_frame)
            row_frame.pack(expand=True, fill="both")
            for func in row:
                btn = tk.Button(row_frame, text=func, font=("Arial", 14), height=2, width=5,
                                command=lambda f=func: self.on_function_click(f))
                btn.pack(side="left", expand=True, fill="both")

    def on_button_click(self, char):
        if char == "=":
            self.calculate()
        elif char == "C":
            self.expression = self.expression[:-1]
            self.update_entry()
        elif char == "CE":
            self.expression = ""
            self.update_entry()
        else:
            self.expression += str(char)
            self.update_entry()

    def on_function_click(self, func):
        if func in ('pi', 'e'):
            self.expression += str(getattr(math, func))
        elif func == 'ln':
            self.expression += 'ln('
        elif func == 'log':
            self.expression += 'log('
        elif func == '^':
            self.expression += '**'
        elif func == '!':
            self.expression += '!'
        else:
            self.expression += f"{func}("
        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

    def calculate(self):
        try:
            expr = self.expression

            # Заменяем функции на math.*
            expr = expr.replace('^', '**')
            expr = expr.replace('ln(', 'math.log(')
            expr = expr.replace('log(', 'math.log10(')
            expr = expr.replace('sqrt(', 'math.sqrt(')
            expr = expr.replace('sin(', 'math.sin(')
            expr = expr.replace('cos(', 'math.cos(')
            expr = expr.replace('tan(', 'math.tan(')
            expr = expr.replace('pi', 'math.pi')
            expr = expr.replace('e', 'math.e')
            expr = expr.replace('abs(', 'abs(')
            expr = expr.replace('exp(', 'math.exp(')

            # Обработка факториала: 5! -> math.factorial(5)
            expr = self.handle_factorial(expr)

            result = eval(expr)
            self.expression = str(result)
            self.update_entry()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Неверное выражение:\n{e}")
            self.expression = ""
            self.update_entry()

    def handle_factorial(self, expr):
        # Преобразование вида 5! → math.factorial(5)
        return re.sub(r'(\d+)!', r'math.factorial(\1)', expr)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()