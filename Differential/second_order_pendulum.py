import numpy as np
import matplotlib.pyplot as plt

def harmonic(x0,v0,T,dt=0.01,k=1.0,m=1.0):
    E0  = 0.5*m*v0**2 - np.cos(x0)
    Time = [i*dt for i in range(int(T/dt)+1)]
    X = [x0]
    V = [v0]
    Energy = [E0]
    x = x0
    v = v0
    
    for i in range(int(T/dt)):
        f0x = v
        f0v = -np.sin(x)
        x1 = x + f0x*dt/2
        v1 = v + f0v*dt/2
        
        f1x = v1
        f1v = -np.sin(x1)
        x2 = x + f1x*dt/2
        v2 = v + f1v*dt/2
        
        f2x = v2
        f2v = -np.sin(x2)
        x3 = x + f2v*dt
        v3 = v + f2v*dt 
        
        f3x = v3
        f3v = -np.sin(x3)
        
        x = x + (f0x + 2*f1x +2*f2x + f3x)/6*dt
        v = v + (f0v + 2*f1v +2*f2v + f3v)/6*dt
        E = 0.5*m*v**2 - np.cos(x)
        X.append(x)
        V.append(v)
        Energy.append(E)
    return Energy,X,V,Time

energy, distance, velocity, time = harmonic(0,1.99,25,0.001)
plt.plot(time,energy)
plt.plot(time,distance)
plt.plot(time,velocity)
plt.show()