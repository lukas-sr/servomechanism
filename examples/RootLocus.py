import control as co
import numpy as np
import matplotlib.pyplot as plt

G0 = co.tf([co.tf([1], [1, 4, 5, 0]))

co.root_locus(G0)
