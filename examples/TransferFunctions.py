import control as co
import numpy as np
import matplotlib.pyplot as plt

G1 = co.tf([2,5],[1,2,3]) # 2s + 5 / s^2 + 2s + 3 --- Provided only the coeficients

G2 = 5*co.tf(np.poly([-2,-5]), np.poly([-4,-5,-9])) # Provided the 'zeros' and the 'poles' of the function

# Algebrism is supported
G3 = G1+G2
G4 = G1*G2
G5 = G1/G2
G6 = G1-G2
G7 = co.feedback(G1,G2)

# Minimum Realization (Pole-Zero Cancellation)
co.minreal(G2)

# TF Properties
print(co.dcgain(G6)) # DC Gain
print(co.pole(G6))   # Pole for G6
print(co.zero(G6))   # Zero for G6

