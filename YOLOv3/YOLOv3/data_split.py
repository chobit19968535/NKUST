# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:17:28 2019

@author: Lycoris radiata
"""
import random
import numpy as np
#%%

#%%

#%%

val_split = 0.20
with open ('lines.txt', 'r') as f:
    lines = f.readlines()
random.shuffle(lines)
np.random.seed(426)
np.random.shuffle(lines)
num_val = int(len(lines)*val_split)
num_train = len(lines) - num_val

with open('annotation_train.txt', 'w') as f:
    [f.write(l) for l in lines[ :num_train]]  

with open('annotation_val.txt', 'w') as f:
    [f.write(l) for l in lines[num_train : ]]