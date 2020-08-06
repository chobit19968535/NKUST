# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 14:22:39 2020

@author: user
"""
from shutil import copyfile

imgpath = r'BCCD_Dataset/BCCD/JPEGImages/'
with open ('val_imgs.txt') as f:
    datas = f.readlines()

for i in datas:
    img = i.split(' ')[0]
    copyfile(img, 'validimgs/' + img.split('\\')[-1] )