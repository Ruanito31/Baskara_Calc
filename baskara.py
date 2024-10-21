import math
from fractions import Fraction

def baskara(a, b, c):
    delta = pow(b,2) - 4 * a * c
    if delta < 0:
        return f"O valor de delta é: {delta}\nNão possui raízes reais"
    elif delta > 1: 
        raiz_delta1 = (b*-1 + math.sqrt(delta))/(2*a)
        raiz_delta2 = (b*-1 - math.sqrt(delta))/(2*a)
        if raiz_delta1 != int or raiz_delta2 != int:
            raiz_delta1 = Fraction(raiz_delta1).limit_denominator(10)
            raiz_delta2 = Fraction(raiz_delta2).limit_denominator(10)
            return (f"Valor de Delta: {delta}\nAs raízes de Delta são: {raiz_delta1} e {raiz_delta2}")

        else:
            return (f"Valor de Delta: {delta}\nAs raízes de Delta são: {raiz_delta1} e {raiz_delta2}")
    else:
        return (f"O valor de delta é {delta}\n Possui somente uma raiz: {raiz_delta1} ")




   