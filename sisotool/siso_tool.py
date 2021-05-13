import numpy as np
import control as co
import matplotlib.pyplot as plt

print("===> Sisotool com python <===")
num = (input("numerador >> ")).split()
num = [int(i) for i in num]
den = (input("denominador >> ")).split()
den = [int(i) for i in den]

# Função de transferência
Gs = co.tf(num, den)

print(Gs)

co.sisotool(Gs)

plt.show()
