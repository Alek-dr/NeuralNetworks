import numpy as np
from numpy import double
import matplotlib.pyplot as plt

function_params = {'K' :'0.5'}

def binary_treshold(v):
    if v>=0:
        return 1
    else:
        return 0

def bipolar_treshold(v):
    if v>0:
        return 1
    elif v==0:
        return 0
    elif v<0:
        return -1

def radially_symmetric(v):
    k = double(function_params['K'])
    thr = np.exp(-np.square(k) / np.square(k))
    y = np.exp(-np.square(v) / np.square(k))
    if y>=thr:
        return 1
    else:
        return 0

# r = 2
# s = np.linspace(-10,10,100)
# y = np.exp(-np.square(s)/np.square(r))
# sigma = np.std(y)
# print(sigma)
# plt.plot(s,y)
# plt.grid(True)
# plt.show()
