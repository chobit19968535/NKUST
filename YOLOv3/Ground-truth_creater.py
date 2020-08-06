# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 13:29:36 2019

@author: user
"""
imgpath = 'D:\\Lycoris\\YoloV3\\BCCD\\BCCD_Dataset\\BCCD\\JPEGImages\\' # Absolute path
txtpath = 'val_imgs.txt'
#path = 'D://WorkSoftware//Python//YOLO//YOLOv3-qqwweee//Data//VOCdevkit//VOC2007//JPEGImages//'

classes = {'RBC' : 0, 'WBC' : 1, 'Platelets' : 2}

with open(txtpath, 'r') as f:
    imgs = f.readlines()
    for file in imgs:
        bboxes = file.split()
        flag = 1
        for row in bboxes:
            if (flag == 1):
                img = row.replace(imgpath,'').split('.')[0]
                flag = 0
                continue
            else:
                left, top, right, bottom, class_ = row.split(',')
                class_ = list(classes.keys())[int(class_)]
                info = class_ + ' ' + left + ' ' + top + ' ' + right + ' ' + bottom +'\n'
                with open( ('groundtruths/'+ eval('img') + '.txt') , 'a') as v:
                    v.write(info)