#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 03:30:57 2023

@author: christophel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
""" La méthode de Newton-Raphson"""

def newton(f, df, x, tol=0.001, maxiter=100):
    """
    f : La fonction à résoudre
    df : la fonction dérivée de f
    x : valeur initiale de x
    tol : La précision de la solution
    maxiter : nombre maximal d'itérations
    return : la valeur de l'axe des abscisses de la racine,
    nombre d'itérations utilisées
    """
    n = 1
    while n <= maxiter:
        x1 = x - f(x)/df(x)
        if abs(x1 - x) < tol:
            return x1, n
        else:
            x = x1
            n += 1
    return None, n