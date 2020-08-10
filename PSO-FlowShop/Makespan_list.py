# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 15:50:36 2019

@author: Lycoris radiata
"""
from Makespan import makespan

def makespan_list(job_list,posible_list):
    """
    makespan_list()
   
    Parameters
    ==========
    job_list : list
        job_list
    posible_list : list
        posible_list of next NEH_list
   
    Optional
    ========
    None
   
    Returns
    =======
    span_list[1][-1] : scalar
        Makespan from possible_list
   
    """
    tjob_list=[]
    for i in range (len(posible_list)):
        tjob_list.append(job_list[posible_list[i]])
    span_list = makespan(tjob_list)
    del tjob_list[0:2]
    
    for i in range(len(tjob_list)):  # Update Span
        for j in range(len(tjob_list[0])):
            if (j==0):  #Round 0 initialize
                tmp = tjob_list[0][0] + span_list[1][0]
                span_list[1][0] = tmp
                continue
            if span_list[1][j-1] < span_list[1][j]:
                tmp = span_list[1][j] + tjob_list[0][j]
                span_list[1][j] = tmp
                continue
            if span_list[1][j-1] >= span_list[1][j]:
                tmp = tjob_list[0][j] + span_list[1][j-1]
                span_list[1][j] = tmp
                continue
        del tjob_list[0]
    return(span_list[1][-1])