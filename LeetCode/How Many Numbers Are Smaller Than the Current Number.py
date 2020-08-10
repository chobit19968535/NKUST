# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:06:46 2020

@author: Lycoris radiata
"""

nums = [8,1,2,2,3]
count = [0]*len(nums)
for index, value in enumerate(nums):
    for v in nums:
        if v <value:
            count[index]+=1
            