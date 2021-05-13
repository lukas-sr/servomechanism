import numpy as np
import control as co
import matplotlib.pyplot as plt

# Transfer Function
Gs = co.tf([1], [1,3,2,0])

print(Gs)

co.root_locus(Gs)
co.sisotool(Gs)

plt.show()


