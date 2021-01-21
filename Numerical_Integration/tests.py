import numpy as np

def f(x):
    return 4*(1/(1+x**2))

from trapezoidal import Trapezoidal

inte = Trapezoidal(0,1,1000)

answer = inte.integrate(f)
print(answer)
    