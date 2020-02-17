#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:53:26 2020

@author: zackkingbackup
"""

import json
import numpy as np
import matplotlib.pyplot as plt

import monte_carlo as mc

#########################################
# Execute a Monte Carlo simulation for
# a door-to-door sales campaign with the
# following parameters:
#
# Someone home	= 0.8
# female rate	    = 0.65
# female purchase rate	= 0.3
# female purchase mean	= 22
# female purchase std	5
# male purchase rate	= 0.2
# male purchase mean	= 28
# male purchase std	= 3
#########################################

# Load the parameters from a config file
f = open('params.json','r')
params = json.load(f)
f.close()

# Run the sim 1000 times, see what the distribution of Amount sold is.
all_results = []
for i in range(1000): 
    x = mc.execute_monte_carlo(params, ntrial=100)
    all_results.append(x)

# Find mean, std of amount
# What is P(amount > $750)?
amounts = [df.Amount.sum() for df in all_results]
print("Mean: $%6.2f"%(np.mean(amounts)))
print("Std. Dev: $%5.2f"%(np.std(amounts)))
p750 = mc.get_prob_amount(amounts, 750)
print("P(Amount > $750) = %4.4f"%(p750))

plt.hist(amounts, bins=50)
plt.xlabel("Amount Sold (100 doors)")
plt.ylabel("Probability")
plt.title("Distribution of Amount Sold")  
