import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# K is the process Gain and T is the time constant
K = 3
T = 4
start = 0
stop = 30
increment = 0.1
# array for the x axis
time = np.arange(start,stop,increment) 
y = K*(1-np.exp(-time/T))

graph = px.line(time,y)

graph.update_xaxes(
        title_text="t [s]", 
        title_font={"size":14}
        )

graph.update_yaxes(
        title_text="y(s)", 
        title_font={"size":14}
        )

graph.update_layout(title_text = "1st Order Dynamic System")
graph.show()
