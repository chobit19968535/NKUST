# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 13:14:00 2020

@author: Public_2080
"""

import numpy as np
import efficientnet.keras as efn
from keras.models import load_model
import os
import PIL.Image as Image
import pandas as pd

input_shape = (224, 224)
n_classes = 42

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
path = 'test/test/'
model = load_model('clean_018_val9409.h5')
files = os.listdir(path)


"""
Read Csv
"""
data = pd.read_csv('test.csv')
count = 0
CATEGORY=[]
for f in data["filename"]:
#    NAME.append(f)
    img_route=(path + f)
    img = test_resize(img_route, input_shape)
    label = np.argmax(model.predict(img),-1)
    label = label[0]
    if label < 10:
        label = '0' + str(label)
    else:
        label = str(label)
    CATEGORY.append(label)
    if (count % 1000) == 0:
        print(count)
    count +=1
    
predict_test = pd.DataFrame({'filename':data["filename"],'category':CATEGORY})
#data.to_csv('predicts.csv',index=False)

#import pandas as pd
#predict_test = pd.read_csv('predicts.csv')
predict_test["category"] = predict_test["category"].apply(lambda x: "{:02}".format(x))
predict_test.to_csv("clean_035_val9161A.csv", index=False)