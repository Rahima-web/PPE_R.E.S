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
    
GDP_Export_Import_histo = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_GDP_Export_Import.csv")
sns.lineplot(data = GDP_Export_Import_histo)
plt.figure()

Inflation_histo = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Inflation.csv")
sns.lineplot(data = Inflation_histo)
plt.figure()

IRBank_histo = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_IR_Bank_Loans%20.csv")
sns.lineplot(data = IRBank_histo)
plt.figure()

GovSpending_histo = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Govspending.csv")
sns.lineplot(data = GovSpending_histo)
plt.figure()

HouseHoldTaxes_histo = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_HouseHoldTaxes.csv")
sns.lineplot(data = HouseHoldTaxes_histo)
plt.figure()

DTI_histo = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_DTI.csv")
sns.lineplot(data = DTI_histo)
plt.figure()

New_Mortgages_histo = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_New_Mortgages.csv")
sns.lineplot(data = New_Mortgages_histo)
plt.figure()

Mort_Rep_histo = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Mort_Rep.csv")
sns.lineplot(data = Mort_Rep_histo)
plt.figure()

Mortgages_histo = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Mortgages.csv")
sns.lineplot(data = Mortgages_histo)
plt.figure()

Firms_taxes_histo = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Firms%20taxes.csv")
sns.lineplot(data = Firms_taxes_histo)
plt.figure()

Household_Tax_Rate_histo = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Household_Tax_Rate.csv")
sns.lineplot(data = Household_Tax_Rate_histo)
plt.figure()

Deposits_Households_histo = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Deposits%20for%20households.csv")
sns.lineplot(data = Deposits_Households_histo)
plt.figure()

Interest_Rates_Government_Bonds_histo = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Interest_rates_on_government_bonds.csv")
sns.lineplot(data = Interest_Rates_Government_Bonds_histo)
plt.figure()

Housing_Wealth_histo = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Dara_Housing%20Wealth.csv")
sns.lineplot(data = Housing_Wealth_histo)
plt.figure()

Var_Inflation_histo = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Varation_Inflation.csv")
sns.lineplot(data = Var_Inflation_histo)
plt.figure()

LTV_histo = readData_all("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_LTV.csv")
sns.lineplot(data = LTV_histo)
plt.figure()

Housing_Stock_histo = readData_years("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Housing%20stock.csv")
sns.lineplot(data = Housing_Stock_histo)
plt.figure()

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