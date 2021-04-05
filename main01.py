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
print(G1)
print('DC Gain: '+ str(co.dcgain(G1)))      # DC Gain
print('Pole: ' + str(co.pole(G1)))          # Pole for G6
print('Zero: ' + str(co.zero(G1)))          # Zero for G6

