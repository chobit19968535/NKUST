# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 11:19:54 2019

@author: Lycoris radiata
"""
from NEH import NEH
from DataSplit import datasplit




"""
Initialize
"""
# Get Joblist ##################################
job_list = datasplit()

# Get sorted_f_index ##################################
singlejob_f = list(map(sum,job_list))
sorted_f_index = sorted(range(len(singlejob_f)),key = lambda i : singlejob_f[i],reverse=True)


"""
NEH algorithm
"""
# NEH algorithm ##################################
NEH_list, fitness = NEH(job_list,sorted_f_index)