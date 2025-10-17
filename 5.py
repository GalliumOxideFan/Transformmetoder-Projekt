import scipy
import numpy as np
import matplotlib.pyplot as plt

R=25
L=0.25
C=400*(10**-9)
T_0 = 100*10**-6

täljare = [1, 0]
nämnare=[R*C, 1, R/L]

t=np.linspace(-10**-4,10**-4, 10**6)
V_in=scipy.signal.square(2*np.pi*t/T_0)

plt.plot(t, V_in, label = 'Amplitud')
plt.xlabel('Frekvens [Hz]')
plt.ylabel('Amplitud [Db]  |  Fas')
plt.grid()
plt.legend()
plt.show()


