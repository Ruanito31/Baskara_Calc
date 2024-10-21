import baskara as f
from tkinter import *

root = Tk()

class Aplicação():
    def __init__(self):
        self.root = root
        self.tela()
        self.frame_tela()
        self.widgtes_frame()
        self.calculo
        self.limpar
        root.mainloop()

    def tela(self):
        self.root.title("Baskara Calc")
        self.root.geometry("550x300")
        self.root.resizable(False, False)
        self.root.config(bg="#242323")

    def frame_tela(self):
        self.tela1 = Frame(self.root)
        self.tela1.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.2)

        self.tela2 = Frame(self.root)
        self.tela2.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.4)
    
   
    def widgtes_frame(self):
        #botão
        self.bt = Button(self.root, text="Calcular", command=self.calculo)
        self.bt.place(relx=0.5, rely=0.4, relheight=0.15, relwidth=0.1)

        self.bt_limpar = Button(self.root, text="Limpar", command=self.limpar)
        self.bt_limpar.place(relx=0.4, rely=0.4, relwidth=0.1, relheight=0.15)
        #label
        self.lb = Label(self.tela1, text="Digite a sua equação de 2º grau", font=("Arial", 12))
        self.lb.place(relx=0.1, rely=0.02, relwidth=0.8, relheight=0.4)
        #texto e entry x²
        self.lb_x_quadrado = Label(self.tela1, text="X²")
        self.lb_x_quadrado.place(relx=0.2, rely=0.4, relwidth=0.13, relheight=0.4)

        self.cod_entry_x_quadrado = Entry(self.tela1)
        self.cod_entry_x_quadrado.place(relx=0.2, rely=0.4, relwidth=0.05)

        #texto e entry X
        self.lb_x = Label(self.tela1, text="X")
        self.lb_x.place(relx=0.35, rely=0.4, relwidth=0.13, relheight=0.4)

        self.cod_entry_x = Entry(self.tela1)
        self.cod_entry_x.place(relx=0.35, rely=0.4, relwidth=0.05)

        #texto e entry Numero
        self.lb_numero= Label(self.tela1)
        self.lb_numero.place(relx=0.5, rely=0.4, relwidth=0.13, relheight=0.4)

        self.cod_entry_numero = Entry(self.tela1)
        self.cod_entry_numero.place(relx=0.5, rely=0.4, relwidth=0.05)

        self.lb_resposta = Label(self.tela2, text="", font=("arial", 15))
        self.lb_resposta.place(relx=0.1, rely=0.02, relwidth=0.8, relheight=0.4)

    def limpar(self):
        self.cod_entry_x_quadrado.delete(0)
        self.cod_entry_x.delete(0)
        self.cod_entry_numero.delete(0)
        self.lb_resposta["text"] = ""

       

        #resposta
    def calculo(self):      
        try:
            value_a = float(self.cod_entry_x_quadrado.get())
            value_b = float(self.cod_entry_x.get())
            value_c = float(self.cod_entry_numero.get())

            self.lb_resposta["text"] = f.baskara(value_a, value_b, value_c)
        except ValueError:
             self.lb_resposta["text"] = "Digite somente números"



Aplicação()






#try:
 #   value_a = float(input("Qual o valor de A? \n"))
  #  value_b = float(input("Qual o valor de B? \n"))
   # value_c = float(input("Qual o valor de C? \n"))
#
 #   f.baskara(value_a, value_b, value_c)
#except ValueError:
 #   print("Digite somente números")


