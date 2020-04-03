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
import numpy as np

training = f_train.copy()
dt = []
x = training.index
for i in range(len(x)):
    dt.append(datetime.fromisoformat(x[i]).timestamp())

training["time_nb"] = dt


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

training = training.drop("time_nb",axis=1)
for col in training:
    Y = training[col]
    axes = plt.axes()
    axes.grid()
    plt.scatter(X,Y)
    plt.xlabel('time in integer')
    plt.ylabel(col)
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
linear_prediction = linear_prediction.set_index("Name")
####### TEST PHASE ############

test_phase = f_test.copy()
time = []
output = []
output = pd.DataFrame(output)
o = []
x = test_phase.index

for i in range(len(x)):
    time.append(datetime.fromisoformat(x[i]).timestamp())

output["time_nb"] = time

def predict_test(x,s,i):
    return s * x + i

for j in test_phase:
    s = linear_prediction["Slope"][j]
    i = linear_prediction["Intercept"][j]
    for k in range(len(test_phase[j])):
        o.append(predict_test(output["time_nb"][k], s, i))
    output[j] = o
    o = []
    
   
output["Date"] = test_phase.index
output = output.set_index("Date")
X_test = output["time_nb"]
output = output.drop("time_nb", axis=1)

final_output = [f_train, output]
#Final dataframe containing training values and test values
final_output = pd.concat(final_output)

for col in final_output.columns:
    final_output.plot( y=col, marker='.', figsize=(15,7))

########## Calcul MSE ###########

n = 95

def error(y,yhat):
    s= 0
    for i in range(n):
        s += (y[i] - yhat[i])**2
    return np.sqrt(1/n * s)

result_linear = []
for col in f_test:
    result_linear.append([col, error(f_test[col], output[col])])

mse_linear = pd.DataFrame(result_linear, columns = ["Name", "Error"])
mse_linear = mse_linear.set_index("Name")
print(mse_linear)
