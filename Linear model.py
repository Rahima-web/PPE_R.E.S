# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 19:40:45 2020

@author: sagan
"""

#Linear Regression
import matplotlib.pyplot as plt
import pandas as pd
from data_preparation import f_train,f_test
from scipy import stats
from datetime import datetime

training = f_train.copy()
dt = []
x = training.index
for i in range(len(x)):
    dt.append(datetime.fromisoformat(x[i]).timestamp())

training["time_nb"] = dt
print(training)

#Initialisation of X and y
X = training["time_nb"]

#Inintialisation of the slope and the intercept
slope = 0.1
intercept = 0.1
n = len(training)

def predict(x):
    return slope * x + intercept


for col in training:
    Y = training[col]
    axes = plt.axes()
    axes.grid()
    plt.scatter(X,Y)
    slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
    print(slope)
    print(intercept)

    #print r_value * r_value
    fitLine = predict(X)
    plt.plot(X, fitLine, c='r')
    plt.show()


