#============================#
# Fermi Dirac  Distribution #
#============================#

import numpy as np
import matplotlib.pyplot as plt

E=np.linspace(6.8,7.4,1000)
mu=7.1
k=0.0000865
T=[100,200,300,400,500,600]

for i in range(6):
    f=lambda E:1/((np.exp((E-mu)/(k*T[i])))+1)
    plt.plot(E,f(E),label='T='+str(T[i])+'k')
    plt.legend()
    
plt.grid()
plt.title(r'Fermi Dirac Distribution [ $\frac{1}{\exp(\frac{E-\mu}{K_bT}+1)}$]')
plt.xlabel('E(Energy)$\longrightarrow$',size = 14)
plt.ylabel(r'$\frac{1}{\exp(\frac{E-\mu}{K_bT}+1)}\longrightarrow$' ,size=18)
plt.axhline(0.5,c='black')
plt.show()

