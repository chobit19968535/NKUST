# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:35:18 2020

@author: Public_2080
"""

from keras.models import load_model
import efficientnet.keras as efn 
model = load_model('logs/oc_cnn/best_acc.h5')

import numpy as np
import os
import PIL.Image as Image

input_shape = (224, 224)
n_classes = 2

def test_resize(img_route, input_shape, proc_img = True):
    image = Image.open(img_route) #RGB but show onli size
    iw, ih = image.size
    h, w = input_shape
    
    # resize image 做縮放，可以以其他方法改變
    scale = min(w/iw, h/ih) #選取最小邊
    nw = int(iw*scale)
    nh = int(ih*scale)
    dx = (w-nw)//2
    dy = (h-nh)//2
    image_data=0 #開一個暫存
    if proc_img:
        image = image.resize((nw,nh), Image.BICUBIC) #双立方滤波。在输入图像的4*4矩阵上进行立方插值
        new_image = Image.new('RGB', (w,h), (128,128,128))#開啟一個新圖像，放置128數值
        new_image.paste(image, (dx, dy))
        image_data = np.array(new_image)/255.
        #image_data = image_data[np.newaxis,:,:,:]
        image_data = np.expand_dims(image_data,axis=0)
    return (image_data)#反回資料並以灰階表示

path = 'train/train/33/'
cluster_path = 'train/oc_cnn_imgs/33/'
files = os.listdir(path)

import pandas as pd
import shutil
LABEL = []
NAME = []
count = 0
GROUND = []
for i in range(33,34):
    if i <10:
        path = 'train/train/0' + str(i) + '/'
        files = os.listdir(path)
    else:
        path = 'train/train/' + str(i) + '/'
        files = os.listdir(path)
    for f in files:
        NAME.append(f)
        img_route=(path + f)
        img = test_resize(img_route, input_shape)
        label = np.argmax(model.predict(img),-1)
        tmp_path = cluster_path + str(label[0]) + '/' + f
        shutil.copyfile(img_route, tmp_path)
        LABEL.append(label[0])
        GROUND.append(i)
        if (count % 1000) == 0:
            print(count)
        count +=1
        
        

data = pd.DataFrame({'NAME':NAME,'LABEL':LABEL, 'Ground':GROUND})
data.to_csv('oc_cnn_33.csv',index=False)