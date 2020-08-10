# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 18:05:21 2020

@author: Public_2080
"""
from PIL import Image
from keras import layers, Input
from keras.models import Model
from keras.initializers import he_normal
from keras.optimizers import adam, SGD
import numpy as np

# =======================================================================
#                                   Def
# =======================================================================
def data_generator(annotation_lines, batch_size, input_shape):
    '''data generator for fit_generator'''
    n = len(annotation_lines)
    i = 0
    while True:
        image_data = []
        label_data = []
        for b in range(batch_size):
            if i==0:
                np.random.shuffle(annotation_lines)
            image, label = process_line(annotation_lines[i], input_shape)
            image_data.append(image)
            label_data.append(label)
            i = (i+1) % n
        image_data = np.array(image_data)
        from keras.utils import to_categorical
        label_data = to_categorical(label_data, num_classes=2)
#        yield image_data, label_data, np.zeros(batch_size)
        yield image_data, label_data
#        yield ( [image_data, *label_data], np.zeros(batch_size) )

def data_generator_wrapper(annotation_lines, batch_size, input_shape):
    n = len(annotation_lines)
    if n==0 or batch_size<=0: return None
    return data_generator(annotation_lines, batch_size, input_shape)

        
def process_line(annotation_lines, input_shape, proc_img = True):
    line = annotation_lines.split()
    image = Image.open(line[0])
    lable = line[1]
    iw, ih = image.size
    h, w = input_shape
    
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
        
    return (image_data, lable)


#aug = ImageDataGenerator(rotation_range=20, zoom_range=0.15,
#	width_shift_range=0.2, height_shift_range=0.2, shear_range=0.15,
#	horizontal_flip=True, fill_mode="nearest")

input_shape = (224, 224)
model_input_shape = (224, 224, 3)
model_input = Input(shape=model_input_shape, name = 'image')
x = layers.Conv2D( filters = 32, kernel_size = (3, 3), strides=2, padding='same', activation = 'relu', use_bias=False, kernel_initializer = he_normal(seed = 426))(model_input)
x = layers.BatchNormalization()(x)
x = layers.Conv2D( filters = 64, kernel_size = (3, 3), strides=2, padding='same', activation = 'relu', use_bias=False,kernel_initializer = he_normal(seed = 426))(x)
x = layers.BatchNormalization()(x)
x = layers.Conv2D( filters = 128, kernel_size = (3, 3), strides=2, padding='same', activation = 'relu', use_bias=False,kernel_initializer = he_normal(seed = 426))(x)
x = layers.BatchNormalization()(x)
x = layers.Conv2D( filters = 256, kernel_size = (3, 3), strides=2, padding='same', activation = 'relu', use_bias=False,kernel_initializer = he_normal(seed = 426))(x)
x = layers.BatchNormalization()(x)
x = layers.Conv2D( filters = 512, kernel_size = (3, 3), strides=2, padding='same', activation = 'relu', use_bias=False,kernel_initializer = he_normal(seed = 426))(x)
x = layers.BatchNormalization()(x)
x = layers.GlobalAvgPool2D()(x)
x = layers.GaussianNoise(0.1)(x)
x = layers.Dropout(0.2)(x)
x = layers.Dense(2, activation = 'softmax', name = 'top')(x)

model = Model(model_input, x)
model.summary()
model.compile(adam(), loss = 'binary_crossentropy')


"""
ABC-Mart....
"""

from keras.callbacks import TensorBoard, ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
log_dir = 'logs/oc_cnn/'
logging = TensorBoard(log_dir=log_dir)
#ModelCheckpoint(log_dir + 'ep{epoch:03d}-loss{loss:.3f}-train_loss{train_loss:.3f}.h5',
#    monitor='train_loss', save_weights_only=True, save_best_only=True, period=3)
checkpoint_acc = ModelCheckpoint(log_dir + 'best_acc.h5',
    monitor='val_binary_accuracy', save_weights_only=False, save_best_only=True, period=1)

checkpoint_loss = ModelCheckpoint(log_dir + 'min_loss.h5',
    monitor='val_loss', save_weights_only=False, save_best_only=True, period=1)

reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=3, verbose=1)
early_stopping = EarlyStopping(monitor='val_loss', min_delta=0, patience=7, verbose=1)


"""
Two-Stage training trick
#"""
dropout_rate = 0.2
n_classes = 2
#import efficientnet.keras as efn 
#base_model = efn.EfficientNetB0(weights='imagenet',  include_top=False)
#x = base_model.output
#x = layers.GlobalAveragePooling2D()(x)
#x = layers.Dropout(dropout_rate, name='top_dropout')(x)
#predictions = layers.Dense(n_classes, activation='softmax', name='probs')(x)
#
#model = Model(inputs=base_model.input, outputs=predictions)

#for layer in base_model.layers:
#    layer.trainable = False

annotation_path = 'train/data/33.txt'
with open (annotation_path, 'r') as f:
    lines = f.readlines()
    
num_train = len(lines)
num_val = num_train

# Stage 1 
model.compile(optimizer=adam(), loss='binary_crossentropy', metrics = ['binary_accuracy'])
batch_size = 256
print('Train on {} samples, val on {} samples, with batch size {}.'.format(num_train, num_val, batch_size))
history_freeze = model.fit_generator(data_generator_wrapper(lines, batch_size, input_shape),
        steps_per_epoch=max(1, num_train//batch_size),
        validation_data=data_generator_wrapper(lines, batch_size, input_shape),
        validation_steps=max(1, num_val//batch_size),
        epochs=50,
        initial_epoch=0,
        callbacks=[logging, checkpoint_acc, checkpoint_loss, reduce_lr, early_stopping])
model.save(log_dir + 'trained_model_stage_1.h5')

# Stage 2
#batch_size = 64
#for layer in model.layers[:230]:
#   layer.trainable = True
#
#model.compile(optimizer=SGD(lr=1e-4, momentum=0.9), loss='binary_crossentropy', metrics = ['binary_accuracy'])
#print('Train on {} samples, val on {} samples, with batch size {}.'.format(num_train, num_val, batch_size))
#history_unfreeze = model.fit_generator(data_generator_wrapper(lines, batch_size, input_shape),
#        steps_per_epoch=max(1, num_train//batch_size),
#        validation_data=data_generator_wrapper(lines, batch_size, input_shape),
#        validation_steps=max(1, num_train//batch_size),
#        epochs=52,
#        initial_epoch=25,
#        callbacks=[logging, checkpoint_acc, checkpoint_loss, reduce_lr, early_stopping])
#model.save(log_dir + 'trained_model_stage_2.h5')

