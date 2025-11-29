#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora básica")
        self.resizable(False, False)
        self.expr = ""
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style(self)
        try:
            style.theme_use('clam')
        except Exception:
            pass

        self.display = tk.Entry(self, font=("Segoe UI", 20), justify='right', bd=5, relief='sunken')
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
        ]

        for r, row in enumerate(buttons, 1):
            for c, char in enumerate(row):
                btn = ttk.Button(self, text=char, command=lambda ch=char: self.on_click(ch))
                btn.grid(row=r, column=c, ipadx=10, ipady=10, padx=3, pady=3, sticky='nsew')

        clear = ttk.Button(self, text='C', command=self.clear)
        clear.grid(row=5, column=0, columnspan=2, sticky='nsew', padx=3, pady=3)

        back = ttk.Button(self, text='⌫', command=self.backspace)
        back.grid(row=5, column=2, columnspan=2, sticky='nsew', padx=3, pady=3)

        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

        self.bind('<Return>', lambda e: self.evaluate())
        self.bind('<BackSpace>', lambda e: self.backspace())
        self.bind('<Escape>', lambda e: self.clear())
        self.bind('<Key>', self.keypress)

    def keypress(self, event):
        char = event.char
        if char in '0123456789.+-*/':
            self.expr += char
            self.update_display()
        elif char == '\r':
            self.evaluate()

    def on_click(self, ch):
        if ch == '=':
            self.evaluate()
        else:
            self.expr += ch
            self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expr)

    def clear(self):
        self.expr = ""
        self.update_display()

    def backspace(self):
        self.expr = self.expr[:-1]
        self.update_display()

    def evaluate(self):
        try:
            # Evaluación controlada: no exponer builtins
            result = eval(self.expr, {"__builtins__": None}, {})
            self.expr = str(result)
            self.update_display()
        except Exception:
            self.expr = "Error"
            self.update_display()
            self.expr = ""


def main():
    app = Calculator()
    app.mainloop()


if __name__ == '__main__':
    main()
