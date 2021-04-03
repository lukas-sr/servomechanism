import control as co
import numpy as np
import matplotlib.pyplot as plt

G1 = co.tf([2,5],[1,2,3]) # 2s + 5 / s^2 + 2s + 3 --- Provided only the coeficients

G2 = 5*co.tf(np.poly([-2,-5]), np.poly([-4,-5,-9])) # Provided the 'zeros' and the 'poles' of the functions

A = [[0,1,0],[0,0,1],[-1,-2,-3]]
B = [[0],[0],[1]]
C = [1,0,0]
D = 0
sys7=co.ss(A,B,C,D)

t = np.linspace(0, 20, 1000)
t1, y1 = co.step_response(sys7, t, [-1, 0, 2])

plt.plot(t1,y1)
plt.xlabel('time (s)')
plt.ylabel('amplitude')
plt.grid()
