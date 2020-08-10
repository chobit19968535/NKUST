# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:45:05 2020

@author: Lycoris radiata
"""

nums = [3,5,7,9,15,12]

target = 24
seen = {}

for index, num in enumerate(nums):
    other = target - num
    
    if other in seen:
        print( [seen[other], index])
    else:
        seen[num] = index