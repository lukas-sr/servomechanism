import control as co
import numpy as np
import matplotlib.pyplot as plt

G1 = co.tf([2,5],[1,2,3]) # 2s + 5 / s^2 + 2s + 3 --- Provided only the coeficients

G2 = 5*co.tf(np.poly([-2,-5]), np.poly([-4,-5,-9])) # Provided the 'zeros' and the 'poles' of the function

# Transfer Function (TF) to State Space (SS)
G1_ss = co.tf2ss(G1)
print(G1_ss)

# State Space (SS) to Transfer Function (TF)
G1_tf = co.ss2tf(G1)
print(G1_tf)

# State Space Model
A = [[0, 1, 0], [0, 0, 1], [-1, -2, -3]]
B = [[0], [0], [1]]
C = [1, 0, 0]
D = 0
sys7 = co.ss(A, B, C, D)

sys7_tf  = co.ss2tf(sys7)

print(sys7_tf)
