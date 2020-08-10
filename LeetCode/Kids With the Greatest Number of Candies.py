# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 11:52:36 2020

@author: Lycoris radiata
"""


A = [2,3,5,1,3]
flag = max(A)
extraCandies  = 3
B = [extraCandies]*len(A)

for index, value in enumerate(A):
    if (B[index] + value ) >= flag:
        B[index] = True
    else:
        B[index] = False
        
print(B)
