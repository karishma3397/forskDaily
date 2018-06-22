# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:25:41 2018

@author: KC
"""

import pandas as pd
df = pd.read_csv("Automobile.csv")
df['price'] = df['price'].fillna(df['price'].mean())
price1 = df['price'].values
min(price1)
max(price1)
price1.mean()
price1.std()