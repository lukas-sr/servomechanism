import numpy as np
import matplotlib.pyplot as plt

# K is the process Gain and T is the time constant
K = 3
T = 4
start = 0
stop = 30
increment = 0.1
# array for the x axis
time = np.arange(start,stop,increment) 
y = K*(1-np.exp(-time/T))
plt.plot(time,y)
plt.title("1st Order Dynamic System")
plt.xlabel("t[s]")
plt.ylabel("y(s)")
plt.grid()
