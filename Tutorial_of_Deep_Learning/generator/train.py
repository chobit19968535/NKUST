# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:36:45 2020

@author: Lycoris

"""


"""
Utils
"""
from PIL import Image

"""
Core
"""

from keras.preprocessing.image import ImageDataGenerator
import numpy as np

from keras.applications import MobileNetV2

from keras.layers import Dense , Dropout, GlobalAveragePooling2D
from keras.models import Model
from keras.optimizers import adam, SGD
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb

"""
Callbacks
"""
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
from tensorflow.keras.callbacks import TensorBoard
log_dir = 'logs/'
logging = TensorBoard(log_dir=log_dir)
#ModelCheckpoint(log_dir + 'ep{epoch:03d}-loss{loss:.3f}-train_loss{train_loss:.3f}.h5',
#    monitor='train_loss', save_weights_only=True, save_best_only=True, period=3)
checkpoint_acc = ModelCheckpoint(log_dir + 'best_acc_Ep{epoch:03d}.h5',
    monitor='val_accuracy', save_weights_only=False, save_best_only=True, period=1)

checkpoint_loss = ModelCheckpoint(log_dir + 'min_loss.h5',
    monitor='val_loss', save_weights_only=False, save_best_only=True, period=1)

reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=3, verbose=1)
early_stopping = EarlyStopping(monitor='val_loss', min_delta=0, patience=7, verbose=1)


print('Starting')
stage_1_epoch = 15
dropout_rate = 0.2
input_shape = (224, 224)
n_classes = 5
batch_size = 4
train_annotation_path = 'train_data.txt'
test_annotation_path = 'test_data.txt'

"""
Modify Model to Custom data
"""
base_model = MobileNetV2(weights='imagenet',  include_top=True)
# model = Xception(weights='imagenet',  include_top=True)
x = base_model.output
x = GlobalAveragePooling2D()(x)
predictions = Dense(n_classes, activation='softmax', name='probs')(x)
model = Model(inputs=base_model.input, outputs=predictions)
base_model.summary()

"""
Data Prepocessing
"""

with open (train_annotation_path, 'r') as f:
    train_lines = f.readlines()
    
with open (test_annotation_path, 'r') as f:
    test_lines = f.readlines()
#lines = lines[:25]
import random
random.shuffle(train_lines)
num_train = len(train_lines)
num_val = len(test_lines)


def data_generator(annotation_lines, batch_size, input_shape, random):
    '''data generator for fit_generator'''
    n = len(annotation_lines)
    i = 0
    while True:
        image_data = []
        label_data = []
        for b in range(batch_size):
            if i==0:
                np.random.shuffle(annotation_lines)
            image, label = get_random_data(annotation_lines[i], input_shape, random)
            image_data.append(image)
            label_data.append(label)
            i = (i+1) % n
        image_data = np.array(image_data)
        from keras.utils import to_categorical
        label_data = to_categorical(label_data, num_classes=n_classes)
#        yield image_data, label_data, np.zeros(batch_size)
        yield image_data, label_data
#        yield ( [image_data, *label_data], np.zeros(batch_size) )

def data_generator_wrapper(annotation_lines, batch_size, input_shape, random):
    n = len(annotation_lines)
    if n==0 or batch_size<=0: return None
    return data_generator(annotation_lines, batch_size, input_shape, random)

def rand(a=0, b=1):
    return np.random.rand()*(b-a) + a 

def get_random_data(annotation_lines, input_shape, proc_img = True, random =True,
                    flip = False, hue = .1, jitter = .1, sat = .25, val = .25):
    line = annotation_lines.split()
    image = Image.open(line[0])
    label = line[1]
    iw, ih = image.size
    h, w = input_shape
    
    if not random:
        # resize image
        scale = min(w/iw, h/ih)
        nw = int(iw*scale)
        nh = int(ih*scale)
        dx = (w-nw)//2
        dy = (h-nh)//2
        image_data=0
        if proc_img:
            image = image.resize((nw,nh), Image.BICUBIC)
            new_image = Image.new('RGB', (w,h), (128,128,128))
            new_image.paste(image, (dx, dy))
            image_data = np.array(new_image)/255.
            
        return (image_data, label)
    else:
        """
        Data-Augmentation
        """
    # =============================================================================
    #                               Scale(parameter is 'jitter')
    # =============================================================================
        # resize image
        new_ar = w/h * rand(1-jitter,1+jitter)/rand(1-jitter,1+jitter)
        scale = rand(.25, 2)
        if new_ar < 1:
            nh = int(scale*h)
            nw = int(nh*new_ar)
        else:
            nw = int(scale*w)
            nh = int(nw/new_ar)
        image = image.resize((nw,nh), Image.BICUBIC)
    
    # =============================================================================
    #                               Shift
    # =============================================================================
        # place image
        dx = int(rand(0, w-nw))
        dy = int(rand(0, h-nh))
        new_image = Image.new('RGB', (w,h), (128,128,128))
        new_image.paste(image, (dx, dy))
        image = new_image
    # =============================================================================
    #                               Flip
    # =============================================================================
        # flip image or not
    #    flip = True
        if flip: image = image.transpose(Image.FLIP_LEFT_RIGHT)
    # =============================================================================
    #                               Color Augmentation
    #                       RGB --> HSV(parameter is hue) --> RGB
    # =============================================================================
        # distort image
        hue = rand(-hue, hue)
        sat = rand(1, sat) if rand()<.5 else 1/rand(1, sat)
        val = rand(1, val) if rand()<.5 else 1/rand(1, val)
        x = rgb_to_hsv(np.array(image)/255.)
        x[..., 0] += hue
        x[..., 0][x[..., 0]>1] -= 1
        x[..., 0][x[..., 0]<0] += 1
        x[..., 1] *= sat
        x[..., 2] *= val
        x[x>1] = 1
        x[x<0] = 0
        image_data = hsv_to_rgb(x) # numpy array, 0 to 1
    
        return (image_data, label)

#aug = ImageDataGenerator(rotation_range=20, zoom_range=0.15,
#	width_shift_range=0.2, height_shift_range=0.2, shear_range=0.15,
#	horizontal_flip=True, fill_mode="nearest")

for layer in model.layers[:]:
   layer.trainable = True
"""
Two-Stage training trick
"""
# Stage 1 
model.compile(optimizer=adam(lr=1e-3), loss='categorical_crossentropy', metrics = ['accuracy'])
print('Train on {} samples, val on {} samples, with batch size {}.'.format(num_train, num_val, batch_size))
history_freeze = model.fit_generator(data_generator_wrapper(train_lines, batch_size, input_shape, random=True),
        steps_per_epoch=max(1, num_train//batch_size),
        validation_data=data_generator_wrapper(test_lines, batch_size, input_shape, random=False),
        validation_steps=max(1, num_val//batch_size),
        epochs=stage_1_epoch,
        initial_epoch=0,
        callbacks=[checkpoint_acc, reduce_lr, early_stopping])
model.save(log_dir + 'trained_model_stage_1.h5')


