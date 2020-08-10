# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:59:44 2020

@author: Lycoris radiata
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib

np.random.seed(426)

#################################################################
#                                                               #
#                                                               #
#                           Prepare Data                        #
#                                                               #
#                                                               #
#################################################################
num_imgs = 5000
img_size = 8
min_rect_size = 1
max_rect_size = 4
num_objects = 1
nb_epoch = 5
# ------------
# -
# -
# -
# ------------
#(x, y)

bboxes = np.zeros((num_imgs, num_objects, 4))
imgs = np.zeros((num_imgs, img_size, img_size))
shapes = np.zeros((num_imgs, num_objects, 1))

for i_img in range(num_imgs):
    for i_object in range(num_objects):
        width, height = np.random.randint(min_rect_size, max_rect_size, size=2)
        x = np.random.randint(0, img_size - width)
        y = np.random.randint(0, img_size - height)
        imgs[i_img, x:x+width, y:y+height] = 1.
        bboxes[i_img, i_object] = [x, y, width, height]
            
imgs.shape, bboxes.shape

i = 0
# TODO: Why does the array have to be transposed?
plt.imshow(imgs[i].T, cmap='Greys', interpolation='none', origin='lower', extent=[0, img_size, 0, img_size])
for bbox, shape in zip(bboxes[i], shapes[i]):
    plt.gca().add_patch(matplotlib.patches.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], ec='r' if shape[0] == 0 else 'y', fc='none'))

X = ((imgs- np.mean(imgs)) / np.std(imgs))
X = np.reshape(X, (num_imgs, img_size, img_size, 1))
X.shape, np.mean(X), np.std(X)
y = np.concatenate([bboxes / img_size, shapes], axis=-1).reshape(num_imgs, -1) # (x, y, w, h, class)
y.shape

i = int(0.8 * num_imgs)
train_image = X[:i]
train_label = y[:i]

test_image = X[i:]
test_label = y[i:]

test_imgs = imgs[i:]
test_bboxes = bboxes[i:]


#################################################################
#                                                               #
#                                                               #
#                           Creat Model                         #
#                                                               #
#                                                               #
#################################################################

import keras.layers as KL


ANN_Input = KL.Input((8,8,3))
h = KL.Conv2D(filters=8, kernel_size=(3,3), activation='relu', padding = 'valid', name='conv1')(ANN_Input)
h = KL.Conv2D(filters=16, kernel_size=(3,3), activation='relu', padding = 'valid', name='conv2')(h)
h = KL.Flatten()(h)
ANN_Output = KL.Dense(5, activation='linear')(h)

# Creat Model
from keras import Model
ANN_detector = Model(ANN_Input, ANN_Output)
ANN_detector.summary()

#################################################################
#                                                               #
#                                                               #
#                           Train Model                         #
#                                                               #
#                                                               #
#################################################################
ANN_detector.compile(optimizer='adam', loss='mse')
ANN_detector.fit(train_image, train_label, nb_epoch=nb_epoch, validation_data=(test_image, test_label), verbose=2)

#################################################################
#                                                               #
#                                                               #
#                        Plot Detection                         #
#                                                               #
#                                                               #
#################################################################

pred_y = ANN_detector.predict(test_image)
pred_y = pred_y.reshape(len(pred_y), num_objects, -1)
pred_bboxes = pred_y[..., :4] * img_size
pred_shapes = pred_y[..., 4:5]
pred_bboxes.shape, pred_shapes.shape

plt.figure(figsize=(16, 8))
for i_subplot in range(1, 9):
    plt.subplot(2, 4, i_subplot)
    i = np.random.randint(len(test_image))
    plt.imshow(test_imgs[i].T, cmap='Greys', interpolation='none', origin='lower', extent=[0, img_size, 0, img_size])
    for pred_bbox, exp_bbox, pred_shape in zip(pred_bboxes[i], test_bboxes[i], pred_shapes[i]):
        plt.gca().add_patch(matplotlib.patches.Rectangle((pred_bbox[0], pred_bbox[1]), pred_bbox[2], pred_bbox[3], ec='r' if pred_shape[0] <= 0.5 else 'y', fc='none'))
        # TODO: Calculate max IOU with all expected bounding boxes.
#         plt.annotate('IOU: {:.2f}'.format(IOU(pred_bbox, exp_bbox)), (pred_bbox[0], pred_bbox[1]+pred_bbox[3]+0.4), color='r')