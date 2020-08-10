# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:06:30 2020

@author: Lycoris radiata
"""


import sys, os
sys.path.append(os.pardir)  
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient

np.random.seed(426)
epochs = 10
class simpleNet:
    def __init__(self):
        self.lr = 1.0
        # init Weights
        self.W = np.random.randn(2,3)

    def predict(self, x):
        # Forward Propagation
        return np.dot(x, self.W)

    def loss(self, x, t):
        # Backward Propagation for getting loss
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        return loss
    
    def update(self, dw):
        # Update
        self.W = self.W - self.lr*dw
        return(self.W)
    
x = np.array([0.6, 0.9]) # Input
t = np.array([0, 0, 1]) # one-hot

net = simpleNet()
print('INIT_Weights[0][0]:\n', net.W[0][0],'\n')
for epoch in range(epochs):
    print('epoch={}, loss={}'.format(epoch, net.loss(x,t)))
    f = lambda w: net.loss(x, t) #計算LOSS FUNCTION
    dW = numerical_gradient(f, net.W) #執行梯度下降 partial(L)/partcial(x)
    net.update(dW) #x' = x- dW
    print('DW[0][0]:\n',dW[0][0],'\n')
print('Updated_W:\n', net.W[0][0],'\n')