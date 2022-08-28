import numpy as np
import random
def f1(x):
	return np.sin(x)**2
def f2(x):
	return (x*np.sin(x))**2
a=0
b=2*np.pi
c1=np.pi
c2=(4*np.pi**3/3)-(np.pi/2)
V=[]
M=0
N=[100.0,500.0,1000.0,5000.0,10000.0,50000.0,100000.0,50000.0,1000000.0]
for i in N:
	k=int(i)
	sum=0
	while(k>0):
		xi=a+(b-a)*random.random()
		sum=sum+f2(xi)
		k=k-1
		M=(sum/i)*(b-a)
	V.append(M-c1)
	print("The value of the intregal:",M)
	print("The error is: ",np.abs(M-c2))


	
		
		