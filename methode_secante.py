#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 22:32:29 2023

@author: christophel
"""

""" Méthode de racine"""
def secante(f, a, b, tol=0.001, maxiter=100):
    """
    f: La fonction à résoudre
    a : Valeur initiale d'estimation de l'axe des x
    b : Valeur initiale d'estimation sur l'axe des x, où b>a
    tol: La précision de la solution
    maxiter : nombre maximal d'itérations
    return : la valeur de l'axe des abscisses de la racine,
    nombre d'itérations utilisées
    """
    n = 1
    while n <= maxiter:
        c = b - f(b)*((b-a)/(f(b)-f(a)))
        if abs(c-b) < tol:
            return c, n
        a = b
        b = c
        n += 1
    return None, n