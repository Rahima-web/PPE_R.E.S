#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:08:58 2020

@author: HOAREAU.LyseMay
"""
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import numpy as np


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
    nb_rows = df.shape[0]
    
    # Répéter 12 fois la ligne afin d'obtenir les données en MM/YYYY
    df = df.loc[df.index.repeat(12)]
    df["Month"] = [i for i in range(1,13)] * nb_rows

    df = df.reset_index(drop=True)
    
    df["MonthYear"] = df.Month.map(str) + "/" + df.Years.map(str)
    # Convertir en Datetime
    df["MonthYear"] = pd.to_datetime(df["MonthYear"], format="%m/%Y")
    return(df)
    
def readData_all(file):
    df = pd.read_csv(file,sep=",",header=0)  
    df['MonthYear']=[datetime.strptime(x, '%d/%m/%Y') for x in df['Years']]
    df = df.set_index('Years')
    return(df)
    
#Graph historic data
GDP_Export_Import = readData_years("./Data/Data_GDP_Export_Import.csv")
GDP_Export_Import = GDP_Export_Import.drop("Years", axis=1)
GDP_Export_Import = GDP_Export_Import.drop("Month", axis=1)
GDP_Export_Import["GDP"] = GDP_Export_Import["GDP"] / 12
GDP_Export_Import["Export"] = GDP_Export_Import["Export"] / 12
GDP_Export_Import["Import"] = GDP_Export_Import["Import"] / 12
#GDP_Export_Import.plot(x="MonthYear", subplots=True)
#plt.figure

Inflation = readData_years("./Data/Data_Inflation.csv")
Inflation = Inflation.drop("Years", axis=1)
Inflation = Inflation.drop("Month", axis=1)
#Inflation.plot(x="MonthYear", subplots=True)
#plt.figure


IRBank = readData_years("./Data/Data_IR_Bank_Loans .csv")
IRBank = IRBank.drop("Years", axis=1)
IRBank = IRBank.drop("Month", axis=1)
#IRBank.plot(x="MonthYear", subplots=True)
#plt.figure

GovSpending = readData_years("./Data/Data_Govspending.csv")
GovSpending = GovSpending.drop("Years", axis=1)
GovSpending = GovSpending.drop("Month", axis=1)

#GovSpending.plot(x="MonthYear", subplots=True)
#plt.figure

HouseHoldTaxes = readData_years("./Data/Data_HouseHoldTaxes.csv")
HouseHoldTaxes = HouseHoldTaxes.drop("Years", axis=1)
HouseHoldTaxes = HouseHoldTaxes.drop("Month", axis=1)
#HouseHoldTaxes.plot(x="MonthYear", subplots=True)
#plt.figure

#######C'est tout les 3 mois PB##
DtI = readData_all("./Data/Data_DTI.csv")
#DtI.plot(x = "MonthYear",subplots=True)
#plt.figure

New_Mortgages = readData_all("./Data/Data_New_Mortgages.csv")
#New_Mortgages.plot(x = "MonthYear",subplots=True)
#plt.figure

#######C'est tout les 3 mois PB####
Mort_Rep = readData_all("./Data/Data_Mort_Rep.csv")
#Mort_Rep.plot(x = "MonthYear",subplots=True)
#plt.figure

Mortgages = readData_all("./Data/Data_Mortgages.csv")
#Mortgages.plot( x = "MonthYear", subplots=True)
#plt.figure

Firms_taxes = readData_years("./Data/Data_Firms taxes.csv")
Firms_taxes = Firms_taxes.drop("Years", axis=1)
Firms_taxes = Firms_taxes.drop("Month", axis=1)
#Firms_taxes.plot(x="MonthYear", subplots=True)
#plt.figure

Household_Tax_Rate = readData_years("./Data/Data_Household_Tax_Rate.csv")
Household_Tax_Rate = Household_Tax_Rate.drop("Years", axis=1)
Household_Tax_Rate = Household_Tax_Rate.drop("Month", axis=1)
#Household_Tax_Rate.plot(x="MonthYear", subplots=True)
#plt.figure

Deposits_Households = readData_years("./Data/Data_Deposits for households.csv")
Deposits_Households = Deposits_Households.drop("Years", axis=1)
Deposits_Households = Deposits_Households.drop("Month", axis=1)
Deposits_Households["Deposits for households"] = Deposits_Households["Deposits for households"] / 12
#Deposits_Households.plot(x="MonthYear", subplots=True)
#plt.figure



IR_Gov_Bonds = readData_all("./Data/Data_Interest_rates_on_government_bonds.csv")
#IR_Gov_Bonds.plot( x = "MonthYear", subplots=True)
#plt.figure

Housing_Wealth = readData_years("./Data/Data_Housing Wealth.csv")
Housing_Wealth = Housing_Wealth.drop("Years", axis=1)
Housing_Wealth = Housing_Wealth.drop("Month", axis=1)
Housing_Wealth["Housing wealth"] = Housing_Wealth["Housing wealth"] / 12
#Housing_Wealth.plot(x="MonthYear", subplots=True)
#plt.figure

#######C'est tout les 3 mois PB#########
LtV = readData_all("./Data/Data_LTV.csv")
#LtV.plot(x = "MonthYear",subplots=True)
#plt.figure

Housing_Stock = readData_years("./Data/Data_Housing stock.csv")
Housing_Stock = Housing_Stock.drop("Years", axis=1)
Housing_Stock = Housing_Stock.drop("Month", axis=1)
Housing_Stock["Housing stock"] = Housing_Stock["Housing stock"] / 12
#Housing_Stock.plot(x="MonthYear", subplots=True)
#plt.figure

Investment = readData_years("./Data/Data_Investment.csv")
Investment = Investment.drop("Years", axis=1)
Investment = Investment.drop("Month", axis=1)
Investment["Annual business investment (million livre)"] = Investment["Annual business investment (million livre)"] / 12
#Investment.plot(x="MonthYear", subplots=True)
#plt.figure

ItR = readData_years("./Data/Data_ITR.csv")
ItR = ItR.drop("Years", axis=1)
ItR = ItR.drop("Month", axis=1)
ItR["Private pension wealth (billion Livres)"] = ItR["Private pension wealth (billion Livres)"] / 12
ItR["Total wealth (billion Livres)"] = ItR["Total wealth (billion Livres)"] /12
#ItR.plot(x="MonthYear", subplots=True)
#plt.figure

G_b = readData_years("./Data/Data_Nominal demand for GB.csv")
G_b = G_b.drop("Years", axis=1)
G_b = G_b.drop("Month", axis=1)
G_b["GDP"] = G_b["GDP"] /12
G_b["UK National debt en Livres"] = G_b["UK National debt en Livres"] /12
G_b["Nominal demand for GB (ICPF)"] = G_b["Nominal demand for GB (ICPF)"] / 12
G_b["Nominal demand for GB (Rest of the World ou Overseas)"] = G_b["Nominal demand for GB (Rest of the World ou Overseas)"] / 12
G_b["Nominal demand for GB (CB)"] = G_b["Nominal demand for GB (CB)"] / 12
G_b = G_b.drop("GDP", axis=1)
#G_b.plot(x="MonthYear", subplots=True)
#plt.figure

IR_deposits = readData_all("./Data/Data_Interest rates on deposits.csv")
#IR_deposits.plot(x = "MonthYear",subplots=True)
#plt.figure

b_G = readData_all("./Data/Data_Government bond.csv")
#b_G.plot(x = "MonthYear, subplots=True)
#plt.figure

IR_Mort = readData_all("./Data/Data_Interest_Rates_Mortgages_3years.csv")
#IR_Mort.plot(x = "MonthYear, subplots=True)
#plt.figure

b_B = readData_years("./Data/Data_Bank bond supply.csv")
b_B = b_B.drop("Years", axis=1)
b_B = b_B.drop("Month", axis=1)
b_B["Bank bond supply "] = b_B["Bank bond supply "] / 12
#b_B.plot(x="MonthYear", subplots=True)
#plt.figure

GovTransferTo_H = readData_years("./Data/Data_Government transfer to households.csv")
GovTransferTo_H = GovTransferTo_H.drop("Years", axis=1)
GovTransferTo_H = GovTransferTo_H.drop("Month", axis=1)
GovTransferTo_H["GDP"] = GovTransferTo_H["GDP"] / 12
GovTransferTo_H["Government transfer to households"] = GovTransferTo_H["Government transfer to households"] / 12
GovTransferTo_H = GovTransferTo_H.drop("GDP", axis=1)
#GovTransferTo_H.plot(x="MonthYear", subplots=True)
#plt.figure

Net_Wealth = readData_years("./Data/Data_Net Wealth.csv")
Net_Wealth = Net_Wealth.drop("Years", axis=1)
Net_Wealth = Net_Wealth.drop("Month", axis=1)
#Net_Wealth.plot(x="MonthYear", subplots=True)
#plt.figure

Ann = readData_years("./Data/Data_Annuity.csv")
Ann = Ann.drop("Years", axis=1)
Ann = Ann.drop("Month", axis=1)
Ann["Annuities "] = Ann["Annuities "] / 12
#Ann.plot(x="MonthYear", subplots=True)
#plt.figure

Div_B = readData_years("./Data/Data_Bank Dividend.csv")
Div_B = Div_B.drop("Years", axis=1)
Div_B = Div_B.drop("Month", axis=1)
Div_B["Bank Dividend (in sterling millions)"] = Div_B["Bank Dividend (in sterling millions)"] / 12
#Div_B.plot(x="MonthYear", subplots=True)
plt.figure


dfs = [GDP_Export_Import,Inflation,IRBank, GovSpending, HouseHoldTaxes, DtI, New_Mortgages, Mort_Rep, Mortgages, Firms_taxes, Household_Tax_Rate, Deposits_Households, IR_Gov_Bonds, Housing_Wealth, LtV, Housing_Stock, Investment, ItR, G_b, IR_deposits, b_G, IR_Mort, b_B, GovTransferTo_H, Net_Wealth, Ann, Div_B ]
dfs = [df.set_index('MonthYear') for df in dfs]
dfs[0].join(dfs[1:])
print("Voilaaaaaa")
print(dfs)

#import sys
#sys.exit()


