# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:31:52 2020

@author: Public_2080
"""
import numpy as np
import PIL.Image as Image
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb
from matplotlib.pyplot import imshow

input_shape = (320,320)
image = Image.open('B104_B103_1.jpg')
iw, ih = image.size
h, w = input_shape
def rand(a=0, b=1):
    return np.random.rand()*(b-a) + a

hue = 0.1
sat = 1.5
val = .5
jitter = 0.3
flip = False

"""
Jitter
"""

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

"""
Shift
"""

dx = int(rand(0, w-nw))
dy = int(rand(0, h-nh))
new_image = Image.new('RGB', (w,h), (128,128,128))
new_image.paste(image, (dx, dy))
image = new_image
imshow(image)
image.save('Jitter3.jpg')
"""
Flip
"""
if flip: image = image.transpose(Image.FLIP_LEFT_RIGHT)
imshow(image)

"""
add HSV Noice
"""

hsv = rand(-hue, hue)
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
image_data = hsv_to_rgb(x)
image_data = np.asarray(image_data*255, dtype='uint8')
image_data = Image.fromarray(image_data)
imshow(image_data)
image_data.save('HSV_noice3.jpg')
