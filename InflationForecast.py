#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 15 13:56:06 2025

@author: ayaankamal
"""

import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
from statsmodels.tsa.seasonal import seasonal_decompose
import pmdarima as pm

#read in CPI data for inflation
cpi = pd.read_csv("~/Downloads/CPIAUCSL.csv")
yoy = []
dates = list(cpi.iloc[90:-1,0])
for i in range(90, len(cpi)-1):
    yearInf = ((cpi.iloc[i, 1]-cpi.iloc[i-12, 1])/cpi.iloc[i-12, 1]) * 100
    yoy.append(yearInf)
strformat = "%Y-%m-%d"
for i in range(len(dates)):
    dates[i] = datetime.strptime(dates[i], strformat)
df = pd.DataFrame(zip(dates, yoy), columns = ["Date", "YoY Inflation"])

#add exogenous vars
fedfundsrate = pd.read_csv("~/Downloads/FEDFUNDS.csv")
df["Fed Funds"] = fedfundsrate.iloc[:-1,1]
unempl = pd.read_csv("~/Downloads/UNRATE-3.csv")
df["Unemployment Rate"] = unempl.iloc[:-1,1]
df = df.set_index("Date")

result = seasonal_decompose(df["YoY Inflation"], model = "additive", period = 12)
trend = result.trend.dropna()
seasonal = result.seasonal.dropna()
residual = result.resid.dropna()

plt.figure(figsize=(6,6))

plt.subplot(4, 1, 1)
plt.plot(df['YoY Inflation'], label='Original Series')
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(trend, label='Trend')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(seasonal, label='Seasonal')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(residual, label='Residuals')
plt.legend()

plt.tight_layout()
plt.show()

df["Month"] = df.index.month

model = pm.auto_arima(df[["YoY Inflation"]], exogenous = df[["Fed Funds", "Unemployment Rate", "Month"]],
                           start_p=1, start_q=1,
                           test='adf',
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=None, D=1,
                           trace=False,
                           error_action='ignore',
                           suppress_warnings=True,
                           stepwise=True)
