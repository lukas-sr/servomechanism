import control as co
import numpy as np
import matplotlib.pyplot as plt

G1 = co.tf([2,5],[1,2,3]) # 2s + 5 / s^2 + 2s + 3 --- Provided only the coeficients

G2 = 5*co.tf(np.poly([-2,-5]), np.poly([-4,-5,-9])) # Provided the 'zeros' and the 'poles' of the function

t = np.linspace(0, 10, 1000)
t1, y1 = co.step_response(G1, t)

plt.plot(t1,y1)
plt.xlabel('time (s)')
plt.ylabel('amplitude')
plt.grid()
