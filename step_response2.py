import scipy.signal as sig
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Simulation Parameters
x0 = [0,0]

start = 0
stop = 30
step = 1
t = np.arange(start, stop, step)

K = 3
T = 4

# State-space Model
A = ([-1/T, 0], [0, 0])
B = ([K/T], [0])
C = ([1, 0])
D = 0

sys= sig.StateSpace(A, B, C, D)

# Step Response
t, y_s = sig.step(sys, x0, t)

# Plotting
plot = go.Figure(data=go.Scatter(x=t, y=y_s))
plot.update_layout(title = "Step Response",
        xaxis_title = "t [s]",
        yaxis_title = "y(s)")
plot.show()
