# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:12:53 2020

@author: sagan
"""


from data_preparation import f_train,f_test
from fbprophet import Prophet

#Copy of the dataframe train
df1 = f_train.copy()

# GDP
df1 = df1["GDP"]
df1 = df1.reset_index()
df1.columns = ["ds","y"]

#Model used : Prophet
model=Prophet()
model.fit(df1)

# Prediction for 9 years from 2011
future = model.make_future_dataframe(periods=12 * 9, freq='M')
forecast = model.predict(future)
fig = model.plot(forecast)

#Test values
df2 = f_test.copy()
test = df2["GDP"]

