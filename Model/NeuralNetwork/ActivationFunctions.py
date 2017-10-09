import numpy as np

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
