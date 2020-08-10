# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:14:20 2020

@author: Public_2080
"""

import os

txt_path = 'train/data/'

classnum = 33
img_path = 'train/oc_cnn/' + str(classnum) + '/'


with open ( txt_path +  str(classnum) + '.txt', 'w') as f:
    pass
for i in range(2):
    label = str(i)
    path = img_path + str(i) + '/'
    files = os.listdir(path)
    for file in files:      
        with open (txt_path + str(classnum) + '.txt', 'a') as f:
            f.write( path+file + ' ' + label + '\n')