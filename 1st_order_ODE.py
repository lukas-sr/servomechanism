import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# initialization
K = 3
T = 4
u = 1
tstart = 0
tstop = 25
increment = 1
y0 = 0
t = np.arange(tstart,tstop+1,increment)

# function that returns dx/dt
def system1order(y, t, K, T, u):
    dydt = (1/T)*(-y+K*u)
    return dydt

# Solve ODE
x = odeint(system1order, y0, t, args=(K,T,u))

print(x)
plt.plot(t,x)
plt.title("1st order system dydt=(1/T)*(-y+K*u)")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.grid()
plt.show()
