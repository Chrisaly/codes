#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:56:00 2023

@author: christophel
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from StockOption import StockOption

""" Prix d'une option européenne ou américaine par l'arbre binomial """

class BinomialTreeOption(StockOption):
    
    def __setup_parameters__(self):
        """ Calculs requis pour le modèle """
        self.u = 1 + self.pu # Expected value in the up state
        self.d = 1 - self.pd # Expected value in the down state
        self.qu = (math.exp((self.r-self.div)*self.dt) -
                   self.d) / (self.u-self.d)
        self.qd = 1-self.qu
    def _initialize_stock_price_tree_(self):
        # Initialiser un arbre 2D à T=0
        self.STs = [np.array([self.S0])]
        # Simuler le chemin possible des cours des actions
        for i in range(self.N):
            prev_branches = self.STs[-1]
            st = np.concatenate((prev_branches*self.u,[prev_branches[-1]*self.d]))
            self.STs.append(st) # Add nodes at each time step
    
    def _initialize_payoffs_tree_(self):
        # Les gains à l'expiration de l'option
        return np.maximum(0, (self.STs[self.N]-self.K) if self.is_call else (self.K-self.STs[self.N]))

    def __check_early_exercise__(self, payoffs, node):
        early_ex_payoff = \
            (self.STs[node] - self.K) if self.is_call \
            else (self.K - self.STs[node])
        return np.maximum(payoffs, early_ex_payoff)
    
    def _traverse_tree_(self, payoffs):
        for i in reversed(range(self.N)):
            # The payoffs from NOT exercising the option
            payoffs = (payoffs[:-1] * self.qu +
                       payoffs[1:] * self.qd) * self.df
            # Payoffs from exercising, for American options
            if not self.is_european:
                payoffs = self.__check_early_exercise__(payoffs,i)
        return payoffs
    
    def __begin_tree_traversal__(self):
        payoffs = self._initialize_payoffs_tree_()
        return self._traverse_tree_(payoffs)
    
    def price(self):
        self._setup_parameters_()
        self._initialize_stock_price_tree_()
        payoffs = self.__begin_tree_traversal__()
        return payoffs[0]