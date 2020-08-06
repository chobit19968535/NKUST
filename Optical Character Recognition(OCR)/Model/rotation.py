# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 10:53:31 2020

@author: Lycoris radiata
"""
import os
import cv2

def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]
 
    if center is None:
        center = (w / 2, h / 2)
 
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h), borderValue= (255,255,255))
 
    return rotated
path = "test/"
imgs = os.listdir(path)
for i in imgs:
    img = cv2.imread( path + i, 0 )
#    img = cv2.adaptiveThreshold(img,125,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#            cv2.THRESH_BINARY,5,5)
    rotation = rotate(img, -35)
    cv2.imwrite(path+ i, rotation)
