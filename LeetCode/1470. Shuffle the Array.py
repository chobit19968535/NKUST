# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 08:57:39 2020

@author: Lycoris radiata
"""

nums = [2,5,1,3,4,7]
n = 3
A = [0]*len(nums)

pair = int(len(nums)/2)

for i in range(0, pair, 1):
    front = i*2
    end = i*2+1
    A[front] = nums[i]
    A[end] = nums[i+n]