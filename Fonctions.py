#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:08:58 2020

@author: HOAREAU.LyseMay
"""
import matplotlib.pyplot as plt
import numpy  as np
import pandas as pd
import seaborn as sns
from datetime import datetime

#Constants

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

#Read Data
def readData(file):
    df = pd.read_csv(file,sep=",",header=0)
    #df['Années'] = [datetime.strptime(x, '%Y') for x in df['Années']]
    #df = pd.DataFrame(data)
    df = df.set_index('Années')
    return(df)
    
GDP_Export_Import_histo = readData("")
sns.lineplot(data = GDP_Export_Import_histo)

Inflation_IR_histo = readData("")
sns.lineplot(data = Inflation_IR_histo)
    
#GDP_histo = readData("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_GDP.csv")
#sns.lineplot(hue="coherence",data = GDP_histo)
#
#Export_histo = readData("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Exportation.csv")
#sns.lineplot(hue="coherence",data = Export_histo)
#
#Import_histo = readData("https://raw.githubusercontent.com/Rahima-web/PPE_R.E.S/master/Data_Importation.csv")
#sns.lineplot(data = Import_histo['Valeurs'])

#Fonctions 
"""
class Household:
    
    def Wages(self, GDP):
        return (1-gamma)*GDP
    
    def Housing_Transaction(self, Delta_Ph):
        return phi1 + phi2*(Delta_Ph)
    
    def Pension(self,Pension_contribution_rate,B_B_ICPF, B_B_ROW, b_B):
        return Pension_contribution_rate *Bank.Bank_Bond_Price(self, B_B_ICPF, B_B_ROW, b_B)
    
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