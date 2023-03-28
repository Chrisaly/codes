#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 00:50:46 2023

@author: christophel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

""" Stocke les attributs communs d'une option d'achat d'actions """

class StockOption(object):
    
    def __init__(self, S0, K, r, T, N, params):
        self.S0 = S0
        self.K = K
        self.r = r
        self.T = T
        self.N = max(1, N) # S'assurer que N a au moins 1 pas de temps
        self.STs = None # Déclarer l'arbre des cours boursiers
        """ Paramètres optionnels utilisés par les classes dérivées """
        self.pu = params.get("pu", 0) # Probabilité d'état haut
        self.pd = params.get("pd", 0) # Probabilité d'état inactif
        self.div = params.get("div", 0) # Rendement du dividende
        self.sigma = params.get("sigma", 0) # Volatilité
        self.is_call = params.get("est_un_call", True) # Call ou put
        self.is_european = params.get("est_eu", True) # Europeen ou americain
        """ Valeurs calculées """
        self.dt = T/float(N) # Pas de temps unique, en années
        self.df = math.exp(-(r-self.div) * self.dt) # Facteur de remise