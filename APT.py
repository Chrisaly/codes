#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 21:13:01 2023

@author: christophel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
np.random.seed()


#Le CAPM souffre de plusieurs limites, telles que l'utilisation d'une moyenne-variance
#et le fait que les rendements sont capturés par le risque de marché

#Le modèle APT suppose que les rendements du titre sont générés selon
#les modèles multifactoriels, qui consistent en une combinaison linéaire de plusieurs
#facteurs de risque. Ces facteurs pourraient être le taux d'inflation, 
#le taux de croissance du PIB, le taux d'intérêt réel les taux ou les dividendes.

# Methode des moindres carrés avec statsmodels

#Generation de donnees
nb_periodes=9
valeurs= np.array([np.random.random(8) for i in range(nb_periodes)])

#Filtrer les données

y_valeurs = valeurs[:, 0] # Premiere colone de valeur comme Y
x_valeurs = valeurs[:, 1:] # Toutes les autres valeurs comme X
x_valeurs=sm.add_constant(x_valeurs) #rajouter l'ordonnée à l'origine
resultats = sm.OLS(y_valeurs, x_valeurs).fit() # Réggression et adaptation du modele

#les parametres du modele se trouvent dans resultats.params
#on peut afficher les data en tableau resultats.summary()
print(resultats.params)