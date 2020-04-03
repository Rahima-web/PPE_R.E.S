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
s = 0.1
i = 0.1
n = len(training)

def predict(x):
    return s * x + i

colonne = []
slope = []   #Stock all the slopes of the different variables
intercept = []   #Stock all the intercepts of the different variables

for col in training:
    Y = training[col]
    axes = plt.axes()
    axes.grid()
    plt.scatter(X,Y)
    s, i, r_value, p_value, std_err = stats.linregress(X, Y)
    colonne.append(col)
    slope.append(s)
    intercept.append(i)
    
    #print r_value * r_value
    fitLine = predict(X)
    plt.plot(X, fitLine, c='r')
    plt.show()

linear_prediction = []
linear_prediction = pd.DataFrame(linear_prediction)
linear_prediction["Name"] = colonne
linear_prediction["Slope"] = slope
linear_prediction["Intercept"] = intercept

####### TEST PHASE ############




