# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 16:06:12 2019

@author: Lycoris radiata
"""

from FSPSO import fspso
from Makespan_list import makespan_list
from DataSplit import datasplit




"""
Initialize
"""
job_list = datasplit()
# Job
lb = [1e-8]*len(job_list)
ub = [1e8]*len(job_list)

"""
Processing
"""
xopt,result_opt = fspso(NEH_list,job_list, makespan_list, lb, ub,ieqcons=[], f_ieqcons=None, args=(), kwargs={}, 
        swarmsize=100, omega=0.2, phip=0.8, phig=0.5, maxiter=50, 
        minstep=1e-8, minfunc=1e-8, debug=True)

"""
Result
"""
FlowShop_list = sorted(range(len(xopt)), key = lambda k:xopt[k])