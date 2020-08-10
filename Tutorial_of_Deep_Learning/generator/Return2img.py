# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:19:54 2020

@author: Public_2080
"""

import numpy as np
import cv2 as cv2

imgs = np.load('image_data.npy')
labels = np.load('label_data.npy')
count = 0
for i in imgs:
    # 顯示圖片
    cv2.imshow('My Image', i)
    print(labels[count])
    print('\n')
    count +=1
    # 按下任意鍵則關閉所有視窗
    cv2.waitKey(0)
    cv2.destroyAllWindows()