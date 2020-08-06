# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:15:56 2020

@author: Public_2080
"""

from keras.callbacks import TensorBoard, ModelCheckpoint, ReduceLROnPlateau, EarlyStopping


logging = TensorBoard(log_dir=log_dir)
#ModelCheckpoint(log_dir + 'ep{epoch:03d}-loss{loss:.3f}-train_loss{train_loss:.3f}.h5',
    #monitor='train_loss', save_weights_only=True, save_best_only=True, period=3)
checkpoint = ModelCheckpoint(log_dir + 'ep{epoch:03d}.h5',
    monitor='val_loss', save_weights_only=True, save_best_only=True, period=2)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=3, verbose=1)
early_stopping = EarlyStopping(monitor='val_loss', min_delta=0, patience=25, verbose=1)