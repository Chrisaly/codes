#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 03:12:50 2023

@author: christophel
"""

""" The bisection method """
def bissection(f, a, b, tol=0.1, maxiter=10):
    """
    f : La fonction à résoudre
    a : La valeur de l'axe des x où f(a)<0
    b : La valeur de l'axe des x où f(b)>0
    tol : La précision de la solution
    maxiter : Nombre maximal d'itérations
    return : La valeur en abscisse de la racine,
    nombre d'itérations utilisées"""
    
    c = (a+b)*0.5 # centre de ab
    n = 1 # commencer avec 1 itération
    while n <= maxiter:
        c = (a+b)*0.5
        if f(c) == 0 or abs(a-b)*0.5 < tol:
            # la racine est soit trouvée soit très proche
            return c, n
        n += 1
        if f(c) < 0:
            a = c
        else:
            b = c
    return c, n

y = lambda x: x**3 + 2*x**2 - 5
racine, iterations = bissection(y, -5, 5, 0.00001, 100)