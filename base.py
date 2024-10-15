import baskara as f

try:
    value_a = float(input("Qual o valor de A? \n"))
    value_b = float(input("Qual o valor de B? \n"))
    value_c = float(input("Qual o valor de C? \n"))

    f.baskara(value_a, value_b, value_c)
except ValueError:
    print("Digite somente números")

