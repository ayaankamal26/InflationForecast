#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 15 13:56:06 2025

@author: ayaankamal
"""

import numpy as np
import pandas as pd

#read in CPI data for inflation
cpi = pd.read_csv("~/Downloads/CPIAUCSL.csv")
yoy = []
dates = list(cpi.iloc[12:,0])
for i in range(12, len(cpi)):
    yearInf = ((cpi.iloc[i, 1]-cpi.iloc[i-12, 1])/cpi.iloc[i-12, 1]) * 100
    yoy.append(yearInf)
df = pd.DataFrame(zip(dates, yoy), columns = ["Date", "YoY Inflation"])
