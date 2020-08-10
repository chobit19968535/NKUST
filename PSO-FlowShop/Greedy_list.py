# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 11:18:17 2019

@author: Lycoris radiata
"""

def greedy_list(NEH_list, sorted_f_index):
    """
    greedy_list()
   
    Parameters
    ==========
    NEH_list : list
        NEH_list
    sorted_f_index : list
        sorted index of fitnesses, sense is similar queue.
        Each value is one of Index in Job_list,also include relative magnitude(Max to min)
   
    Optional
    ========
    None
   
    Returns
    =======
    greedy_list : list
        possible combinations of next NEH_list
   
    """
    greedy_list = []
    for i in range (len(NEH_list)+1):
        tmp =[]
        tmp = tmp + NEH_list
        tmp.insert(i,sorted_f_index[0])
        greedy_list.append(tmp)
    return(greedy_list)