#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 01:27:32 2023

@author: christophel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

""" Méthode de recherche incrémentale dans la recherche de racines"""
def recherche_incrementale(f, a, b, dx):
        
    """
    f : La fonction à résoudre
    a : La valeur de l'axe des x de la frontière gauche
    b : La valeur de l'axe des x de la frontière droite
    dx : La valeur incrémentale dans la recherche
    return : La valeur de l'axe des x de la racine,
    le nombre d'itérations utilisées"""
    
    fa = f(a)
    c = a + dx
    fc = f(c)
    n = 1
    while np.sign(fa) == np.sign(fc):
        if a >= b:
            return a - dx, n
        a = c
        fa = fc
        c = a + dx
        fc = f(c)
        n += 1
    if fa == 0:
        return a, n
    elif fc == 0:
        return c, n
    else:
        return (a + c)/2., n
    
#y = lambda x: x**3 + 2.0*x**2 - 5
#racine,iterations = recherche_incrementale(y, -5., 5., 0.001)
