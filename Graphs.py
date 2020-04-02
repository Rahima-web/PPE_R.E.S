# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:39:04 2020

@author: sagan
"""
from data_preparation import final_dataframe

#Visualisation des données
tmp = final_dataframe.reset_index()
tmp = tmp[tmp["Date"] >= "2000"] # Données après 1960
tmp["Date"] = tmp["Date"].astype(str)

for col in final_dataframe.columns:
    tmp.plot(x='Date', y=col, marker='.', figsize=(15,7))

