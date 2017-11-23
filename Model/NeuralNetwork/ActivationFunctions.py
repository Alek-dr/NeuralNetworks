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
    k2 = np.square(k)
    thr_ = 315.38
    thr = np.exp(-np.square(thr_)/k2)
    num = np.square(v)
    den = np.square(k)
    p = num/den
    y = np.exp(-p)
    if y>=abs(thr):
        return 1
    else:
        return 0

# r = 300
# s = np.linspace(-2800,2200,100)
# y = np.exp(-np.square(s+158)/np.square(r))
# samples_1 = [4.714e-23, 4.43e-32]
# samples_2 = [0.496, 0.971, 0.781]
# s1 = [2151-158, -2549-158]
# s2 = [251-158, 51-158, -149-158]
# line = [0.1 for l in s]
#
# fig, ax = plt.subplots()
#
# plt.plot(s,y)
# plt.plot(s1, samples_1, 'go')
# plt.plot(s2, samples_2, 'ro')
# plt.plot(s,line, 'r--')
# plt.xlabel("s")
# plt.ylabel("y")
#
# an1 = ax.annotate("s5", xy=(251-158, 0.496),
#                   xytext=(251-158+200, 0.496+0.02),
#                   va="top", ha="center")
# an2 = ax.annotate("s6", xy=(51-158, 0.971),
#                   xytext=(51-158+150, 0.971+0.02),
#                   va="top", ha="center")
# an3 = ax.annotate("s7", xy=(-149-158, 0.781),
#                   xytext=(-149-158+150, 0.781+0.02),
#                   va="top", ha="center")
# an4 = ax.annotate("A2", xy=(2151-158, 4.714e-23),
#                   xytext=(2151, 4.714e-23+0.05),
#                   va="top", ha="center")
# an5 = ax.annotate("C2", xy=(-2549-158, 4.43e-32),
#                   xytext=(-2549-158+150, 4.43e-32+0.05),
#                   va="top", ha="center")
# plt.grid(True)
# plt.show()
