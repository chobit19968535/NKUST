# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:20:43 2020

@author: Lycoris radiata
"""

nums = [1,2,3,4]
A=[]

def processing(nums, A):
    for index, value in enumerate(nums):
        try:
            freq = nums[2*index]
            val = nums[2*index+1] 
            A+= [val]*freq
        except:
            return(A)

print(processing(nums, A))