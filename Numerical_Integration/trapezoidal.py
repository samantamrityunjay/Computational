


class Trapezoidal:
    def __init__(self, initial, final, grid_spacing):
        self.a = initial
        self.b = final
        self.N = grid_spacing
            
    def integrate(self, func):
        h = (self.b-self.a)/self.N
        sum = 0 
        for i in range(self.N):
            x_a = self.a + i*h
            x_b = self.a + (i+1)*h
            area = (func(x_a) + func(x_b))*h /2 
            sum += area
        return sum
    