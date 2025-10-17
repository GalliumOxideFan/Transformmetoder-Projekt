import scipy
import numpy as np
import matplotlib.pyplot as plt
import csv

R=25
L=0.25
C=400*(10**-9)
T_0 = 100*10**-6

täljare = [1, 0]
nämnare=[R*C, 1, R/L]


system=scipy.signal.TransferFunction(täljare,nämnare)


t=np.linspace(0,10**-3, 10**6)
k=1

insignaler = []
frekvenser = []
amplituder = np.zeros(5)
faser = np.zeros(5)
utsignaler = []


for k in range(1,6):
  signal = 2/((2*k-1)*np.pi)*np.sin(2*np.pi*(2*k-1)/T_0*t)
  frekvens = round(2*np.pi*(2*k-1)/T_0/(2*np.pi))

  _, h = scipy.signal.freqresp(system, w=frekvens*2*np.pi)

  amplitud=round(float(20 * np.log10(abs(h))),2)

  fas = round(float(np.angle(h, deg=True)),2)

  utsignal=str(round(float(2/((2*k-1)*np.pi)*amplitud),4))+" * sin("+str(round(2*np.pi*(2*k-1)/T_0))+"t + "+str(round(float(fas),1))+"*)"
  insignal = str(round(2/((2*k-1)*np.pi),4))+" * sin("+str(round(2*np.pi*(2*k-1)/T_0))+"t)"
  
  insignaler.append(insignal)
  frekvenser.append(frekvens)
  amplituder[k-1]=float(amplitud)
  faser[k-1]=float(fas)
  utsignaler.append(utsignal)

print("Insignaler: ", insignaler)
print("Frekvenser: ",frekvenser)
print("Gains: ",amplituder)
print("Fasskiftningar: ",faser)
print("Utsignaler: ", utsignaler)


filnamn="lista.csv"
with open(filnamn, 'w', newline='') as file:
  writer = csv.writer(file)
  for c1, c2, c3, c4, c5 in zip(insignaler, frekvenser, amplituder, faser, utsignaler):
        writer.writerow([c1, c2, c3, c4, c5])


