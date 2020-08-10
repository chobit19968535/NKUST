# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 11:19:54 2019

@author: Lycoris radiata
"""

from Makespan import makespan
from Makespan_list import makespan_list
from Greedy_list import greedy_list

def NEH(job_list,sorted_f_index):
    """
    NEH Algorithm
   
    Parameters
    ==========
    job_list : list
        job_list
    sorted_f_index : list
        sorted index of fitnesses, sense is similar queue.
        Each value is one of Index in Job_list,also include relative magnitude(Max to min)
   
    Optional
    ========
    None
   
    Returns
    =======
    NEH_list : list
        Result of NEH_list in NEH algorithm
    spanlist[0]
        Makespan of NEH_list
   
    """
    NEH_list=[]
    posible_list=[]
    for i in range (len(job_list)-1):
        if (i == 0): # 'Part A' : Round0 Initialize
            tmp_job_list = []
            tmp_job_list.append(job_list[sorted_f_index[0]])
            tmp_job_list.append(job_list[sorted_f_index[1]])
            left = makespan(tmp_job_list)[-1][-1]
            
            
            tmp_job_list = []
            tmp_job_list.append(job_list[sorted_f_index[1]])
            tmp_job_list.append(job_list[sorted_f_index[0]])
            right = makespan(tmp_job_list)[-1][-1]
            if left <= right:
                NEH_list.append(sorted_f_index[0])
                NEH_list.append(sorted_f_index[1])
                del sorted_f_index[0:2]
            else:
                assert left > right, 'left not > right'
                NEH_list.append(sorted_f_index[1])
                NEH_list.append(sorted_f_index[0])
                del sorted_f_index[0:2]
        else:   # 'Part B' : Processing
            spanlist=[]
            posible_list = greedy_list(NEH_list,sorted_f_index)
            for i in range (len(posible_list)):
                spanlist.append(makespan_list(job_list,posible_list[i]))
            sorted_spanlist = sorted(range(len(spanlist)),key = lambda i : spanlist[i])
            NEH_list = posible_list[sorted_spanlist[0]]
            del sorted_f_index[0]
    return(NEH_list,spanlist[0])
        
#spancost, posible_list, fitness = NEH(job_list,sorted_f_index)