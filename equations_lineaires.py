#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 15:14:28 2023

@author: christophel
"""

import pandas as pd
import numpy as np
import scipy.linalg as linalg
import matplotlib.pyplot as plt

""" Algèbre linéaire avec matrices NumPy """

#A = np.array([[2, 1, 1],[1, 3, 2],[1, 0, 0]])
#B = np.array([4, 5, 6])

"""On veut résoudre Ax=B,on utilise linalg.solve de numpy"""
#print(np.linalg.solve(A, B ))

#Ou
"""Decomposition LU"""
# P, L, U = linalg.lu(A)

#Nous utilisons la méthode linal de scipy pour résoudre l'equation

#LU = linalg.lu_factor(A) 
#x = linalg.lu_solve(LU, B)

#Ou
"""Decomposition de Cholesky avec numpy"""

#C = np.array([[10., -1., 2., 0.],[-1., 11., -1., 3.],[2., -1., 10., -1.],[0.0, 3., -1., 8.]])
#D = np.array([6., 25., -11., 15.])

#L = np.linalg.cholesky(C)

# C=L.L.T (avec T transposée. On veut résoudre Cx=D donc L.L.Tx=D)
#en utilisant le solver on cher y=L.T.X.
#ayant trouvé y on trouve x avec le solver encore"""


#y = np.linalg.solve(L, D)
#Pour résoudre pour x , tout ce que nous avons à faire est de résoudre à nouveau en utilisant la transposée conjuguée de L
#et y
#x = np.linalg.solve(L.T.conj(), y) #solution



"""QR Decomposition"""

#Couramment utilisé pour résoudre des problèmes de moindres carrés

#E = np.array([[2., 1., 1.],[1., 3., 2.],[1., 0., 0]])
#F = np.array([4., 5., 6.])

#Q,R = linalg.qr(E) # Decompose en deux matrices Q,R
#x= linalg.solve(R,np.dot(Q.T,F)) #solution

"""Methode de Jacobi"""

def jacobi(A, B, n, tol=1e-10):
    # Initialise x avec des zéros de même forme et de même type que B
    x = np.zeros_like(B)
    for a in range(n):
        x_nouveau = np.zeros_like(x)
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_nouveau[i] = (B[i] - s1 - s2) / A[i, i]
        if np.allclose(x, x_nouveau, tol):
            break
        x = x_nouveau
    return x

"""Méthode Gauss-Seidel"""
def gauss(A, B, n, tol=1e-10):
    L = np.tril(A) # Returns the lower triangular matrix of A
    U = A - L # Decompose A = L + U
    L_inv = np.linalg.inv(L)
    x = np.zeros_like(B)
    for i in range(n):
        Ux = np.dot(U, x)
        x_new = np.dot(L_inv, B - Ux)
        if np.allclose(x, x_new, tol):
            break
        x = x_new
    return x