# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:02:47 2020

@author: Lycoris radiata
"""


import os
import pandas as pd


split = True

info = os.listdir('pokemon/')
IMAGE = []
LABEL = []

for index, val in enumerate(info):
    image_path = 'pokemon/' + val + '/'
    images = os.listdir(image_path)
    label = []
    
    for n, img in enumerate(images):
        IMAGE.append(image_path + img)
        LABEL.append(index)

df = {'image' : IMAGE, 'label' : LABEL}
df = pd.DataFrame(data=df)

df.to_csv('data.csv', index=False)



csv = pd.read_csv('data.csv')

if not split:
    with open ('data.txt', 'w') as f:
        for i in range(len(csv)):
            img = csv.iloc[i][0]
            label = csv.iloc[i][1]
            f.write(str(img) + ' ' + str(label) +'\n')
else:
    csv = csv.sample(frac=1).reset_index(drop=True)
    bp = int(0.8*len(df))
    with open ('train_data.txt', 'w') as f:
        for i in range(bp):
            img = csv.iloc[i][0]
            label = csv.iloc[i][1]
            f.write(str(img) + ' ' + str(label) +'\n')
            
    with open ('test_data.txt', 'w') as f:
        for i in range(bp, len(df)):
            img = csv.iloc[i][0]
            label = csv.iloc[i][1]
            f.write(str(img) + ' ' + str(label) +'\n')