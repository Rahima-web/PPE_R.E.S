#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:24:37 2020

@author: HOAREAU.LyseMay
"""
from data_preparation import final_dataframe
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

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
Tx_F = 19./100
alpha = 6.5/100

L = 41754836735 
T_F = 24000000000
D_F = 371255000
B_B = 11900000000

#Graphe des données

def graph(df):
    sns.lineplot(data = df)
    plt.figure()

df = final_dataframe.copy()

#Équations

Wages = pd.DataFrame((1 - gamma) * df["GDP"])
Wages.columns = ['Wages']
graph(Wages)

Housing_Transaction = pd.DataFrame(phi1 + phi2 * df["Variations Inflation (%)"])
Housing_Transaction.columns = ["Housing Transaction"]
graph(Housing_Transaction)

Government_Bond_Price = pd.DataFrame((df["Nominal demand for GB (ICPF)"] + df["Nominal demand for GB (Rest of the World ou Overseas)"] + df["Nominal demand for GB (CB)"]) / df["UK government bonds issued by Central Government (in sterling millions)"])
Government_Bond_Price.columns = ["Government Bond Price"]
graph(Government_Bond_Price)

NLG = pd.DataFrame(df["HouseHold Taxes"] + Tx_F - df["Government Spending (% of GDP)"] * df["GDP"] - df["Government transfer to households"] - T_F - df["Interest rates on government bonds"] * (df["Nominal demand for GB (Rest of the World ou Overseas)"] + df["Nominal demand for GB (ICPF)"] ))
NLG.columns = ["Net Lending Government"]
graph(NLG)

Bank_Bond_Price = pd.DataFrame(B_B / df["Bank bond supply "])
Bank_Bond_Price.columns = ["Bank Bond Price"]
graph(Bank_Bond_Price)

IR_Bank_Bond = pd.DataFrame(rho_B_1 * df["Interest rates on government bonds"] + rho_B_2 * Bank_Bond_Price["Bank Bond Price"])
IR_Bank_Bond.columns = ["Interest Rate Bank Bond"]
graph(IR_Bank_Bond)

Pension = pd.DataFrame(alpha * Wages['Wages'])
Pension.columns = ["Pension"]
graph(Pension)

Disposable_Income_H = pd.DataFrame(Wages["Wages"] + df["HouseHold Taxes"] - df["Interest rates Mortgages 3 years (%)"] * df["Mortgages (Million of Livre)"] - Pension["Pension"] - df["Interest rates on deposits (%)"] * df["Deposits for households"] + df["Government transfer to households"] + df["Annuities "])
Disposable_Income_H.columns = ["Disposable Income Households"]
graph(Disposable_Income_H)