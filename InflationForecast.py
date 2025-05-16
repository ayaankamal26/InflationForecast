#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 15 13:56:06 2025

@author: ayaankamal
"""

import numpy as np
import pandas as pd
from datetime import datetime

#read in CPI data for inflation
cpi = pd.read_csv("~/Downloads/CPIAUCSL.csv")
yoy = []
dates = list(cpi.iloc[90:-1,0])
for i in range(90, len(cpi)-1):
    yearInf = ((cpi.iloc[i, 1]-cpi.iloc[i-12, 1])/cpi.iloc[i-12, 1]) * 100
    yoy.append(yearInf)
strformat = "%Y-%M-%d"
for i in range(len(dates)):
    dates[i] = datetime.strptime(dates[i], strformat)
    dates[i] = dates[i].replace(hour=12, minute = 0)
df = pd.DataFrame(zip(dates, yoy), columns = ["Date", "YoY Inflation"])

#add exogenous vars
fedfundsrate = pd.read_csv("~/Downloads/FEDFUNDS.csv")
df["Fed Funds"] = fedfundsrate.iloc[:-1,1]
unempl = pd.read_csv("~/Downloads/UNRATE-3.csv")
df["Unemployment Rate"] = unempl.iloc[:-1,1]
df = df.set_index("Date")
