import numpy as np
import matplotlib.pyplot as plt

#write out the bessel function at an array of thetas for integration
def bessel(m, t, x): #t is an array of theta values
    bsl=[]
    for i in xrange(len(t)):
        bsl.append(np.cos(m*i-x*np.sin(i)))
    return bsl

#integrate and evaluate at list of x
def inbsl(xmin, xmax, tmin, tmax, N, m, Nx):
	Ns=np.linspace(tmin, tmax, N)
	bsvl=[]
	for i in np.linspace(xmin, xmax, Nx):
		y = bessel(m, np.asarray(Ns), i)
		mps=[]
		for i in xrange(N-1):
			mps.append((y[i]+y[i+1])/2)
		bsvl.append(((tmax-tmin)/N)*sum(mps)/np.pi)
	return bsvl
            
#for the given plot of bessel fn
#N=1000
#x=np.linspace(0, 20, N)
#y0=inbsl(0,20,0,np.pi, N, 0)
#y1=inbsl(0,20,0,np.pi, N, 1)
#y2=inbsl(0,20,0,np.pi, N, 2)
#y3=inbsl(0,20,0,np.pi, N, 3)

#plt.plot(x, y0, 'm-')
#plt.plot(x, y1, 'r-')
#plt.plot(x, y2, 'y-')
#plt.plot(x, y3, 'g-')

#plt.ylabel("$J_m(x)$")
#plt.xlabel('x')

#write out psf
def psfv(f, lm, I, Nq, qmin, qmax): #take radial distance from centre, focal ratio, and operational wavelength
	x = (np.pi*np.asarray(np.linspace(qmin, qmax, Nq))/f*lm)
	return I*(2*np.asarray(inbsl(x[0], x[-1], 0, np.pi, 10000, 1, Nq))/x)**2, x

arrs = psfv(6,500E-9,1,1000,0, 300000000)
c    = arrs[0]
xc   = arrs[1]
#assign points to values on the 1D psf
def get_nearest(arr,val):
    idx = (np.abs(arr-val)).argmin()
    return idx
#assemble as an array
def makepsf(ox,oy,arrpsf, arrx, dim, Npix):
	rng=np.linspace(-1*dim, dim, Npix)
	psfarr=[]
	for i in rng:
		psfrow=[]
		for j in rng:
			R=np.sqrt((ox-j)**2+(oy-i)**2)
			psfrow.append(arrpsf[get_nearest(arrx, R)])
		psfarr.append(psfrow)
	return psfarr

psf = makepsf(0,0,c,xc,80, 200)

#plt.imshow(psf, origin='lower', cmap='gray', vmax=0.05)
			
from astropy.io import fits 
from scipy import signal
somb = fits.open('sombrero.fits')[0].data[0]
plt.imshow(somb, origin='lower')

#somcon = signal.convolve(somb, psf)

			






