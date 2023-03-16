#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 22:41:03 2023

@author: christophel
"""
import pulp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#L'optimisation linéaire vous aide à surmonter 
#le problème de l'allocation de portefeuille.
#L'optimisation se concentre sur la minimisation ou la maximisation de 
#la valeur de la foncton objectif
#On peut utiliser l'algo du simplex avec des packages tiers

#Resoudre un simple problem d'optimisation linéaire en utilisant pulp

x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)
probleme = pulp.LpProblem("Une maximisation simple",
pulp.LpMaximize)
probleme += 3*x + 2*y, "Fonction objectif"
probleme += 2*x + y <= 100, "contrainte 1"
probleme += x + y <= 80, "Contrainte 2"
probleme += x <= 40, "Contrainte 3"
probleme.solve()






