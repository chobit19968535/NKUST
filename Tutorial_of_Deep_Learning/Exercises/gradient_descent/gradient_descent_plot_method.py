# coding: utf-8
import numpy as np
import matplotlib.pylab as plt
from gradient_descent import gradient_descent

def function_2(x):
    return (x[0]**2 + x[1]**2)

init_x = np.array([-3.0, 4.0])    
x, x_history = gradient_descent(function_2, init_x, lr=1e-3 ,step_num=1000)

plt.plot( [-5, 5], [0,0], '--b')
plt.plot( [0,0], [-5, 5], '--b')
plt.plot(x_history[:,0], x_history[:,1], 'o')

plt.xlim(-3.5, 3.5)
plt.ylim(-4.5, 4.5)
plt.xlabel("X0")
plt.ylabel("X1")
plt.show()
