#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:08:58 2020

@author: HOAREAU.LyseMay
"""

import pandas as pd
from datetime import datetime

#Read Data
def readData_years(file):
    df = pd.read_csv(file,sep=",",header=0)
    nb_rows = df.shape[0]
    
    # Répéter 12 fois la ligne afin d'obtenir les données en MM/YYYY
    df = df.loc[df.index.repeat(12)]
    df["Month"] = [i for i in range(1,13)] * nb_rows

    df = df.reset_index(drop=True)
    
    df["Date"] = df.Month.map(str) + "/" + df.Years.map(str)
    # Convertir en Datetime
    df["Date"] = pd.to_datetime(df["Date"], format="%m/%Y")
    df = df.drop("Years", axis=1)
    df = df.drop("Month", axis=1)
    
    return(df)
    
def readData_all(file):
    df = pd.read_csv(file,sep=",",header=0)
    df['Date']=[datetime.strptime(x, '%m/%Y') for x in df['Years'].str.slice(3,10)]
    df = df.drop("Years", axis=1)
    return(df)
    
#Graph historic data
GDP_Export_Import = readData_years("./Data/Data_GDP_Export_Import.csv")

GDP_Export_Import["GDP"] = GDP_Export_Import["GDP"] / 12
GDP_Export_Import["Export"] = GDP_Export_Import["Export"] / 12
GDP_Export_Import["Import"] = GDP_Export_Import["Import"] / 12


Inflation = readData_years("./Data/Data_Inflation.csv")

IRBank = readData_years("./Data/Data_IR_Bank_Loans .csv")

GovSpending = readData_years("./Data/Data_Govspending.csv")

HouseHoldTaxes = readData_years("./Data/Data_HouseHoldTaxes.csv")


#######C'est tout les 3 mois PB##
DtI = readData_all("./Data/Data_DTI.csv")

New_Mortgages = readData_all("./Data/Data_New_Mortgages.csv")

#######C'est tout les 3 mois PB####
Mort_Rep = readData_all("./Data/Data_Mort_Rep.csv")

Mortgages = readData_all("./Data/Data_Mortgages.csv")

Firms_taxes = readData_years("./Data/Data_Firms taxes.csv")

Household_Tax_Rate = readData_years("./Data/Data_Household_Tax_Rate.csv")

Deposits_Households = readData_years("./Data/Data_Deposits for households.csv")
Deposits_Households.rename(columns={'Deposits for households ': 'Deposits for households'}, inplace=True)
Deposits_Households["Deposits for households"] = Deposits_Households["Deposits for households"] / 12

IR_Gov_Bonds = readData_all("./Data/Data_Interest_rates_on_government_bonds.csv")

Housing_Wealth = readData_years("./Data/Data_Housing Wealth.csv")
Housing_Wealth["Housing wealth"] = Housing_Wealth["Housing wealth"] / 12


#######C'est tout les 3 mois PB#########
LtV = readData_all("./Data/Data_LTV.csv")

Housing_Stock = readData_years("./Data/Data_Housing stock.csv")
Housing_Stock["Housing stock"] = Housing_Stock["Housing stock"] / 12

Investment = readData_years("./Data/Data_Investment.csv")
Investment["Annual business investment (million livre)"] = Investment["Annual business investment (million livre)"] / 12

ItR = readData_years("./Data/Data_ITR.csv")
ItR["Private pension wealth (billion Livres)"] = ItR["Private pension wealth (billion Livres)"] / 12
ItR["Total wealth (billion Livres)"] = ItR["Total wealth (billion Livres)"] /12

G_b = readData_years("./Data/Data_Nominal demand for GB.csv")
G_b["GDP"] = G_b["GDP"] /12
G_b["UK National debt en Livres"] = G_b["UK National debt en Livres"] /12
G_b["Nominal demand for GB (ICPF)"] = G_b["Nominal demand for GB (ICPF)"] / 12
G_b["Nominal demand for GB (Rest of the World ou Overseas)"] = G_b["Nominal demand for GB (Rest of the World ou Overseas)"] / 12
G_b["Nominal demand for GB (CB)"] = G_b["Nominal demand for GB (CB)"] / 12
G_b = G_b.drop("GDP", axis=1)

IR_deposits = readData_all("./Data/Data_Interest rates on deposits.csv")

b_G = readData_all("./Data/Data_Government bond.csv")

IR_Mort = readData_all("./Data/Data_Interest_Rates_Mortgages_3years.csv")

b_B = readData_years("./Data/Data_Bank bond supply.csv")
b_B["Bank bond supply "] = b_B["Bank bond supply "] / 12

GovTransferTo_H = readData_years("./Data/Data_Government transfer to households.csv")
GovTransferTo_H["GDP"] = GovTransferTo_H["GDP"] / 12
GovTransferTo_H["Government transfer to households"] = GovTransferTo_H["Government transfer to households"] / 12
GovTransferTo_H = GovTransferTo_H.drop("GDP", axis=1)

Net_Wealth = readData_years("./Data/Data_Net Wealth.csv")

Ann = readData_years("./Data/Data_Annuity.csv")
Ann["Annuities "] = Ann["Annuities "] / 12

Div_B = readData_years("./Data/Data_Bank Dividend.csv")
Div_B["Bank Dividend (in sterling millions)"] = Div_B["Bank Dividend (in sterling millions)"] / 12


dfs = [GDP_Export_Import,Inflation,IRBank, GovSpending, HouseHoldTaxes, DtI, New_Mortgages, Mort_Rep, Mortgages, Firms_taxes, Household_Tax_Rate, Deposits_Households, IR_Gov_Bonds, Housing_Wealth, LtV, Housing_Stock, Investment, ItR, G_b, IR_deposits, b_G, IR_Mort, b_B, GovTransferTo_H, Net_Wealth, Ann, Div_B ]
dfs = [df.set_index('Date') for df in dfs]


#Notre dataframe train s'appelle f_train
final_dataframe = pd.concat([df for df in dfs], join='outer', axis=1)
final = final_dataframe[1380:1668]
final_train = final[:192]

final_train.to_csv("result_train.csv")
f_train = pd.read_csv("result_train.csv", index_col = "Date")
f_train.fillna((f_train.mean()), inplace=True)
#f_train.to_csv("r_train.csv")   #(permet de voir le dataframe f_train complété au max)

#Notre dataframe test s'appelle f_test
final_test = final[192:]
final_test.to_csv("result_test.csv")
f_test = pd.read_csv("result_test.csv", index_col = "Date")
f_test.fillna((f_test.mean()), inplace=True)
#f_test.to_csv("r_test.csv")    #(permet de voir le dataframe f_test complété au max)

tab = [f_train, f_test]
tab = pd.concat(tab)
print(tab)