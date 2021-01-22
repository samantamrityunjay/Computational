import matplotlib.pyplot as plt 
def f(y):
    return 1+y**2


import euler


c=euler.eulerMethod(0,1.55,0,0.02)
print(len(c.X))
y = c.euler(f)
print(len(y))
# plt.plot(c.X,c.euler(f))
plt.plot(c.X,c.modifiedEuler(f))
plt.plot(c.X,c.improvedEuler(f))
plt.plot(c.X,c.RK4(f))
plt.show()