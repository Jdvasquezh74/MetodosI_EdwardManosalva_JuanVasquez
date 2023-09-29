# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 16:58:47 2023

@author: jd.vasquezh
"""
from IPython.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from scipy import integrate
sym.init_printing(use_unicode=True)

n = 20
Roots, Weights = np.polynomial.hermite.hermgauss(n)

print(Roots)
print(Weights)
'''
x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)
def GetHermite(n,x,y):
      
    y = sym.exp(-x**2)
    
    poly = (-1)**n*sym.exp(x**2)*sym.diff(y,x,n)
    
    return poly

Hermite = []

for i in range(n+1):
    
    Poly = GetHermite(i,x,y)
    Hermite.append(Poly)

_x = np.linspace(-1,1,100)

for i, p in enumerate(Hermite):
    if i != 0:
        pn = sym.lambdify([x],p,'numpy')
        plt.plot(_x,pn(_x))
f = lambda x: 1/np.sqrt(np.pi) * 2 * x**4
'''