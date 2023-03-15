#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 13:07:34 2023

@author: christophel
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Importance de la linéarité en finance

#Le CAPM définit le rendement du titre comme la somme du taux sans risque
# et de la multiplication de
#son beta avec la prime de risque(ou premium)
#Le beta est une mesure du risk systémique d'un stock
#Il mesure la sensibilité des rendements du stock par rapport 
#aux mouvements du marché


#Regression linéaire avec Scipy

rendements_titre = [0.065, 0.0265, -0.0593, -0.001, 0.0346]
rendements_marché = [0.055, -0.09, -0.041, 0.045, 0.022]

beta, alpha, r_value, p_value, std_err = \
stats.linregress(rendements_titre, rendements_marché)



