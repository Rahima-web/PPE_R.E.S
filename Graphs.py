# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:39:04 2020

@author: sagan
"""
from data_preparation import final_dataframe

# Visualisation des données
tmp = final_dataframe.reset_index()
tmp = tmp[tmp["MonthYear"] >= "1960"] # Données après 1960
tmp["MonthYear"] = tmp["MonthYear"].astype(str)

for col in final_dataframe.columns:
    tmp.plot(x='MonthYear', y=col, marker='.', figsize=(15,7))
