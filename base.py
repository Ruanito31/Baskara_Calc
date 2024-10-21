import baskara as f
from tkinter import *

root = Tk()

class Aplicação():
    def __init__(self):
        self.root = root
        self.tela()
        self.frame_tela()
        self.widgets_frame()
        root.mainloop()

    def tela(self):
        self.root.title("Baskara Calc")
        self.root.geometry("600x350")
        self.root.resizable(False, False)
        self.root.config(bg="#2b2b2b")

    def frame_tela(self):
        self.tela1 = Frame(self.root, bg="#393939")
        self.tela1.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.3)

        self.tela2 = Frame(self.root, bg="#393939")
        self.tela2.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.4)

    def widgets_frame(self):
        # Botões
        self.bt = Button(self.root, text="Calcular", command=self.calculo, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        self.bt.place(relx=0.7, rely=0.42, relheight=0.08, relwidth=0.2)

        self.bt_limpar = Button(self.root, text="Limpar", command=self.limpar, bg="#f44336", fg="white", font=("Arial", 12, "bold"))
        self.bt_limpar.place(relx=0.5, rely=0.42, relwidth=0.15, relheight=0.08)

        # Label e campos de entrada
        self.lb = Label(self.tela1, text="Digite a sua equação de 2º grau", font=("Arial", 14), bg="#393939", fg="white")
        self.lb.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.2)

        # Coeficientes
        self.lb_x_quadrado = Label(self.tela1, text="Coeficiente de X²:", bg="#393939", fg="white", font=("Arial", 12))
        self.lb_x_quadrado.place(relx=0.05, rely=0.3, relwidth=0.25, relheight=0.3)

        self.cod_entry_x_quadrado = Entry(self.tela1, font=("Arial", 12))
        self.cod_entry_x_quadrado.place(relx=0.3, rely=0.35, relwidth=0.15)

        self.lb_x = Label(self.tela1, text="Coeficiente de X:", bg="#393939", fg="white", font=("Arial", 12))
        self.lb_x.place(relx=0.5, rely=0.3, relwidth=0.25, relheight=0.3)

        self.cod_entry_x = Entry(self.tela1, font=("Arial", 12))
        self.cod_entry_x.place(relx=0.75, rely=0.35, relwidth=0.15)

        self.lb_numero = Label(self.tela1, text="Termo Independente:", bg="#393939", fg="white", font=("Arial", 12))
        self.lb_numero.place(relx=0.05, rely=0.65, relwidth=0.25, relheight=0.3)

        self.cod_entry_numero = Entry(self.tela1, font=("Arial", 12))
        self.cod_entry_numero.place(relx=0.3, rely=0.7, relwidth=0.15)

        # Label para mostrar a resposta
        self.lb_resposta = Label(self.tela2, text="", font=("Arial", 15), bg="#393939", fg="white", wraplength=400, justify="center")
        self.lb_resposta.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    def limpar(self):
        self.cod_entry_x_quadrado.delete(0, END)
        self.cod_entry_x.delete(0, END)
        self.cod_entry_numero.delete(0, END)
        self.lb_resposta["text"] = ""

    def calculo(self):
        try:
            value_a = float(self.cod_entry_x_quadrado.get())
            value_b = float(self.cod_entry_x.get())
            value_c = float(self.cod_entry_numero.get())
            resultado = f.baskara(value_a, value_b, value_c)
            self.lb_resposta["text"] = resultado
        except ValueError:
            self.lb_resposta["text"] = "Digite somente números"

Aplicação()
