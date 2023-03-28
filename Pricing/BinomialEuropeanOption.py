#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 00:50:46 2023

@author: christophel
"""

""" Cette classe hérite de la classe StockOption"""
""" Evalue une option Européenne par le model binomial"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from StockOption import StockOption

class BinomialEuropeanOption(StockOption):
    
    def __setup_parameters__(self):
        """ Required calculations for the model """
        self.M = self.N + 1 # Number of terminal nodes of tree
        self.u = 1 + self.pu # Expected value in the up state
        self.d = 1 - self.pd # Expected value in the down state
        self.qu = (math.exp((self.r-self.div)*self.dt) -
                   self.d) / (self.u-self.d)
        self.qd = 1-self.qu
        
    def _initialize_stock_price_tree_(self):
        # Initialize terminal price nodes to zeros
        self.STs = np.zeros(self.M)
        # Calculate expected stock prices for each node
        for i in range(self.M):
            self.STs[i] = self.S0*(self.u**(self.N-i))*(self.d**i)
            
    def _initialize_payoffs_tree_(self):
        # Get payoffs when the option expires at terminal nodes
        payoffs = np.maximum(0, (self.STs-self.K) if self.is_call else(self.K-self.STs))
        return payoffs
    
    def _traverse_tree_(self, payoffs):
        # Starting from the time the option expires, traverse
        # backwards and calculate discounted payoffs at each node
        for i in range(self.N):
            payoffs = (payoffs[:-1] * self.qu + payoffs[1:] * self.qd) * self.df
        return payoffs
    
    def __begin_tree_traversal__(self):
        payoffs = self._initialize_payoffs_tree_()
        return self._traverse_tree_(payoffs)
    
    def price(self):
        """ The pricing implementation """
        self.__setup_parameters__()
        self._initialize_stock_price_tree_()
        payoffs = self.__begin_tree_traversal__()
        return payoffs[0]
    # Option value converges to first node