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

Pension = pd.DataFrame(alpha * Wages['Wages'])
Pension.columns = ["Pension"]
graph(Pension)

Disposable_Income_H = pd.DataFrame(Wages["Wages"] + df["HouseHold Taxes"] - df["Interest rates Mortgages 3 years (%)"] * df["Mortgages (Million of Livre)"] - Pension["Pension"] - df["Interest rates on deposits (%)"] * df["Deposits for households"] + df["Government transfer to households"] + df["Annuities "])
Disposable_Income_H.columns = ["Disposable Income Households"]
graph(Disposable_Income_H)

Housing_Consumption = pd.DataFrame(a1 * Disposable_Income_H["Disposable Income Households"] + a2 * df["% of net disposable income"] * Disposable_Income_H["Disposable Income Households"])
Housing_Consumption.columns = ["Housing Consumption"]
graph(Housing_Consumption)

Net_Wealth_H = pd.DataFrame(df["Deposits for households"] + df["Total wealth (billion Livres)"] + df["Housing wealth"] - df["Mortgages (Million of Livre)"])
Net_Wealth_H.columns = ["Net Wealth Household"]
graph(Net_Wealth_H)

Housing_Transaction = pd.DataFrame(phi1 + phi2 * df["Variations Inflation (%)"])
Housing_Transaction.columns = ["Housing Transaction"]
graph(Housing_Transaction)

Price_of_House = pd.DataFrame((Rs + df["Debt to Income Ratio (%)"] + Disposable_Income_H["Disposable Income Households"]) / df["Housing stock"])
Price_of_House.columns = ["Price of House"]
graph(Price_of_House)

Nominal_Investment_in_Housing = pd.DataFrame(theta1 + theta2 * (df["Residential mortgage LTV ratio (%)"] * Price_of_House["Price of House"] * Housing_Transaction["Housing Transaction"]) + theta3 * Price_of_House["Price of House"])
Nominal_Investment_in_Housing.columns = ["Nominal Investment in Housing"]
graph(Nominal_Investment_in_Housing)

Demand = pd.DataFrame(Housing_Consumption["Housing Consumption"] + df["Annual business investment (million livre)"] + Nominal_Investment_in_Housing["Nominal Investment in Housing"] + df["Government Spending (% of GDP)"] * df["GDP"] + df["Export"])
Demand.columns = ["Demand"]
graph(Demand)

NLH = pd.DataFrame(Disposable_Income_H["Disposable Income Households"] + Pension["Pension"] - Housing_Consumption["Housing Consumption"] - Nominal_Investment_in_Housing["Nominal Investment in Housing"])
NLH.columns = ["Net Lending Household"]
graph(NLH)

#################A REVOIR#################
NLF = pd.DataFrame(S_F * (Demand["Demand"] + df["Import"] - Wages['Wages'] - Tx_F + T_F - df["Interest rate on bank loans"] * L + df["Interest rates on deposits (%)"] *D_F) - df["Annual business investment (million livre)"])
NLF.columns = ['Net Lending Firm']
graph(NLF)

Government_Bond_Price = pd.DataFrame((df["Nominal demand for GB (ICPF)"] + df["Nominal demand for GB (Rest of the World ou Overseas)"] + df["Nominal demand for GB (CB)"]) / df["UK government bonds issued by Central Government (in sterling millions)"])
Government_Bond_Price.columns = ["Government Bond Price"]
graph(Government_Bond_Price)

#################A REVOIR#################
NLG = pd.DataFrame(df["HouseHold Taxes"] + Tx_F - df["Government Spending (% of GDP)"] * df["GDP"] - df["Government transfer to households"] - T_F - df["Interest rates on government bonds"] * (df["Nominal demand for GB (Rest of the World ou Overseas)"] + df["Nominal demand for GB (ICPF)"] ))
NLG.columns = ["Net Lending Government"]
graph(NLG)

Interest_rate_GB = pd.DataFrame(rho_G_1 + rho_G_2 * Government_Bond_Price["Government Bond Price"] )
Interest_rate_GB.columns = ["Interest rate government bond"]
graph(Interest_rate_GB)

Bank_Bond_Price = pd.DataFrame(B_B / df["Bank bond supply "])
Bank_Bond_Price.columns = ["Bank Bond Price"]
graph(Bank_Bond_Price)

IR_Bank_Bond = pd.DataFrame(rho_B_1 * df["Interest rates on government bonds"] + rho_B_2 * Bank_Bond_Price["Bank Bond Price"])
IR_Bank_Bond.columns = ["Interest Rate Bank Bond"]
graph(IR_Bank_Bond)

NLB = pd.DataFrame(df["Interest rates Mortgages 3 years (%)"] * df["Residential mortgage LTV ratio (%)"] * Price_of_House["Price of House"] * Housing_Transaction["Housing Transaction"] + df["Interest rate on bank loans"] * L - df["Interest rates on deposits (%)"] * (df["Deposits for households"] + D_F) - IR_Bank_Bond["Interest Rate Bank Bond"] * B_B - df["Bank Dividend (in sterling millions)"])
NLB.columns = ["Net Lending Bank"]
graph(NLB)


dfs = [Wages, Pension, Disposable_Income_H, Housing_Consumption, Net_Wealth_H, Housing_Transaction, Price_of_House, Nominal_Investment_in_Housing, Demand, NLH, NLF, Government_Bond_Price, NLG, Interest_rate_GB, Bank_Bond_Price, IR_Bank_Bond, NLB]
dfs = [df.set_index('MonthYear') for df in dfs]

equations = pd.concat([df for df in dfs], join='outer', axis=1)


