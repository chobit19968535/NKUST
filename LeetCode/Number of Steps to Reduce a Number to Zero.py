# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:18:13 2020

@author: Lycoris radiata
"""

num = 14
count = 0
ans = 0

def processing(x, count):
    if x == 0:
        return(count)
    if x%2 !=0:
        x-= 1
        count+= 1
        return(processing(x, count))
    else:
        x/= 2
        count+= 1
        return(processing(x, count))
        
print(processing(num, count))