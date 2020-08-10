# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 13:55:49 2020

@author: Public_2080
"""

import pandas as pd
csv = pd.read_csv('data.csv')


with open ('data.txt', 'w') as f:
    for i in range(len(csv)):
        img = csv.iloc[i][0]
        label = csv.iloc[i][1]
        f.write(str(img) + ' ' + str(label) +'\n')