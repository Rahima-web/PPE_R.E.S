# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:12:53 2020

@author: sagan
"""

from data_preparation import final_dataframe
from fbprophet import Prophet


# GDP
df = final_dataframe.copy()

df = df["GDP"][960:-12]
df = df.reset_index()
df.columns = ["ds", "y"]

#train = df[:495]


train = df[:200]

model=Prophet()
model.fit(train)

future = model.make_future_dataframe(periods=12 * 10, freq='M')
forecast = model.predict(future)
fig = model.plot(forecast)

print(fig)

