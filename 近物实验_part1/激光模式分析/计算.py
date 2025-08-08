import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import pi,c

L1 = 0.35  # meter
L2 = 0.235  # meter

def delta_nu_h(L):
    return c/(2*pi*1*L)*1*np.sqrt(np.arccos(1-L/1))
def delta_nu_q(L):
    return c/(2*1*L)

a = 1875*(2560/4250)

print(a)