#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:08:58 2020

@author: HOAREAU.LyseMay
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers.advanced_activations import PReLU

#Constants
"""
theta1 = 4200
theta2 = 0.11
theta3 = 37
gamma = 0.35
S_F = 0.74
rho_G_1 = 0.06
rho_G_2 = -0.027
rho_B_1 = 0.023
rho_B_2 = -0.02
phi1 = 283
phi2 = 8.6
Rs = 2.90
a1 = 0.79
a2 = 0.01

L = 41754836735 
T_F = 24000000000
D_F = 371255000
B_B = 11900000000

"""
#Read Data
def readData_years(file):
    df = pd.read_csv(file,sep=",",header=0)
    df = df.set_index('Years')
    return(df)
    
def readData_all(file):
    df = pd.read_csv(file,sep=",",header=0)  
    df['Years']=[datetime.strptime(x, '%d/%m/%Y') for x in df['Years']]
    df = df.set_index('Years')
    return(df)
    
#Graph historic data
    
GDP_Export_Import = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_GDP_Export_Import.csv")
sns.lineplot(data = GDP_Export_Import)
plt.figure()

Inflation = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Inflation.csv")
sns.lineplot(data = Inflation)
plt.figure()

IRBank = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_IR_Bank_Loans%20.csv")
sns.lineplot(data = IRBank)
plt.figure()

GovSpending = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Govspending.csv")
sns.lineplot(data = GovSpending)
plt.figure()

HouseHoldTaxes = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_HouseHoldTaxes.csv")
sns.lineplot(data = HouseHoldTaxes)
plt.figure()

DTI = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_DTI.csv")
sns.lineplot(data = DTI)
plt.figure()

New_Mortgages = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_New_Mortgages.csv")
sns.lineplot(data = New_Mortgages)
plt.figure()

Mort_Rep = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Mort_Rep.csv")
sns.lineplot(data = Mort_Rep)
plt.figure()

Mortgages = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Mortgages.csv")
sns.lineplot(data = Mortgages)
plt.figure()

Firms_taxes = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Firms%20taxes.csv")
sns.lineplot(data = Firms_taxes)
plt.figure()

Household_Tax_Rate = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Household_Tax_Rate.csv")
sns.lineplot(data = Household_Tax_Rate)
plt.figure()

Deposits_Households = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Deposits%20for%20households.csv")
sns.lineplot(data = Deposits_Households)
plt.figure()

IR_Gov_Bonds = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Interest_rates_on_government_bonds.csv")
sns.lineplot(data = IR_Gov_Bonds)
plt.figure()

Housing_Wealth = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Housing%20Wealth.csv")
sns.lineplot(data = Housing_Wealth)
plt.figure()

Inflation = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Inflation.csv")
sns.lineplot(data = Inflation)
plt.figure()

LTV = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_LTV.csv")
sns.lineplot(data = LTV)
plt.figure()

Housing_Stock = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Housing%20stock.csv")
sns.lineplot(data = Housing_Stock)
plt.figure()

Investment = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Investment.csv")
sns.lineplot(data = Investment)
plt.figure()

ITR = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_ITR.csv")
sns.lineplot(data = ITR)
plt.figure()

B_G = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Nominal%20demand%20for%20GB.csv")
sns.lineplot(data = B_G)
plt.figure()

IR_deposits = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Interest%20rates%20on%20deposits.csv")
sns.lineplot(data = IR_deposits)
plt.figure()

b_G = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Government%20bond.csv")
sns.lineplot(data = b_G)
plt.figure()

IR_Mort = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Interest_Rates_Mortgages_3years.csv")
sns.lineplot(data = IR_Mort)
plt.figure()

b_B = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Bank%20bond%20supply.csv")
sns.lineplot(data = b_B)
plt.figure()

GovTransferTo_H = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Government%20transfer%20to%20households.csv")
sns.lineplot(data = GovTransferTo_H)
plt.figure()

Net_Wealth = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Net%20Wealth.csv")
sns.lineplot(data = Net_Wealth)
plt.figure()

Ann = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Annuity.csv")
sns.lineplot(data = Ann)
plt.figure()

Div_B = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Bank%20Dividend.csv")
sns.lineplot(data = Div_B)
plt.figure()

#Training

def model(df,x_test):
    
    y = []
    
    for el in df.columns:
        y.append(np.ravel(df[el]))
    
    x = np.ravel(df.index)
    y = np.array(y).transpose()
    
    new_y = np.zeros((y.shape[0],y.shape[1]))
    for i in range(y.shape[1]):
        new_y[:,i] = (y[:,i] - y[:,i].mean())/y[:,i].std()
    
    pred = []
    
    model = Sequential()
            
    model.add(Dense(output_dim = 1,init ='uniform',activation = PReLU(),input_shape=(1,)))
    model.add(Dense(output_dim = 1,init ='uniform',activation = PReLU()))
    model.add(Dense(output_dim = 1,init ='uniform',activation = PReLU()))
    model.add(Dense(output_dim = 1,init ='uniform',activation = PReLU()))
    model.add(Dense(output_dim = 1,init ='uniform',activation = PReLU()))
    model.add(Dense(output_dim = 1,init ='uniform',activation = PReLU()))
    model.add(Dense(output_dim = 1,init ='uniform',activation = PReLU()))
            
    model.compile(optimizer = 'adam' , loss = 'mean_squared_error', metrics = ['accuracy'])
    
    for i in range(y.shape[1]):
        model.fit(x,new_y[:,i],batch_size = 10 ,nb_epoch=100) 
        pred.append(model.predict(x_test, batch_size=128))
        
        
    pred = np.array(pred).transpose()
    y_pred = np.zeros((pred.shape[1],pred.shape[2]))  
    for i in range(pred.shape[1]):
        y_pred[:,i] = pred[:,i] * y[:,i].std() + y[:,i].mean()
    
    return y_pred





#Fonctions 
"""
class Household:
    
    def Wages(self, GDP):
        return (1-gamma)*GDP
    
    def Housing_Transaction(self, Delta_Ph):
        return phi1 + phi2*(Delta_Ph)
    
    
class Government:
    
    def Government_Bond_Price(self, B_G_ICPF, B_G_ROW,B_G_CB, b_G):
        return (B_G_ICPF + B_G_ROW + B_G_CB)/b_G
    
    def NetLending_G(self, Tx_H, Tx_F, G, T_H, T_F, i_BG, B_G_ICPF, B_G_ROW):
        return Tx_H + Tx_F - G - T_H - T_F - i_BG*(B_G_ICPF + B_G_ROW)
    
class Bank:
    
    def Bank_Bond_Price(self, B_B_ICPF, B_B_ROW, b_B):
        return (B_B_ICPF + B_B_ROW) / b_B
    
    def Interest_rate_BB(self, i_BG,B_B_ICPF, B_B_ROW, b_B):
        return rho_B_1 + i_BG + rho_B_2 * Bank.Bank_Bond_Price(self,B_B_ICPF, B_B_ROW, b_B)
"""    