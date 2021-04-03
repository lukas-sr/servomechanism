import control as co
import numpy as np
import matplotlib.pyplot as plt

G1 = co.tf([10], [1, 3, 1])

# Nysquit Plot for the Transfer Function Above
co.nysquit_plot(G1)

# Stability Margins
G2 = co.tf([10], np.poly([-1, -2, -3]))
GM, PM, _, PCF, GCF, _ = co.stability.margins(G2)
print("f'PCF = {PCF}, GM (abs) = {GM}, GCF = {GCF}, PM (deg) = {PM}") 
