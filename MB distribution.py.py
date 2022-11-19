#================================#
# MAXWELL BOLLTZMAN DISTRIBUTION #
#================================#


import numpy as np
import matplotlib.pyplot as plt

E=np.linspace(7.1,7.4,1000)
mu=7.1
k=0.0000865
T=[100,200,300,400,500,600]

for i in range(6):
    f=lambda E:1/np.exp((E-mu)/(k*T[i]))
    plt.plot(E,f(E),label='T='+str(T[i])+'k')
    plt.legend()
    
plt.grid()
plt.title(r'Maxwell-boltzmann Distribution [ $\frac{1}{\exp(\frac{E-\mu}{K_bT})}$]')
plt.xlabel('E(Energy)$\longrightarrow$',size=10)
plt.ylabel(r'$\frac{1}{\exp(\frac{E-\mu}{K_bT})}$$\longrightarrow$',size=18)
plt.axhline(c='black')
plt.show()
