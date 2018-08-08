
# coding: utf-8

# In[18]:


get_ipython().run_line_magic('pylab', 'inline')
from lmfit import Model

k0=1 # Rate Constant | cm/s
D=1e-6 # Diffusion Coefficient | cm2/s
E=0.1 # applied potential | V
E0=0.4 # formal potential | V
alpha=0.5  # Charge transfer coefficient
F=96485  # Faraday Constant | C/mol
R=8.314 #Gas Constant | J/mol*K
T=293 #Temperature | K
f=F/(R*T)
n=1  # number of electrons per reaction 
rtip=25e-7 # Tip radius | cm
z=np.linspace(0.2,10,49) # Dimensionless Distance 

def approach(L, E, E0, D=1e-6, rtip=25e-7, k0=1, n=1, alpha=0.5, T=293):
    F=96485  # Faraday Constant | C/mol
    R=8.314 #Gas Constant | J/mol*K
    f=F/(R*T)
    
    # effective mass transfer coefficient
    m0=(4*D*(0.68+0.78377/L+0.315*exp(-1.0672/L)))/(pi*rtip)
    
    # rate constant
    k=k0*exp(-alpha*n*f*(E-E0))/m0
    
    # Dimensionless Current
    Ip=(0.68+0.78377/L+0.315*exp(-1.0672/L))/(1+exp(n*f*(E-E0))+1/k)
    
    In=1/(0.292+1.515/L+0.6553*exp(-2.4035/L))
    
    plot(L,Ip)
    xlabel('L')
    ylabel('$i_T$(L)/$i_T,_\infty$')
    text(7,0.4,'$k_0$=%1.0e cm/s'%k0)
    text(7,0.3,'D=%1.0e cm$^2$/s'%D)
    text(7,0.2,'$E$=%1.2f V'%E)
    show()
    return Ip
y=approach(L,E,E0)

def approach_fit(y):
    fmodel=Model(approach)
    # initial values
    params = fmodel.make_params(E=0, E0=0, D=1e-6, rtip=25e-7, k0=1, n=1, alpha=0.5, T=293)
    # fix parameters:
    params['T'].vary = False
    params['alpha'].vary = False
    params['rtip'].vary = False
    params['E0'].vary = False
    params['E'].vary = False
    
    # fit parameters to data with various *static* values of b:
#    for b in range(10):
#        params['T'].value = 293
#        params['alpha'].value = 0.5
#        params['rtip'].value = 25e-7
#        params['E0'].value = 0
#        params['E'].value = 0.4
        
    result = fmodel.fit(i, params, x=L)

t=approach_fit(y)
print(t)

