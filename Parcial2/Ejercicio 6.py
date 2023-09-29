# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from IPython.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

class Integrator:
    
    def __init__(self,x,f):
        
        self.x = x
        self.h = self.x[1] - self.x[0]
        self.y = f(self.x)
        
        self.Integral = 0.

class Simpson(Integrator):
    
    def __init__(self,x,f):
        Integrator.__init__(self,x,f)
        
    def GetIntegral(self):
        
        self.Integral = 0.
        
        self.Integral += self.y[0] + self.y[-1]
        
        for i in range( len(self.y[1:-1]) ):
            
            if i%2 == 0:
                self.Integral += 4*self.y[i+1]
            else:
                self.Integral += 2*self.y[i+1]
          
        return self.Integral*self.h/3
    
a = 0.01
R = 0.5
f = lambda x: np.sqrt(a**2-x**2)/(R+x)
N = 300 
x = np.linspace(-a,a,N)

Integrador = Simpson(x,f)
ResultadoAproximado = Integrador.GetIntegral()
ResultadoExacto = np.pi*(R-np.sqrt(R**2-a**2))
print("Resultado Aproximado Integral: "+str(ResultadoAproximado))
print("Resultado Exacto Integral: "+str(ResultadoExacto))
print("Error: "+str(round((abs(ResultadoAproximado-ResultadoExacto))/ResultadoExacto*100,3))+"%")