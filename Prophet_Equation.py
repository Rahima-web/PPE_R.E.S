# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:37:15 2020

@author: sagan
"""

import pandas as pd
from data_preparation import tab
from fbprophet import Prophet
from datetime import timedelta

#Copy of the dataframe train
df1 = tab.copy()

# GDP

prediction = []

#Dataframe ou on aura tout stocké: les anciennes valeurs et les predictions
prediction = pd.DataFrame(prediction)

def model(df1):
    #Model used : Prophet
    df1 = df1.reset_index()
    name = df1.keys()
    df1.columns = ["ds","y"]
    model=Prophet()
    model.fit(df1)
    
    # Prediction for 9 years from 2011
    future = model.make_future_dataframe(periods=12 * 9, freq='M')
    forecast = model.predict(future)
    prediction["Date"] = forecast["ds"]
    prediction[name[1]] = forecast["yhat"]
    fig = model.plot(forecast)


# Application pour chaque colonne
df_GDP = df1["GDP"]
model(df_GDP)


df_Export = df1["Export"]
model(df_Export)

df_Import = df1["Import"]
model(df_Import)

df_Inflation = df1["Inflation"]
model(df_Inflation)

df_VarInflation = df1["Variations Inflation (%)"]
model(df_VarInflation)

df_VarIntBankLoans = df1["Variations Interest rates on bank loans(%)"]
model(df_VarIntBankLoans)

df_IntBankLoans = df1["Interest rate on bank loans"]
model(df_IntBankLoans)

df_GovSpending = df1["Government Spending (% of GDP)"]
model(df_GovSpending)

df_HouseholdTaxes = df1["HouseHold Taxes"]
model(df_HouseholdTaxes)

df_DtI = df1["Debt to Income Ratio (%)"]
model(df_DtI)

df_NewMortgages = df1["New mortgages "]
model(df_NewMortgages)

df_PaidMortgages = df1["Part of mortgage already paid"]
model(df_PaidMortgages)

df_Mortgages = df1["Mortgages (Million of Livre)"]
model(df_Mortgages)

df_CorpTaxRate = df1["Corporation tax Rate"]
model(df_CorpTaxRate)

df_HouseTaxRate = df1["Household Tax Rate"]
model(df_HouseTaxRate)

df_DepHouse = df1["Deposits for households"]
model(df_DepHouse)

df_IntGovBonds = df1["Interest rates on government bonds"]
model(df_IntGovBonds)

df_HousingWealth = df1["Housing wealth"]
model(df_HousingWealth)

df_LTV = df1["Residential mortgage LTV ratio (%)"]
model(df_LTV)

df_HouseStock = df1["Housing stock"]
model(df_HouseStock)

df_AnnualInvest = df1["Annual business investment (million livre)"]
model(df_AnnualInvest)

df_growth = df1["% growth"]
model(df_growth)

df_pension = df1["Private pension wealth (billion Livres)"]
model(df_pension)

df_TotWealth = df1["Total wealth (billion Livres)"]
model(df_TotWealth)

df_debt = df1["UK National debt en % de GDP"]
model(df_debt)

df_debty = df1["UK National debt en Livres"]
model(df_debty)

df_NomDemICPF = df1["Nominal demand for GB (ICPF)"]
model(df_NomDemICPF)

df_NomDemROW = df1["Nominal demand for GB (Rest of the World ou Overseas)"]
model(df_NomDemROW)

df_NomDemCB = df1["Nominal demand for GB (CB)"]
model(df_NomDemCB)

df_IntDep = df1["Interest rates on deposits (%)"]
model(df_IntDep)

df_GovBondCG = df1["UK government bonds issued by Central Government (in sterling millions)"]
model(df_GovBondCG)

df_intmort = df1["Interest rates Mortgages 3 years (%)"]
model(df_intmort)

df_bbsupply = df1["Bank bond supply "]
model(df_bbsupply)

df_GovtoHouse = df1["Government transfer to households"]
model(df_GovtoHouse)

df_netincome = df1["% of net disposable income"]
model(df_netincome)

df_Annuities = df1["Annuities "]
model(df_Annuities)

df_BDiv = df1["Bank Dividend (in sterling millions)"]
model(df_BDiv)

#Nos index deviennent les dates
prediction = prediction.set_index("Date")
print(prediction)
e = prediction[:288]
p = prediction[288:]
#Les nouvelles données sont des fin de mois donc décalage de 1 jour pour avoir le 1er jour de tous les mois
p.index += timedelta(days=1)

#On recolle les anciennes et les nouvelles valeurs décalées de 1 jour
predict = [e, p]
predict = pd.concat(predict)
# predict est la dataframe finale contenant toutes les valeurs anciennes et nouvelles avec les dates ajustées.
#print(predict)