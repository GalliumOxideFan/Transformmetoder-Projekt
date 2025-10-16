import scipy
import numpy as np
import matplotlib.pyplot as plt

R=25
L=0.25
C=400*(10**-9)

täljare = [1, 0]
nämnare=[R*C, 1, R/L]

signal=scipy.signal.TransferFunction(täljare,nämnare)

w, A, fas = scipy.signal.bode(signal, w = np.logspace(0,9,1000))

f = w/(2*np.pi)
plt.plot(f,A, label = 'Amplitud')
plt.plot(f,fas, label = 'Fas')
plt.xscale('log')
plt.xlabel('Frekvens [Hz]')
plt.ylabel('Amplitud [Db]  |  Fas')
plt.grid()
plt.legend()
plt.xlim(1,10**8)
plt.show()