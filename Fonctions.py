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
    f = df.to_dict(orient = 'index')
    return(df,f)
    
def readData_all(file):
    df = pd.read_csv(file,sep=",",header=0)  
    df['Years']=[datetime.strptime(x, '%d/%m/%Y') for x in df['Years']]
    df = df.set_index(orient = 'Years')
    f = df.to_dict()
    return(df,f)
    
GDP_Export_Import,GDP_Export_Import_dic = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_GDP_Export_Import.csv")
sns.lineplot(data = GDP_Export_Import)
plt.figure()

Inflation,Inflation_dic= readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Inflation.csv")
sns.lineplot(data = Inflation)
plt.figure()

IRBank,IRBank_dic= readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_IR_Bank_Loans%20.csv")
sns.lineplot(data = IRBank)
plt.figure()

GovSpending,GovSpending_dic = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Govspending.csv")
sns.lineplot(data = GovSpending)
plt.figure()

HouseHoldTaxes,HouseHoldTaxes_dic = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_HouseHoldTaxes.csv")
sns.lineplot(data = HouseHoldTaxes)
plt.figure()

DTI,DTI_dic = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_DTI.csv")
sns.lineplot(data = DTI)
plt.figure()

New_Mortgages,New_Mortgages_dic= readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_New_Mortgages.csv")
sns.lineplot(data = New_Mortgages)
plt.figure()

Mort_Rep,Mort_Rep_dic = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Mort_Rep.csv")
sns.lineplot(data = Mort_Rep)
plt.figure()

Mortgages,Mortgages_dic = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Mortgages.csv")
sns.lineplot(data = Mortgages)
plt.figure()

Firms_taxes,Firms_taxes_dic= readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Firms%20taxes.csv")
sns.lineplot(data = Firms_taxes)
plt.figure()

Household_Tax_Rate,Household_Tax_Rate_dic = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Household_Tax_Rate.csv")
sns.lineplot(data = Household_Tax_Rate)
plt.figure()

Deposits_Households,Deposits_Households_dic = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Deposits%20for%20households.csv")
sns.lineplot(data = Deposits_Households)
plt.figure()

IR_Gov_Bonds,IR_Gov_Bonds_dic= readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Interest_rates_on_government_bonds.csv")
sns.lineplot(data = IR_Gov_Bonds)
plt.figure()

Housing_Wealth,Housing_Wealth_dic= readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Housing%20Wealth.csv")
sns.lineplot(data = Housing_Wealth)
plt.figure()

Inflation,Inflation_dic = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Inflation.csv")
sns.lineplot(data = Inflation)
plt.figure()

LTV,LTV_dic= readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_LTV.csv")
sns.lineplot(data = LTV)
plt.figure()

Housing_Stock, Housing_Stock_dic= readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Housing%20stock.csv")
sns.lineplot(data = Housing_Stock)
plt.figure()

Investment,Investment_dic= readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Investment.csv")
sns.lineplot(data = Investment)
plt.figure()

ITR,ITR_dic = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_ITR.csv")
sns.lineplot(data = ITR)
plt.figure()

B_G,B_G_dic = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Nominal%20demand%20for%20GB.csv")
sns.lineplot(data = B_G)
plt.figure()

IR_deposits,IR_deposits_dic = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Interest%20rates%20on%20deposits.csv")
sns.lineplot(data = IR_deposits)
plt.figure()

b_G,b_G_dic = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Government%20bond.csv")
sns.lineplot(data = b_G)
plt.figure()

IR_Mort,IR_Mort_dic= readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Interest_Rates_Mortgages_3years.csv")
sns.lineplot(data = IR_Mort)
plt.figure()

b_B,b_B_dic= readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Bank%20bond%20supply.csv")
sns.lineplot(data = b_B)
plt.figure()

GovTransferTo_H,GovTransferTo_H_dic = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Government%20transfer%20to%20households.csv")
sns.lineplot(data = GovTransferTo_H)
plt.figure()

Net_Wealth,Net_Wealth_dic= readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Net%20Wealth.csv")
sns.lineplot(data = Net_Wealth)
plt.figure()

Ann,Ann_dic = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Annuity.csv")
sns.lineplot(data = Ann)
plt.figure()

Div_B,Div_B_dic = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Bank%20Dividend.csv")
sns.lineplot(data = Div_B)
plt.figure()
'''
import keras
from keras.models import Sequential

model = Sequential()

from keras.layers import Dense

model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
optimizer='sgd',
metrics=['accuracy'])

model.compile(loss=keras.losses.categorical_crossentropy,
optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True))

model.fit(GDP_Export_Import_histo['Index'], GDP_Export_Import_histo['GDP'], epochs=2, batch_size=32)

'''

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