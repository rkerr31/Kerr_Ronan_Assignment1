from astropy.io import fits 
from scipy import signal
somb = fits.open('sombrero.fits')[0].data[0]
plt.imshow(somb, origin='lower')

somcon = signal.convolve(somb, 30)
