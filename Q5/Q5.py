import numpy as np
import matplotlib.pyplot as plt

def loglist(start, stop, num):
    lspace = np.logspace(np.log10(start),np.log10(stop),num)
    return np.array(sorted(set(lspace.tolist())))

lx = loglist(1.0E-11, 1.0E-4, 1000)

def fn(x):
	return x*(x-1)

def defderiv(delt, x):
	return (fn(x+delt)-fn(x))/delt

ldr=[]
for i in xrange(len(lx)):
	ldr.append(defderiv(lx[i], 1))
