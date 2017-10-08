import numpy as np

def binary_treshold(v, trs):
    if v>trs:
        return 1
    else:
        return 0

def bipolar_treshold(v, trs):
    if v>trs:
        return 1
    else:
        return -1
