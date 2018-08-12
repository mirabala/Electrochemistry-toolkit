
# coding: utf-8

# In[18]:

import pylab as py
import lmfit  #https://lmfit.github.io/lmfit-py/model.html
import numpy as np



def approach(L, E, E0, D, k0, rtip=25e-7, n=1, alpha=0.5, T=293, pn=0):
    #binary variable for positive or negative approach curves:
    #positive approach curve, p: 0
    #negative approach curve, n: 1
    #pn=bin(pn)
    F=96485  # Faraday Constant | C/mol
    R=8.314 #Gas Constant | J/mol*K
    f=F/(R*T)
    n= int(n)
    pn=int(pn)
    
    # effective mass transfer coefficient
    m0=(4*D*(0.68+0.78377/L+0.315*py.exp(-1.0672/L)))/(py.pi*rtip)
    
    # rate constant
    k=k0*py.exp(-alpha*n*f*(E-E0))/m0
    
    if pn==0: 
        #positive approach

        # Dimensionless Current
        I=(0.68+0.78377/L+0.315*py.exp(-1.0672/L))/(1+py.exp(n*f*(E-E0))+1/k)
    elif pn==1:
        #negative approach
        I=1/(0.292+1.515/L+0.6553*py.exp(-2.4035/L))

    return I

def approach_plot(x,y, E=0.4, E0=0, D=10e-6, k0=1, rtip=25e-7, n=1, alpha=0.5, T=293):
    py.plot(x,y)
    py.xlabel('L')
    py.ylabel('$i_T$(L)/$i_T,_\infty$')
    py.text(0.7*np.max(x),(np.max(y)-np.min(y))*0.9+np.min(y),'$k_0$=%1.0e cm/s'%k0)
    py.text(0.7*np.max(x),(np.max(y)-np.min(y))*0.8+np.min(y),'D=%1.0e cm$^2$/s'%D)
    py.text(0.7*np.max(x),(np.max(y)-np.min(y))*0.7+np.min(y),'$E$=%1.2f V'%E)
    py.show()



