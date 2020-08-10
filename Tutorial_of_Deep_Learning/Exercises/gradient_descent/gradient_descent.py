# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 13:56:29 2018

@author: Lycoris radiata
"""
import numpy as np
from numerical_gradient import numerical_gradient



def gradient_descent(f, init_x, lr, step_num):
    x = init_x
    x_history = []
    
    for i in range(step_num):
        x_history.append( x.copy() )
        
        grad = numerical_gradient(f,x)
        x = x - lr * grad
    return x,np.array(x_history)