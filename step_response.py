import control as co
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

K = 3
T = 4
# H(s) = 3 / 4s + 1

num = np.array([K])
den = np.array([T , 1])

H = co.tf(num, den)
print('H(s) = ', H)

t , y_s = co.step_response(H)

simulation = go.Figure(data=go.Scatter(x=t, y=y_s))
simulation.update_layout(title = "Step Response",
        xaxis_title = "time [s]",
        yaxis_title = "y(s)")
simulation.show()
