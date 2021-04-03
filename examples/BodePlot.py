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

# Bode Plot
co.bode_plot(G7)

# Bode Plot in dB escale
co.bode_plot(G7, dB=True)

# Removing Mag, Phase, Freq from Bode Plot
mag, phase, freq = co.bode_plot(G7)

