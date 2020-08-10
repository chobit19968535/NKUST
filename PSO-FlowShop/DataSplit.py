# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 12:06:44 2019

@author: Lycoris radiata
"""


def datasplit():
    """
    Split Datas of Taillard 
   
    Parameters
    ==========
    A : list
        Input of a J/M data in Taillard
    job_num : scalar
        Numbers of Job in Data
    m_num : scalar
        Numbers of Machine in Data
   
    Optional
    ========
    None
   
    Returns
    =======
    job_list : list
        job_list
   
    """
    print("Please Input Raw-DATA \n")
    A = [int(x) for x in input().split()]
    print("Please Input Job.num \n")
    job_num = int(input())
    print("Please Input Machine.num \n")
    m_num = int(input())
    job_list = [[]]
    for i in range (job_num):
        tmp=[]
        for j in range(0,job_num*m_num,job_num):
            if (i==0):
                job_list[0].append(A[j+i])
                continue
            tmp.append(A[j+i])
            if ( j>= (m_num-1)*job_num ):
                job_list.append(tmp)
    return(job_list)
    
    
