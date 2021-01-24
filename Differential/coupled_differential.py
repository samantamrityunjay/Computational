import numpy as np
import matplotlib.pyplot as plt

number_of_particles = 50
T = 100
dt = 0.01
Time = np.array([i*dt for i in range(int(T/dt)+1)],dtype="float32")
Y = []
V_y = []

y = np.zeros(number_of_particles)
v = np.zeros(number_of_particles)

y[0]=0.3

f0y = np.zeros(number_of_particles)
f0v = np.zeros(number_of_particles)
f1y = np.zeros(number_of_particles)
f1v =np.zeros(number_of_particles)
f2y= np.zeros(number_of_particles)
f2v =np.zeros(number_of_particles)
f3y = np.zeros(number_of_particles)
f3v = np.zeros(number_of_particles)
y1 = np.zeros(number_of_particles)
v1 = np.zeros(number_of_particles)
y2 = np.zeros(number_of_particles)
v2 = np.zeros(number_of_particles)
y3 = np.zeros(number_of_particles)
v3 = np.zeros(number_of_particles)

Y.append(y)
V_y.append(v)

for t in range(int(T/dt)):
    for i in range(number_of_particles):
        i_0 = i-1
        i_1 = i+1
        if i == 0:
            i_0 = number_of_particles-1
        if i == number_of_particles-1 :
            i_1 = 0
        f0y[i] = v[i]
        f0v[i] = -(y[i_1] + y[i_0] - 2*y[i])
        
    # for i in range(number_of_particles):
    
    #     y1[i] = x + f0x*dt/2
    #     v1 = v + f0v*dt/2
    
    y1 = y + f0y*dt/2
    v1 = v + f0v*dt/2
    
    for i in range(number_of_particles):
        i_0 = i-1
        i_1 = i+1
        if i == 0:
            i_0 = number_of_particles-1
        if i == number_of_particles-1 :
            i_1 = 0
        f1y[i] = v1[i]
        f1v[i] = -(y1[i_1] + y1[i_0] - 2*y1[i])
        
    y2 = y + f1y*dt/2
    v2 = v + f1v*dt/2
    
    for i in range(number_of_particles):
        i_0 = i-1
        i_1 = i+1
        if i == 0:
            i_0 = number_of_particles-1
        if i == number_of_particles-1 :
            i_1 = 0
        f2y[i] = v2[i]
        f2v[i] = -(y2[i_1] + y2[i_0] - 2*y2[i])
    
    y3 = y + f2y*dt
    v3 = v + f2v*dt
    
    for i in range(number_of_particles):
        i_0 = i-1
        i_1 = i+1
        if i == 0:
            i_0 = number_of_particles-1
        if i == number_of_particles-1 :
            i_1 = 0
        f3y[i] = v3[i]
        f3v[i] = -(y3[i_1] + y3[i_0] - 2*y3[i])
       
    y = y + (f0y + 2*f1y + 2*f2y + f3y)/6*dt
    v = v + (f0v + 2*f1v + 2*f2v + f3v)/6*dt
    
    Y.append(y)
    V_y.append(v)
    
print(len(Time),len(Y),len(V_y))

two_pi = 4*np.arcsin(1.0)
theta = two_pi/number_of_particles
X = np.array([5*np.sin(i*theta) for i in range(number_of_particles)],dtype="float32")
Z = np.array([5*np.cos(i*theta) for i in range(number_of_particles)],dtype="float32")

fig, ax = plt.subplots()
ax = plt.axes(projection ='3d')
for t in range(int(T/dt)+1):
    ax.plot(X,Y[t],Z,marker = 'o', linestyle='None')
    plt.pause(0.00001)