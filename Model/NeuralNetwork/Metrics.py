import numpy as np

def similarity(img1, img2, percent=False):
    width = img1.shape[0]
    height = img1.shape[1]
    ch = img1.shape[2]
    sim = np.round(np.sum(img1==img2)/ch,0)
    if len(img1.shape) == 2:
        img1 = np.reshape(img1, newshape=(width,height,1))
    ch = img1.shape[2]
    if percent:
        sim = (sim/(width*height*ch))*100
    return sim
