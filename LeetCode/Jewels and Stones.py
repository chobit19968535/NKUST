# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:58:17 2020

@author: Lycoris radiata
"""

J = "aA"
S = "aAAbbbb"
count = 0
for s in S:
    if s in J:
        count+=1
        
print(count)