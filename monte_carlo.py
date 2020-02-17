#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:57:16 2020

@author: zackkingbackup
"""

import numpy as np
import pandas as pd
import random


def execute_monte_carlo(params, ntrial=1000):
    '''
    This function runs the Monte Carlo simulation given
    parameters (probabilities) and a number of trials
    
    Params
    ------
    params : dict
        Dictionary where keys are the names of the necessary
        probabilities and the values are the probabilities
    ntrial : int
        Number of trials to run
    
    Returns
    -------
    pd.DataFrame
        All values generated for each sim is contained in the dataframe
    '''
    
    rows = [run_trial(visit, params) for visit in np.arange(1,ntrial+1)]
    df_data = {}
    for idx, col in enumerate(['Visit','Answers_Door','Gender',
                               'Purchase','Amount']):
        df_data[col] = [row[idx] for row in rows]
    
    return pd.DataFrame(df_data)
    

def run_trial(visit, params):
    
    # Is someone home?
    # If a uniform random number is less than params['home'], then yes
    someone_home = random.random() < params['home']
    
    # If no one answered, nothing will be sold, return 0s
    if not someone_home: return (visit,0,'None',0,0)
    
    # If so, what gender?
    if random.random() < params['female']:
        gender = 'Female'
    else:
        gender = 'Male'
        
    # Determine probability of a purchase by gender
    # as well as the mean/std of purchases
    if gender == 'Female':
        purchase_prob = params['female_purchase']
        purchase_mean = params['female_mean']
        purchase_std = params['female_std']
    else:
        purchase_prob = params['male_purchase']
        purchase_mean = params['male_mean']
        purchase_std = params['male_std']
    
    # Was a purchase made?
    purchase = random.random() < purchase_prob
    
    # If not, return 0s
    if not purchase: return (visit,1,gender,0,0)
    
    # If so, calculate the amount
    amount = random.normalvariate(purchase_mean, purchase_std)
    
    # Convert someone_home, purchase to binary from boolean
    someone_home = bool2bin(someone_home)
    purchase = bool2bin(someone_home)
    
    return (visit,someone_home,gender,purchase,amount)


def bool2bin(x):
    '''
    Map True to 1; False to 0
    '''
    if x:
        return 1
    return 0


def get_prob_amount(amounts, value):
    '''
    Given a list-like object for amounts, return the probabilty
    that an amount over value will occur.
    '''
    over_amount = 0
    for amount in amounts:
        if amount >= value:
            over_amount += 1
    
    return over_amount/len(amounts)
    
    