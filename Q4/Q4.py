
# coding: utf-8

# In[ ]:

import numpy as np
import matplotlib.pyplot as plt

def iter8(i,k):
    c=complex(i,k)
    z0=0
    for m in xrange(1000):
        z0=z0**2+c
        if np.absolute(z0)>10 or np.isnan(np.absolute(z0)):
            return 1
    return 0
    

Npts = 1000
def itcmplx():
    arr=[]
    for i in np.linspace(-2,2,Npts):
        arrr=[]
        for k in np.linspace(-2,2,Npts):
            iter8(i,k)
            arrr.append(iter8(i,k))
        arr.append(arrr)
    return arr

farrr=itcmplx()

plt.imshow(itcmplx(), vmin=0, vmax=1)
plt.show()

