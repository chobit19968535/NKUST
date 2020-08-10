# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:58:58 2020

@author: Lycoris radiata
"""


from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
# Load Mnist Data
(train_image, train_label), (test_image, test_label) = mnist.load_data()

img = train_image[0]


#===============================================#
#                   Display                     #
#===============================================#

# Display Image and its label
plt.imshow(img)
label = train_label[0]
print('Label of image is : ', label)

#===============================================#
#                One hot Encoding               #
#===============================================#

from keras.utils import np_utils
train_label = np_utils.to_categorical(train_label)
print(train_label[0])
test_label = np_utils.to_categorical(test_label)

train_image = train_image.reshape(60000, 784)
test_image = test_image.reshape(10000, 784)

train_image = train_image.astype('float32')
test_image = test_image.astype('float32')

train_image /= 255
test_image /= 255



#===============================================#
#                   Model                       #
#===============================================#

import keras.layers as KL


ANN_Input = KL.Input((784,))
h = KL.Dense(units=512, activation='sigmoid', name='HiddenLayer1')(ANN_Input)
h = KL.Dense(units=512, activation='sigmoid', name='HiddenLayer2')(h)
ANN_Output = KL.Dense(10, activation='softmax')(h)

# Creat Model
from keras import Model
ANN_Mnist = Model(ANN_Input, ANN_Output)
ANN_Mnist.summary()

ANN_Mnist.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
trainlogs = ANN_Mnist.fit(x=train_image, y=train_label, batch_size=128, epochs=10,
              validation_data=(test_image, test_label), class_weight=None)

#===============================================#
#                   evaluate                    #
#===============================================#
results = ANN_Mnist.evaluate(test_image, test_label, batch_size=128)

print('Test loss is : ', round(results[0],4))
print('Test Accuracy is : {}%'.format(round(results[1]*100,2)))

#===============================================#
#                   Predict                     #
#===============================================#
Probs = ANN_Mnist.predict(test_image, batch_size=128)
Labels  = np.argmax(Probs, -1)

print('Probs of Image_0: ', np.round(Probs[0],2)*100)
print('Label of Image_0: {}'.format(Labels[0]))
