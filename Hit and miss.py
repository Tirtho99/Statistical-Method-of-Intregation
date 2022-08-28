import numpy as np
from tabulate import tabulate
import random
def f(y):
    return (y*np.sin(y))**2
M=[]
correct_I= (4*np.pi**3/3)-(np.pi/2)
a=0
b= 2*np.pi
y=np.linspace(a,b,1000)
F=f(y)
fmax=max(F)
At= fmax*(b-a)
dx= 0.1
nx= int((b-a)/dx+0.5) # number of steps for changing x
Ntrial= 10
for i in range(0,5):   
    x=a
    nhit=0
    L=[]
    for j in range(0,nx):
        for k in range(0,Ntrial):
            r= random.random()*fmax
            if r< f(x):         
                nhit= nhit+1
            else:
                continue
        x= x+dx
    I= (At*nhit)/(nx*Ntrial)
    err= abs(correct_I- I)
    L.append(Ntrial)
    L.append(I)
    L.append(err)
    M.append(L)
    Ntrial= Ntrial*5
print(tabulate(M, headers=["No of Trials", "Intregation Val", "Error"]))
            
        
