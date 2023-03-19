#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 00:56:10 2023

@author: christophel
"""

import pulp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#x = pulp.LpVariable("x", lowBound=0)
#y = pulp.LpVariable("y", lowBound=0)
#z = pulp.LpVariable("z", lowBound=0)

#probleme=pulp.LpProblem("Simple probleme d'optimization",pulp.LpMinimize)
#probleme += 500*x + 350*y + 450*z + 12000, "Fonction objectif"
#probleme += 30 <= x <= 100, "contrainte 1"
#probleme += 30 <= y <= 90, "Contrainte 2"
#probleme += 30 <= z <= 70, "Contrainte 3"
#probleme += x+y+z == 150, "Contrainte 4"
#probleme.solve()

#print(pulp.value(probleme.objective))

negociants = ["X", "Y", "Z"]
prix_contrat = {"X": 500,"Y": 350,"Z": 450}
frais = {"X": 4000,"Y": 2000,"Z": 6000}

quantites = pulp.LpVariable.dicts("quantite",negociants,lowBound=0,cat=pulp.LpInteger)
commandes = pulp.LpVariable.dicts("ordres",negociants,cat=pulp.LpBinary)

modele = pulp.LpProblem("Un probleme de minimisatio de couts",
pulp.LpMinimize)
modele += sum([prix_contrat[i]*quantites[i] +
frais[i]*commandes[i] for i in negociants]), \
"Minimiser le cout du portefeuille"
modele += sum([quantites[i] for i in negociants]) == 150, \
"nombre total de contrats"
modele += commandes["X"]*30 <= quantites["X"] <= \
commandes["X"]*100, "Limite du volume total de X"
modele += commandes["Y"]*30 <= quantites["Y"] <= \
commandes["Y"]*90, "Limite du volume total de Y"
modele += commandes["Z"]*30 <= quantites["Z"] <= \
commandes["Z"]*70, "Limite du volume total de Z"
modele.solve()









