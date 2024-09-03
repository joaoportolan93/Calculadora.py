import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.geometry("400x600")
        self.root.configure(bg="#1c1c1c")

        self.expression = ""
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Configurar grade principal
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=5)
        self.root.rowconfigure(2, weight=5)
        self.root.rowconfigure(3, weight=5)
        self.root.rowconfigure(4, weight=5)
        self.root.rowconfigure(5, weight=5)
        self.root.columnconfigure(0, weight=1)

        # Display
        display_frame = tk.Frame(self.root, bg="#1c1c1c")
        display_frame.grid(row=0, column=0, sticky="nsew")

        display_label = tk.Label(display_frame, textvariable=self.result_var, anchor="e",
                                 bg="#1c1c1c", fg="white", padx=24, pady=20,
                                 font=font.Font(size=32))
        display_label.pack(expand=True, fill="both")

        # Botões
        button_frame = tk.Frame(self.root, bg="#1c1c1c")
        button_frame.grid(row=1, column=0, rowspan=5, sticky="nsew")

        # Configurar grade de botões
        for i in range(6):
            button_frame.rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.columnconfigure(j, weight=1)

        # Definir botões
        buttons = [
            ['AC', 'C', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '(', ')'],
            ['√', '^', '=', '']
        ]

        colors = ['#ff4b4b', '#ff758f', '#d780e3', '#88e4ff']  # Cores em gradiente

        for i, row in enumerate(buttons):
            for j, button in enumerate(row):
                if button == '':
                    continue  # Espaço vazio
                button_color = colors[j % len(colors)]
                btn = tk.Button(button_frame, text=button, font=font.Font(size=18, weight="bold"),
                                bg=button_color, fg="white", borderwidth=0,
                                activebackground="#4f4f4f", activeforeground="white",
                                command=lambda b=button: self.on_button_click(b))
                btn.grid(row=i, column=j, sticky="nsew", padx=1, pady=1)

                # Efeitos de hover
                btn.bind("<Enter>", lambda e, b=btn: b.configure(bg="#6f6f6f"))
                btn.bind("<Leave>", lambda e, b=btn, c=button_color: b.configure(bg=c))

    def on_button_click(self, char):
        if char == "=":
            try:
                # Avaliar a expressão de forma segura
                result = str(eval(self.expression))
                self.result_var.set(result)
                self.expression = result
            except Exception:
                self.result_var.set("Erro")
                self.expression = ""
        elif char == "C":
            # Apagar o último caractere
            self.expression = self.expression[:-1]
            self.result_var.set(self.expression)
        elif char == "AC":
            # Limpar toda a expressão
            self.expression = ""
            self.result_var.set(self.expression)
        elif char == "√":
            # Calcular a raiz quadrada
            try:
                result = str(eval(f"({self.expression})**0.5"))
                self.result_var.set(result)
                self.expression = result
            except Exception:
                self.result_var.set("Erro")
                self.expression = ""
        elif char == "^":
            # Operador de potência
            self.expression += "**"
            self.result_var.set(self.expression)
        else:
            self.expression += str(char)
            self.result_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
