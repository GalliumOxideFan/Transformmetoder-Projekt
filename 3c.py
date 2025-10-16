import scipy
import matplotlib.pyplot as plt
import numpy as np

R=25
L=0.25
C=400*(10**-9)

täljare = [1, 0]
nämnare=[R*C, 1, R/L]

scipyFunc=scipy.signal.TransferFunction(täljare,nämnare)
t, V_ut = scipy.signal.step(scipyFunc, T=np.linspace(0,0.05,10**6))

plt.plot(t,V_ut, label = 'Stegsvar')
plt.xlabel('Tid [s]')
plt.ylabel('V_ut')
plt.grid()
plt.legend()
plt.xlim(-0.005,0.03)
plt.ylim(-.1,1.05)
plt.show()

plt.plot(t,V_ut, label = 'Stegsvar kort intervall')
plt.xlabel('Tid [s]')
plt.ylabel('V_ut')
plt.grid()
plt.legend()
plt.xlim(-0.00005,0.0005)
plt.ylim(-.1,1.05)
plt.show()