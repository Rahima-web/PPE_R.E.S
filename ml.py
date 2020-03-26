# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:12:53 2020

@author: sagan
"""

from data_preparation import final_dataframe
from fbprophet import Prophet


# GDP
df = final_dataframe.copy()
df = df["GDP"][960:-12] # Récupère uniquement les dates avec une valeur.
df = df.reset_index()
df.columns = ["ds", "y"]

# Train set (70%) et Test set (30%)
train = df[:495]
test = df[495:]

# Modèle Prophet
model=Prophet()
model.fit(train)

# Prediction sur 10 ans
future = model.make_future_dataframe(periods=12 * 10, freq='M')
forecast = model.predict(future)
fig = model.plot(forecast)

print(fig)

